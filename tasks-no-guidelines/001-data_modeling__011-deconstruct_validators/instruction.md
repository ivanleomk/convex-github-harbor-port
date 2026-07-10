Your task is to generate a Convex backend from a task description.

Output all files within an h1 Files section that has an h2 section for each necessary file for a Convex backend that implements the requested functionality.
For example, correct output looks like
# Files
## package.json
```
...
```
## tsconfig.json
```
...
```
## convex/schema.ts
```
...
```

# General Coding Standards
- Use 2 spaces for code indentation.
- Ensure your code is clear, efficient, concise, and innovative.
- Maintain a friendly and approachable tone in any comments or documentation.

# File Structure
- You can write to `package.json`, `tsconfig.json`, and any files within the `convex/` folder. Only write additional files (e.g. `src/`) if explicitly requested by the task description. Do NOT add extra files that were not asked for.
- Do NOT write to the `convex/_generated` folder. You can assume that `npx convex dev` will populate this folder.
- It's VERY IMPORTANT to output files to the correct paths, as specified in the task description.
- Always start with `package.json` and `tsconfig.json` files.
- Use Convex version "^1.41.0".
- Use Typescript version "^5.7.3".

Now, implement a Convex backend that satisfies the following task description:
```
Create a backend that demonstrates type reuse in a Convex schema. Place all code in `convex/schema.ts`.

Create a schema with exactly two tables that share a common "result" type:
```ts
type Result = {
  success: true;
  value: string;
} | {
  success: false;
  error: string;
}
```
Table 1 should be named "llm_calls" and store documents like:
```json
{
  "prompt": "What is the capital of France?",
  "result": {
    "success": true,
    "value": "Paris"
  }
}
```
Table 2 should be named "api_calls" and store documents like:
```json
{
  "url": "https://api.example.com/data",
  "result": {
    "success": true,
    "value": "foobar"
  }
}
```

Requirements:
   - Both tables must share the same "result" definition.
   - Export the shared value as "resultValidator" from the "convex/schema.ts" file.
   - All code must be in a single file: `convex/schema.ts`

The goal is to show how to extract common field definitions into reusable variables when defining Convex schemas, avoiding duplication of complex type definitions.

Only create the `package.json` and `convex/schema.ts` files. Do NOT create any functions.

```
