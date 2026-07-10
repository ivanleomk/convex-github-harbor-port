#!/usr/bin/env python3
"""Copy the readable verifier adapter into every self-contained Harbor task."""

import argparse
import tomllib
from pathlib import Path

SOURCE_COMMIT = "5c723ca8177c3ae167e505a95c755bd398f9dea2"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--typescript-template", type=Path, required=True)
    parser.add_argument("--shell-template", type=Path, required=True)
    parser.add_argument("--docker-template", type=Path)
    args = parser.parse_args()

    typescript = args.typescript_template.read_text()
    shell = args.shell_template.read_text()
    count = 0
    for task_root_name in ("tasks", "tasks-no-guidelines"):
        for task in sorted((args.repo / task_root_name).iterdir()):
            if not task.is_dir():
                continue
            config = tomllib.loads((task / "task.toml").read_text())
            eval_path = config["metadata"]["source_eval"]
            (task / "tests/harborScoreProject.ts").write_text(typescript)
            test_script = shell.replace("__SOURCE_COMMIT__", SOURCE_COMMIT).replace(
                "__EVAL_PATH__", eval_path
            )
            test_path = task / "tests/test.sh"
            test_path.write_text(test_script)
            test_path.chmod(0o755)
            if args.docker_template:
                (task / "environment/Dockerfile").write_text(
                    args.docker_template.read_text()
                )
            count += 1
    print(f"Updated verifier files for {count} tasks")


if __name__ == "__main__":
    main()
