#!/usr/bin/env python3
"""Compare every saved Harbor response with Convex's prompt and parser."""

import argparse
import json
import os
import subprocess
import sys
import tomllib
from pathlib import Path

sys.path.insert(0, "/home/nanoclaw/benchmark-lab")
from benchmarks.convex_harbor_agent import ConvexSingleShotAgent  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--tasks", type=Path, required=True)
    parser.add_argument("--source", type=Path, required=True)
    args = parser.parse_args()

    bun = "/home/nanoclaw/.bun/bin/bun"
    render_code = (
        'import { renderPrompt } from "./runner/models/modelCodegen.ts";'
        "process.stdout.write(renderPrompt(await Bun.stdin.text()));"
    )
    parse_code = (
        'import { readFileSync } from "node:fs";'
        'import { parseMarkdownResponse } from "./runner/models/modelCodegen.ts";'
        'process.stdout.write(JSON.stringify(parseMarkdownResponse('
        'readFileSync(process.argv[1], "utf8"))));'
    )

    prompt_mismatches = []
    parser_mismatches = []
    checked = 0
    for result_path in sorted(args.run.glob("*/result.json")):
        result = json.loads(result_path.read_text())
        task_name = result["task_name"].split("/")[-1]
        task_root = args.tasks / task_name
        response_path = result_path.parent / "agent/model-response.md"
        if not response_path.exists():
            continue
        config = tomllib.loads((task_root / "task.toml").read_text())
        eval_path = config["metadata"]["source_eval"]
        raw_task = (args.source / "evals" / eval_path / "TASK.txt").read_text()

        official_prompt = subprocess.run(
            [bun, "-e", render_code], cwd=args.source, input=raw_task,
            text=True, stdout=subprocess.PIPE, check=True,
        ).stdout
        harbor_prompt = (task_root / "instruction.md").read_text()
        if official_prompt != harbor_prompt:
            prompt_mismatches.append(task_name)

        official_files = json.loads(subprocess.run(
            [bun, "-e", parse_code, str(response_path.resolve())],
            cwd=args.source, text=True, stdout=subprocess.PIPE, check=True,
        ).stdout)
        harbor_files = ConvexSingleShotAgent._parse_files(response_path.read_text())
        if official_files != harbor_files:
            parser_mismatches.append(task_name)
        checked += 1

    print(json.dumps({
        "checked": checked,
        "prompt_mismatches": prompt_mismatches,
        "parser_mismatches": parser_mismatches,
    }, indent=2))


if __name__ == "__main__":
    main()
