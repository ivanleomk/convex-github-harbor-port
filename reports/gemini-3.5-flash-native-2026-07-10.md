# Gemini 3.5 Flash — full benchmark report

Date: 2026-07-10  
Benchmark: official get-convex/convex-evals at commit 5c723ca8177c3ae167e505a95c755bd398f9dea2  
Model/API: gemini-3.5-flash through the native Google Gemini Interactions API  
Agent: one model call per task, exact upstream prompt, upstream response parser and graders

## Result

- Score: **19/76 (25.0%)**
- Failed: 57
- Input tokens: 444,000
- Cached input tokens: 140,419
- Output tokens: 62,041

The requested concurrency-30 run produced 50 valid scored trials and
26 infrastructure exceptions caused by Docker network-pool exhaustion and
build timeouts. Only those 26 tasks were retried at concurrency 5; all retry
trials completed. The merged score above contains exactly one valid result for each of the
76 benchmark tasks. Infrastructure exceptions are not counted as model failures.

## Category breakdown

| Category | Passed | Total | Rate |
|---|---:|---:|---:|
| 000-fundamentals | 1 | 10 | 10.0% |
| 001-data_modeling | 6 | 15 | 40.0% |
| 002-queries | 8 | 24 | 33.3% |
| 003-mutations | 2 | 8 | 25.0% |
| 004-actions | 1 | 8 | 12.5% |
| 005-idioms | 0 | 8 | 0.0% |
| 006-clients | 1 | 3 | 33.3% |

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
