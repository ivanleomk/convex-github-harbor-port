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

The verifier clones the pinned official source after generation, keeping
reference answers and graders unavailable during the model call.

## Run locally

Install Harbor, set provider credentials, and run:

    PYTHONPATH=. harbor run \
      --path tasks \
      --agent agent.convex_single_shot:ConvexSingleShotAgent \
      --model google/gemini-3.5-flash \
      --ak api=openai \
      --n-tasks 5 \
      -n 2

For Kaggle's Model Proxy:

    kaggle benchmarks auth -y --env-file .env
    set -a
    . ./.env
    set +a
    export OPENAI_API_KEY="$MODEL_PROXY_API_KEY"
    export OPENAI_BASE_URL="\${MODEL_PROXY_URL%/}/openapi"

## Validation

- Harbor task validation: 76/76.
- Kaggle Model Proxy shell smoke: google/gemini-3.5-flash returned HTTP 200.
- Five-task sample with concurrency 2: 4/5 passed, no infrastructure
  exceptions.
- Prompt equality and parser equality are checked by tools/check_parity.py.
