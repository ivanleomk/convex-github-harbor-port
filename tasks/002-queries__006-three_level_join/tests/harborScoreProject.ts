#!/usr/bin/env bun
/**
 * Harbor adapter for Convex's official scorer.
 *
 * This file deliberately contains no benchmark-specific grading logic. It
 * collects the model's generated files, calls Convex's `convexScorer`, and
 * converts Convex's all-stages result into Harbor's numeric reward.
 *
 * Original scorer:
 * https://github.com/get-convex/convex-evals/blob/5c723ca8177c3ae167e505a95c755bd398f9dea2/runner/scorer.ts
 */
import {
  existsSync,
  mkdirSync,
  readdirSync,
  readFileSync,
  writeFileSync,
} from "node:fs";
import { join, relative, resolve } from "node:path";

import { convexScorer } from "../runner/scorer.js";

// Convex's backend helper asks GitHub's releases API which binary to use before
// checking its local cache. Harbor's image already contains the exact binary
// used by the native comparison run, so return matching release metadata for
// only that lookup and leave every other network request untouched.
// Original helper:
// https://github.com/get-convex/convex-evals/blob/5c723ca8177c3ae167e505a95c755bd398f9dea2/runner/convexBackend.ts
const releasesUrl =
  "https://api.github.com/repos/get-convex/convex-backend/releases?per_page=50";
const backendVersion = "precompiled-2026-07-10-f35f765";
const backendAsset = "convex-local-backend-x86_64-unknown-linux-gnu.zip";
const originalFetch = globalThis.fetch;
globalThis.fetch = ((input: string | URL | Request, init?: RequestInit) => {
  const url = typeof input === "string" ? input : input.toString();
  if (url === releasesUrl) {
    return Promise.resolve(new Response(JSON.stringify([{
      tag_name: backendVersion,
      assets: [{
        name: backendAsset,
        browser_download_url:
          `https://github.com/get-convex/convex-backend/releases/download/${backendVersion}/${backendAsset}`,
      }],
    }]), { status: 200, headers: { "content-type": "application/json" } }));
  }
  return originalFetch(input, init);
}) as typeof fetch;

function requiredArgument(name: string): string {
  const index = process.argv.indexOf(name);
  const value = process.argv[index + 1];
  if (index < 0 || !value) throw new Error(`Missing required argument: ${name}`);
  return value;
}

/** Read the model-authored project in the same file-map shape Convex expects. */
function readGeneratedFiles(projectDirectory: string): Record<string, string> {
  const root = resolve(projectDirectory);
  const generatedFiles: Record<string, string> = {};
  const ignoredDirectories = new Set(["node_modules", ".git", ".cache", ".next"]);

  function visit(directory: string): void {
    for (const entry of readdirSync(directory, { withFileTypes: true })) {
      if (ignoredDirectories.has(entry.name)) continue;
      const absolutePath = join(directory, entry.name);
      if (entry.isDirectory()) visit(absolutePath);
      if (entry.isFile()) {
        const projectPath = relative(root, absolutePath).replaceAll("\\", "/");
        generatedFiles[projectPath] = readFileSync(absolutePath, "utf8");
      }
    }
  }

  if (existsSync(root)) visit(root);
  return generatedFiles;
}

const evalPath = requiredArgument("--eval");
const projectDirectory = requiredArgument("--project");
const summaryPath = requiredArgument("--summary");
const rewardPath = requiredArgument("--reward");
const [category, evalName] = evalPath.split("/");

const taskText = readFileSync(join("evals", evalPath, "TASK.txt"), "utf8");
const scores = await convexScorer(
  "/tmp/harbor-convex-score",
  taskText,
  {},
  { model: "harbor-agent", category, eval_name: evalName },
  readGeneratedFiles(projectDirectory),
);

// Convex treats an eval as passed only when every scorer stage is exactly 1.
// A partial test score (for example 0.75) is still a benchmark failure.
const reward = scores.length > 0 && scores.every(({ score }) => score === 1) ? 1 : 0;
mkdirSync(resolve(summaryPath, ".."), { recursive: true });
writeFileSync(
  summaryPath,
  JSON.stringify({ eval: evalPath, reward, scores }, null, 2) + "\n",
);
writeFileSync(rewardPath, `${reward}\n`);

// The official scorer starts temporary local Convex backends. End this small
// adapter explicitly after the summary is durable instead of waiting for any
// provider handles to drain.
process.exit(0);
