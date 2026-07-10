# Convex Evals Harbor Port

Harbor port of all 76 tasks from the official
[get-convex/convex-evals](https://github.com/get-convex/convex-evals)
benchmark, pinned to commit
5c723ca8177c3ae167e505a95c755bd398f9dea2.

## Design

- Uses Convex's exact rendered system and user prompts.
- Makes exactly one model call per task.
- Parses the upstream Files response format.
- Uses Convex's original scorer and graders.
- Supports Google Gemini Interactions and OpenAI-compatible Chat Completions.
- Allows forced routing through the custom agent option api=gemini or
  api=openai.

## Task variants

- `tasks/` contains the official `with_guidelines` prompt variant.
- `tasks-no-guidelines/` contains the official `no_guidelines` prompt variant.

Each `instruction.md` begins with Convex's required output format. The `...`
inside the example `package.json`, `tsconfig.json`, and `convex/schema.ts`
code fences are intentional placeholders showing the response structure; they
are not empty starter files. The actual eval request appears at the bottom
under `Now, implement a Convex backend...` and is copied verbatim from that
eval's upstream `TASK.txt`.

The empty `[environment.env]` and `[solution.env]` tables in `task.toml` are
valid Harbor configuration and mean that the task supplies no additional
environment variables. They do not remove content from the model prompt.

The verifier clones the pinned official source after generation, keeping
reference answers and graders unavailable during the model call.

## Run locally

Install Harbor, set provider credentials, and run:

    PYTHONPATH=. harbor run \
      --path tasks \
      --agent agent.convex_single_shot:ConvexSingleShotAgent \
      --model gemini/gemini-3.5-flash \
      --ak api=gemini \
      -n 30

To run the same benchmark without the embedded Convex guidelines, change
`--path tasks` to `--path tasks-no-guidelines`. No agent or grader change is
required.

For the direct OpenAI API, set OPENAI_API_KEY and use an OpenAI model:

    PYTHONPATH=. harbor run \
      --path tasks \
      --agent agent.convex_single_shot:ConvexSingleShotAgent \
      --model openai/gpt-5 \
      --ak api=openai \
      -n 30

## Results

| Model | API | Tasks | Passed | Score |
|---|---|---:|---:|---:|
| Gemini 3.5 Flash | OpenRouter, Convex native | 76 | 44 | 57.9% |
| Gemini 3.5 Flash | OpenRouter + Harbor/Daytona | 76 | 42 | 55.3% |

See the [parity report](reports/gemini-3.5-flash-parity-2026-07-10.md).

The Harbor score is 2 tasks (2.6 percentage points) below the independent
native Convex run. All 76 prompts and all 76 parsed response file maps were
verified against Convex's implementations. The final Harbor rescore ran in
Daytona EU with zero infrastructure exceptions.

The [live Convex dashboard](https://convex-evals.netlify.app/model/k575nhxzwg69c00qa4mjr20dsx873bws)
reports Gemini 3.5 Flash at 67.5% with guidelines
and 70.9% without guidelines across its displayed run aggregates. Its latest
completed direct-Google runs scored 43/76 (56.6%) with guidelines and 48/76
(63.2%) without guidelines. A paired five-task Harbor smoke test showed the
same direction: 2/5 with guidelines versus 3/5 without guidelines. This small
slice is diagnostic only and is not a benchmark-wide uplift estimate.

The direct OpenAI run is pending because the configured key returned HTTP 401
from api.openai.com; no OpenAI result is claimed here.

## Validation

- Harbor task validation: 76/76.
- Native Gemini full benchmark: 76/76 valid task results after retrying only
  infrastructure exceptions from the concurrency-30 stress run.
- Prompt equality and parser equality are checked by tools/check_parity.py.
