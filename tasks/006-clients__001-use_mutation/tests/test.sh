#!/usr/bin/env bash
set -uo pipefail

# This wrapper intentionally delegates all grading to Convex's official code.
# Source benchmark: https://github.com/get-convex/convex-evals
# The placeholders below are filled per task by tools/sync_verifier_files.py.
SOURCE_COMMIT="5c723ca8177c3ae167e505a95c755bd398f9dea2"
EVAL_PATH="006-clients/001-use_mutation"
UPSTREAM_REPOSITORY="https://github.com/get-convex/convex-evals.git"
UPSTREAM_CHECKOUT="/tmp/convex-evals"
SUMMARY_PATH="/logs/verifier/summary.json"

# Harbor expects a reward even if setup or the official scorer exits early.
# We intentionally do not enable `set -e`: Convex's scorer reports failures in
# the score array, and the final block below must still translate that result.
mkdir -p /logs/verifier
trap 'printf "0\n" > /logs/verifier/reward.txt' ERR

git clone --quiet "$UPSTREAM_REPOSITORY" "$UPSTREAM_CHECKOUT"
git -C "$UPSTREAM_CHECKOUT" checkout --quiet "$SOURCE_COMMIT"

# Put the small Harbor adapter beside Convex's scripts. The adapter imports and
# calls runner/scorer.ts; it does not reimplement the benchmark's tests.
cp /tests/harborScoreProject.ts "$UPSTREAM_CHECKOUT/scripts/harborScoreProject.ts"

cd "$UPSTREAM_CHECKOUT"
bun install --frozen-lockfile
bun run scripts/harborScoreProject.ts \
  --eval "$EVAL_PATH" \
  --project /app \
  --summary "$SUMMARY_PATH" \
  --reward /logs/verifier/reward.txt
