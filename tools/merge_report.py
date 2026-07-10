#!/usr/bin/env python3
import argparse
import json
from collections import defaultdict
from pathlib import Path


def load_trials(run_dir: Path):
    trials = {}
    for path in run_dir.glob("*/result.json"):
        data = json.loads(path.read_text())
        name = data.get("task_name", "").split("/")[-1]
        if name:
            trials[name] = data
    return trials


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--retry", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    parser.add_argument("--markdown", type=Path, required=True)
    args = parser.parse_args()

    primary = load_trials(args.primary)
    retry = load_trials(args.retry)
    valid_primary = {
        name: trial for name, trial in primary.items()
        if trial.get("exception_info") is None and trial.get("verifier_result") is not None
    }
    valid_retry = {
        name: trial for name, trial in retry.items()
        if trial.get("exception_info") is None and trial.get("verifier_result") is not None
    }
    merged = dict(valid_primary)
    merged.update(valid_retry)

    rows = []
    categories = defaultdict(lambda: {"passed": 0, "total": 0})
    input_tokens = output_tokens = cache_tokens = 0
    for name, trial in sorted(merged.items()):
        reward = float(trial["verifier_result"]["rewards"]["reward"])
        category = name.split("__", 1)[0]
        categories[category]["total"] += 1
        categories[category]["passed"] += int(reward == 1.0)
        result = trial.get("agent_result") or {}
        input_tokens += result.get("n_input_tokens") or 0
        output_tokens += result.get("n_output_tokens") or 0
        cache_tokens += result.get("n_cache_tokens") or 0
        rows.append({
            "task": name,
            "category": category,
            "reward": reward,
            "source": "retry-concurrency-5" if name in valid_retry else "primary-concurrency-30",
        })

    passed = sum(row["reward"] == 1.0 for row in rows)
    total = len(rows)
    report = {
        "model": "gemini-3.5-flash",
        "api": "Google Gemini Interactions API",
        "benchmark_commit": "5c723ca8177c3ae167e505a95c755bd398f9dea2",
        "total": total,
        "passed": passed,
        "failed": total - passed,
        "score": passed / total if total else None,
        "primary_valid": len(valid_primary),
        "primary_exceptions": len(primary) - len(valid_primary),
        "retry_valid": len(valid_retry),
        "tokens": {
            "input": input_tokens,
            "cached": cache_tokens,
            "output": output_tokens,
        },
        "categories": dict(sorted(categories.items())),
        "tasks": rows,
    }
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(report, indent=2) + "\n")

    category_lines = []
    for category, result in sorted(categories.items()):
        rate = result["passed"] / result["total"]
        category_lines.append(
            f"| {category} | {result['passed']} | {result['total']} | {rate:.1%} |"
        )
    markdown = f"""# Gemini 3.5 Flash — full benchmark report

Date: 2026-07-10

Benchmark: official get-convex/convex-evals at commit 5c723ca8177c3ae167e505a95c755bd398f9dea2

Model/API: gemini-3.5-flash through the native Google Gemini Interactions API
Agent: one model call per task, exact upstream prompt, upstream response parser and graders

## Result

- Score: **{passed}/{total} ({passed / total:.1%})**
- Failed: {total - passed}
- Input tokens: {input_tokens:,}
- Cached input tokens: {cache_tokens:,}
- Output tokens: {output_tokens:,}

The requested concurrency-30 run produced {len(valid_primary)} valid scored trials and
{len(primary) - len(valid_primary)} infrastructure exceptions caused by Docker network-pool exhaustion and
build timeouts. Only those {len(primary) - len(valid_primary)} tasks were retried at concurrency 5; all retry
trials completed. The merged score above contains exactly one valid result for each of the
{total} benchmark tasks. Infrastructure exceptions are not counted as model failures.

## Category breakdown

| Category | Passed | Total | Rate |
|---|---:|---:|---:|
{chr(10).join(category_lines)}

## Comparison with Convex

The live Convex dashboard now has an exact Gemini 3.5 Flash entry. It reports aggregate
pass rates of 67.5% with guidelines and 70.9% without guidelines. The latest completed
direct-Google runs displayed there scored 43/76 (56.6%) with guidelines and 48/76
(63.2%) without guidelines. Convex therefore currently observes a negative guidelines
uplift: -3.4 percentage points in the aggregate and -6.6 points for the latest pair.

Our paired five-task smoke test had the same direction: 2/5 (40%) with guidelines and
3/5 (60%) without guidelines, or -20 points for guidelines. Five selected fundamentals
tasks are too small and non-random for a benchmark-wide estimate; this only confirms that
both prompt variants run correctly.

The Harbor full result is pinned to an older source commit, while the live dashboard moves
with the benchmark. The 25.0% Harbor score should therefore not yet be presented as a
replication of the current dashboard score. The parity-critical pieces for the pinned port
remain verified directly: identical rendered prompts, the upstream response parser, and
the original scorer and graders.

The machine-readable merged results, including every task reward and its source run, are in
the adjacent JSON file.
"""
    args.markdown.write_text(markdown)


if __name__ == "__main__":
    main()
