#!/usr/bin/env python3
import os
import shutil
import subprocess
import tomllib
from pathlib import Path

SOURCE = Path("/home/nanoclaw/benchmark-lab/.workspace/repos/convex-evals")
WITH_GUIDELINES = Path("/home/nanoclaw/convex-github-harbor-port/tasks")
OUT = Path("/home/nanoclaw/benchmark-lab/.workspace/datasets/convex-evals-smoke-no-guidelines/tasks")
BUN = "/home/nanoclaw/.bun/bin/bun"
TASKS = [
    "000-fundamentals__000-empty_functions",
    "000-fundamentals__001-basic_schema",
    "000-fundamentals__003-crons",
    "000-fundamentals__004-scheduler",
    "000-fundamentals__005-function_calling",
]


def render_no_guidelines(task_text: str) -> str:
    code = (
        'import { renderPrompt } from "./runner/models/modelCodegen.ts";'
        "process.stdout.write(renderPrompt(await Bun.stdin.text()));"
    )
    env = dict(os.environ, EVALS_EXPERIMENT="no_guidelines")
    return subprocess.run(
        [BUN, "-e", code], cwd=SOURCE, env=env, input=task_text,
        text=True, stdout=subprocess.PIPE, check=True,
    ).stdout


def main() -> None:
    if OUT.parent.exists():
        shutil.rmtree(OUT.parent)
    OUT.mkdir(parents=True)
    for name in TASKS:
        source_task = WITH_GUIDELINES / name
        target = OUT / name
        shutil.copytree(source_task, target)
        metadata = tomllib.loads((target / "task.toml").read_text())["metadata"]
        task_text = (SOURCE / "evals" / metadata["source_eval"] / "TASK.txt").read_text()
        (target / "instruction.md").write_text(render_no_guidelines(task_text))
        instruction = (target / "instruction.md").read_text()
        assert "# Convex guidelines" not in instruction
    print(OUT)


if __name__ == "__main__":
    main()
