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
Create a backend that demonstrates various ways to use literals and unions in a Convex schema.

Given this schema.ts file starter code:
```ts
import { defineSchema, defineTable } from "convex/server";

export default defineSchema({
  configurations: defineTable({
    // Add fields here
  })
});
```

Generate a "convex/schema.ts" file that adds the following fields to the `configurations` table:
- Simple literal
  - environment: "production" string literal
- Union of string literals
  - logLevel: "debug" | "info" | "warn" | "error"
- Union of number literals
  - priority: 1 | 2 | 3
- Union of number literal and boolean
  - enabled: 0 | 1 | false
- Union of different types
  - status: "active" | "inactive" | 0 | 1 | null
- Nested union structure
  - feature: { type: "basic" | "advanced", allowed: boolean }

The goal is to showcase different ways to use literals and unions in Convex schemas and how to properly type functions that interact with these complex types.

Only create the `package.json` and `convex/schema.ts` files. Do NOT create any functions.
```
