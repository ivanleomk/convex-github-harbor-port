# Multi-model benchmark results

Date: 2026-07-10

Benchmark: get-convex/convex-evals at `5c723ca8177c3ae167e505a95c755bd398f9dea2`

Experiment: with Convex guidelines

Provider/scoring: OpenRouter generation, Harbor single-shot agent, Daytona EU

## Overall results

| Model | Passed | Total | Score |
|---|---:|---:|---:|
| Anthropic Claude Haiku 4.5 | 53 | 76 | 69.7% |
| Google Gemini 3.5 Flash | 42 | 76 | 55.3% |
| OpenAI GPT-5 Mini | 38 | 76 | 50.0% |

Every model used the same with-guidelines prompts, single-response parser, and
strict official Convex scorer. All 152 new GPT-5 Mini and Claude Haiku trials
completed without infrastructure exceptions.

## Category breakdown

| Category | Claude Haiku 4.5 | Gemini 3.5 Flash | GPT-5 Mini |
|---|---:|---:|---:|
| Fundamentals | 7/10 | 3/10 | 4/10 |
| Data Modeling | 12/15 | 13/15 | 6/15 |
| Queries | 20/24 | 10/24 | 17/24 |
| Mutations | 6/8 | 5/8 | 4/8 |
| Actions | 4/8 | 4/8 | 3/8 |
| Idioms | 4/8 | 5/8 | 3/8 |
| Clients | 0/3 | 2/3 | 1/3 |

These are single independent runs, so small differences should not be treated
as stable model rankings without repeated trials.
