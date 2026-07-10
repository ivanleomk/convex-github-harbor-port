#!/usr/bin/env bun
import { existsSync, mkdirSync, readdirSync, readFileSync, writeFileSync } from "fs";
import { join, relative, resolve } from "path";
import { convexScorer } from "../runner/scorer.js";
function value(flag: string): string {
  const i = process.argv.indexOf(flag);
  if (i < 0 || !process.argv[i + 1]) throw new Error("Missing argument " + flag);
  return process.argv[i + 1];
}
function files(project: string): Record<string, string> {
  const root = resolve(project), result: Record<string, string> = {};
  const skip = new Set(["node_modules", ".git", ".cache", ".next"]);
  function visit(dir: string): void {
    for (const entry of readdirSync(dir, {withFileTypes:true})) {
      if (skip.has(entry.name)) continue;
      const path = join(dir, entry.name);
      if (entry.isDirectory()) visit(path);
      else if (entry.isFile()) result[relative(root, path).replaceAll("\\", "/")] = readFileSync(path, "utf8");
    }
  }
  if (existsSync(root)) visit(root);
  return result;
}
const evalRel=value("--eval"), project=value("--project"), summary=value("--summary");
const parts=evalRel.split("/");
const scores=await convexScorer("/tmp/harbor-convex-score",readFileSync(join("evals",evalRel,"TASK.txt"),"utf8"),{},{model:"harbor-agent",category:parts[0],eval_name:parts[1]},files(project));
const reward=scores.length ? Math.min(...scores.map((s)=>s.score)) : 0;
mkdirSync(resolve(summary,".."),{recursive:true});
writeFileSync(summary,JSON.stringify({eval:evalRel,reward,scores},null,2));
