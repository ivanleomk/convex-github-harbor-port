#!/usr/bin/env python3
from pathlib import Path
import shutil
import subprocess

SOURCE = Path("/home/nanoclaw/benchmark-lab/.workspace/repos/convex-evals")
OUT = Path("/home/nanoclaw/benchmark-lab/.workspace/datasets/convex-evals-harbor")
COMMIT = "5c723ca8177c3ae167e505a95c755bd398f9dea2"
BUN = shutil.which("bun") or "/home/nanoclaw/.bun/bin/bun"

DOCKER = """FROM oven/bun:1.3.8
RUN apt-get update && apt-get install -y --no-install-recommends git ca-certificates && rm -rf /var/lib/apt/lists/*
WORKDIR /app
"""

TASK = """schema_version = "1.3"
artifacts = ["/logs/verifier/summary.json"]
[task]
name = "benchmark-lab/{name}"
description = "Official Convex eval {eval_rel}, ported to Harbor."
keywords = ["convex", "typescript", "coding"]
[[task.authors]]
name = "Convex"
[metadata]
source_repository = "https://github.com/get-convex/convex-evals.git"
source_commit = "{commit}"
source_eval = "{eval_rel}"
[verifier]
timeout_sec = 1200.0
[agent]
timeout_sec = 900.0
[environment]
network_mode = "public"
build_timeout_sec = 900.0
os = "linux"
mcp_servers = []
[environment.env]
[solution.env]
"""

TEST = """#!/bin/bash
set -uo pipefail
mkdir -p /logs/verifier
trap 'echo 0 > /logs/verifier/reward.txt' ERR
git clone --quiet https://github.com/get-convex/convex-evals.git /tmp/convex-evals
test "$(git -C /tmp/convex-evals remote get-url origin)" = "https://github.com/get-convex/convex-evals.git"
git -C /tmp/convex-evals checkout --quiet {commit}
test "$(git -C /tmp/convex-evals rev-parse HEAD)" = "{commit}"
cp /tests/harborScoreProject.ts /tmp/convex-evals/scripts/harborScoreProject.ts
cd /tmp/convex-evals
bun install --frozen-lockfile
bun run scripts/harborScoreProject.ts --eval "{eval_rel}" --project /app --summary /logs/verifier/summary.json
node -e 'const fs=require("fs");const s=JSON.parse(fs.readFileSync("/logs/verifier/summary.json","utf8"));if(!Number.isFinite(s.reward)||s.reward<0||s.reward>1)process.exit(1);fs.writeFileSync("/logs/verifier/reward.txt",String(s.reward)+"\\n");'
"""

SCORER = """#!/usr/bin/env bun
import { existsSync, mkdirSync, readdirSync, readFileSync, writeFileSync } from "fs";
import { join, relative, resolve } from "path";
import { convexScorer } from "../runner/scorer.js";
function value(flag: string): string {
  const i = process.argv.indexOf(flag);
  if (i < 0 || !process.argv[i + 1]) throw new Error("Missing argument " + flag);
  return process.argv[i + 1];
}
function files(project: string): Record<string, string> {
  const root = resolve(project), result: Record<string, string> = {};
  const skip = new Set(["node_modules", ".git", ".cache", ".next"]);
  function visit(dir: string): void {
    for (const entry of readdirSync(dir, {withFileTypes:true})) {
      if (skip.has(entry.name)) continue;
      const path = join(dir, entry.name);
      if (entry.isDirectory()) visit(path);
      else if (entry.isFile()) result[relative(root, path).replaceAll("\\\\", "/")] = readFileSync(path, "utf8");
    }
  }
  if (existsSync(root)) visit(root);
  return result;
}
const evalRel=value("--eval"), project=value("--project"), summary=value("--summary");
const parts=evalRel.split("/");
const scores=await convexScorer("/tmp/harbor-convex-score",readFileSync(join("evals",evalRel,"TASK.txt"),"utf8"),{},{model:"harbor-agent",category:parts[0],eval_name:parts[1]},files(project));
const reward=scores.length ? Math.min(...scores.map((s)=>s.score)) : 0;
mkdirSync(resolve(summary,".."),{recursive:true});
writeFileSync(summary,JSON.stringify({eval:evalRel,reward,scores},null,2));
"""

def instruction(task):
    code = (
        'import { renderPrompt } from "./runner/models/modelCodegen.ts";'
        "process.stdout.write(renderPrompt(await Bun.stdin.text()));"
    )
    return subprocess.run(
        [BUN, "-e", code],
        cwd=SOURCE,
        input=task,
        text=True,
        stdout=subprocess.PIPE,
        check=True,
    ).stdout

def main():
    if not (SOURCE / ".git").exists():
        raise SystemExit("Official source clone missing")
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "tasks").mkdir(parents=True)
    names = []
    evals = [
        path.parent.relative_to(SOURCE / "evals").as_posix()
        for path in sorted(SOURCE.glob("evals/*/*/TASK.txt"))
    ]
    for eval_rel in evals:
        name = eval_rel.replace("/", "__")
        names.append(name)
        root = OUT / "tasks" / name
        (root / "environment").mkdir(parents=True)
        (root / "tests").mkdir()
        (root / "environment/Dockerfile").write_text(DOCKER)
        (root / "task.toml").write_text(TASK.format(name=name, eval_rel=eval_rel, commit=COMMIT))
        task_text = (SOURCE / "evals" / eval_rel / "TASK.txt").read_text()
        (root / "instruction.md").write_text(instruction(task_text))
        test = root / "tests/test.sh"
        test.write_text(TEST.format(eval_rel=eval_rel, commit=COMMIT))
        test.chmod(0o755)
        (root / "tests/harborScoreProject.ts").write_text(SCORER)
    entries = "\n".join('  "tasks/' + n + '",' for n in names)
    (OUT / "dataset.toml").write_text("""schema_version = "1.0"
[dataset]
name = "benchmark-lab/convex-evals-harbor"
description = "All official Convex evals ported to Harbor."
[metadata]
source_repository = "https://github.com/get-convex/convex-evals.git"
source_commit = "COMMIT"
tasks = [
ENTRIES
]
""".replace("COMMIT", COMMIT).replace("ENTRIES", entries))
    print(OUT)
if __name__ == "__main__":
    main()
