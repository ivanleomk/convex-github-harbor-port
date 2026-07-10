# Gemini 3.5 Flash parity report

Date: 2026-07-10

Benchmark: get-convex/convex-evals at `5c723ca8177c3ae167e505a95c755bd398f9dea2`

Experiment: with Convex guidelines
Model: `google/gemini-3.5-flash` through OpenRouter, medium reasoning

## Result

| Runner | Passed | Total | Score |
|---|---:|---:|---:|
| Convex native runner | 44 | 76 | 57.9% |
| Harbor single-shot port | 42 | 76 | 55.3% |

The Harbor port is 2 tasks, or 2.6 percentage points, below the independent
native run. Convex's live dashboard recently reported 43/76 (56.6%) for the
same model and guidelines experiment. These results are reasonably close for
independent stochastic generations.

## Category comparison

| Category | Convex native | Harbor | Delta |
|---|---:|---:|---:|
| Fundamentals | 5/10 | 3/10 | -2 |
| Data Modeling | 10/15 | 13/15 | +3 |
| Queries | 15/24 | 10/24 | -5 |
| Mutations | 3/8 | 5/8 | +2 |
| Actions | 4/8 | 4/8 | 0 |
| Idioms | 5/8 | 5/8 | 0 |
| Clients | 2/3 | 2/3 | 0 |

## Verified parity

- All 76 Harbor instructions are byte-identical to Convex's `renderPrompt()`
  output for the pinned commit.
- Convex's parser and the Harbor parser produced identical file maps for all
  76 saved Harbor model responses.
- Both runners used the same system prompt, model slug, guidelines variant,
  16,384-token output limit, and medium reasoning effort.
- Harbor delegates grading to the pinned official `convexScorer` and records a
  pass only when every scorer stage is exactly 1.
- The Harbor rescore completed in Daytona EU with 76 trials and zero
  infrastructure exceptions.

The native and Harbor scores come from independent model generations. Harbor's
OpenRouter responses were replayed only to replace an invalid local-Docker
scoring attempt that hit GitHub API limits; replay did not alter model text or
parsed files and made no additional model calls.

## Source links

- [Official Convex benchmark](https://github.com/get-convex/convex-evals)
- [Pinned Convex scorer](https://github.com/get-convex/convex-evals/blob/5c723ca8177c3ae167e505a95c755bd398f9dea2/runner/scorer.ts)
- [Pinned Convex prompt renderer](https://github.com/get-convex/convex-evals/blob/5c723ca8177c3ae167e505a95c755bd398f9dea2/runner/models/modelCodegen.ts)
- [Live Gemini 3.5 Flash results](https://convex-evals.netlify.app/model/k575nhxzwg69c00qa4mjr20dsx873bws)
