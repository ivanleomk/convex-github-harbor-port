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

The pinned official benchmark does not list Gemini 3.5 Flash among its published model
configurations, so there is no exact official Gemini 3.5 Flash score for an apples-to-apples
numeric comparison. This port instead verifies the parity-critical pieces directly: the
rendered system and user prompts are identical, the response parser matches upstream, and
the original scorer and graders execute inside each Harbor task.

Results should not be compared numerically with a different Gemini release or with results
served through a different provider/API, because the underlying model and inference path
would differ.

The machine-readable merged results, including every task reward and its source run, are in
the adjacent JSON file.
