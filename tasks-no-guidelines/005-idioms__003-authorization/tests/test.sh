#!/bin/bash
set -uo pipefail
mkdir -p /logs/verifier
trap 'echo 0 > /logs/verifier/reward.txt' ERR
git clone --quiet https://github.com/get-convex/convex-evals.git /tmp/convex-evals
test "$(git -C /tmp/convex-evals remote get-url origin)" = "https://github.com/get-convex/convex-evals.git"
git -C /tmp/convex-evals checkout --quiet 5c723ca8177c3ae167e505a95c755bd398f9dea2
test "$(git -C /tmp/convex-evals rev-parse HEAD)" = "5c723ca8177c3ae167e505a95c755bd398f9dea2"
cp /tests/harborScoreProject.ts /tmp/convex-evals/scripts/harborScoreProject.ts
cd /tmp/convex-evals
bun install --frozen-lockfile
bun run scripts/harborScoreProject.ts --eval "005-idioms/003-authorization" --project /app --summary /logs/verifier/summary.json
node -e 'const fs=require("fs");const s=JSON.parse(fs.readFileSync("/logs/verifier/summary.json","utf8"));if(!Number.isFinite(s.reward)||s.reward<0||s.reward>1)process.exit(1);fs.writeFileSync("/logs/verifier/reward.txt",String(s.reward)+"\n");'
