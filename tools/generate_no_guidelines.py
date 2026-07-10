#!/usr/bin/env python3
"""Generate the no-guidelines task tree from the canonical Harbor tasks."""

import argparse
import os
import shutil
import subprocess
import tomllib
from pathlib import Path

DEFAULT_SOURCE = Path("/home/nanoclaw/benchmark-lab/.workspace/repos/convex-evals")
DEFAULT_TASKS = Path("/home/nanoclaw/convex-github-harbor-port/tasks")
DEFAULT_OUTPUT = Path("/home/nanoclaw/convex-github-harbor-port/tasks-no-guidelines")
DEFAULT_BUN = "/home/nanoclaw/.bun/bin/bun"


def render_no_guidelines(source: Path, bun: str, task_text: str) -> str:
    code = (
        'import { renderPrompt } from "./runner/models/modelCodegen.ts";'
        "process.stdout.write(renderPrompt(await Bun.stdin.text()));"
    )
    env = dict(os.environ, EVALS_EXPERIMENT="no_guidelines")
    return subprocess.run(
        [bun, "-e", code], cwd=source, env=env, input=task_text,
        text=True, stdout=subprocess.PIPE, check=True,
    ).stdout


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--tasks", type=Path, default=DEFAULT_TASKS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--bun", default=DEFAULT_BUN)
    args = parser.parse_args()

    if args.output.exists():
        shutil.rmtree(args.output)
    args.output.mkdir(parents=True)

    count = 0
    for source_task in sorted(path for path in args.tasks.iterdir() if path.is_dir()):
        target = args.output / source_task.name
        shutil.copytree(source_task, target)
        config = tomllib.loads((target / "task.toml").read_text())
        eval_rel = config["metadata"]["source_eval"]
        task_text = (args.source / "evals" / eval_rel / "TASK.txt").read_text()
        instruction = render_no_guidelines(args.source, args.bun, task_text)
        assert "# Convex guidelines" not in instruction
        assert task_text in instruction
        (target / "instruction.md").write_text(instruction)

        toml = (target / "task.toml").read_text()
        toml = toml.replace(
            f'description = "Official Convex eval {eval_rel}, ported to Harbor."',
            f'description = "Official Convex eval {eval_rel}, without guidelines."',
        )
        toml = toml.replace(
            f'source_eval = "{eval_rel}"',
            f'source_eval = "{eval_rel}"\nexperiment = "no_guidelines"',
        )
        (target / "task.toml").write_text(toml)
        count += 1

    print(f"Generated {count} no-guidelines tasks in {args.output}")


if __name__ == "__main__":
    main()
