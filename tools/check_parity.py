#!/usr/bin/env python3
"""Check prompt and parser parity against the official Convex implementation."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

try:
    from agent.convex_single_shot import ConvexSingleShotAgent
except ImportError:
    from benchmarks.convex_harbor_agent import ConvexSingleShotAgent


LAB = Path("/home/nanoclaw/benchmark-lab")
REPO = LAB / ".workspace/repos/convex-evals"
BUN = "/home/nanoclaw/.bun/bin/bun"


def main() -> None:
    eval_rel = sys.argv[1]
    task_dir = Path(sys.argv[2]).resolve()
    response_path = Path(sys.argv[3]).resolve()

    official_prompt = subprocess.run(
        [
            BUN,
            "run",
            "scripts/kaggleRenderPrompt.ts",
            "--eval",
            eval_rel,
        ],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        check=True,
    ).stdout
    harbor_prompt = (task_dir / "instruction.md").read_text()

    parse_code = (
        'import { readFileSync } from "fs";'
        'import { parseMarkdownResponse } from "./runner/models/modelCodegen.ts";'
        "process.stdout.write(JSON.stringify("
        "parseMarkdownResponse(readFileSync(process.argv[1], 'utf8'))));"
    )
    official_files = json.loads(
        subprocess.run(
            [BUN, "-e", parse_code, str(response_path)],
            cwd=REPO,
            text=True,
            stdout=subprocess.PIPE,
            check=True,
        ).stdout
    )
    harbor_files = ConvexSingleShotAgent._parse_files(response_path.read_text())

    print("prompt_same=" + str(harbor_prompt == official_prompt).lower())
    print("parsed_result_same=" + str(harbor_files == official_files).lower())
    print("files=" + ",".join(sorted(harbor_files)))
    if harbor_prompt != official_prompt or harbor_files != official_files:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
