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
Build a simple task management backend with a complete test suite using the `convex-test` library and Vitest.

Write this schema to `convex/schema.ts`:
```ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  tasks: defineTable({
    text: v.string(),
    isCompleted: v.boolean(),
  }),
});
```

Implement these functions in `convex/tasks.ts`:

1. A query `list` that:
   - Takes no arguments
   - Returns all tasks ordered by creation time (newest first)

2. A mutation `create` that:
   - Takes arguments: `{ text: string }`
   - Inserts a new task with `isCompleted: false`
   - Returns the new task's ID

3. A mutation `complete` that:
   - Takes arguments: `{ id: Id<"tasks"> }`
   - Sets `isCompleted` to `true` on the given task
   - Returns nothing

4. A mutation `remove` that:
   - Takes arguments: `{ id: Id<"tasks"> }`
   - Deletes the given task
   - Returns nothing

Write a test file `convex/tasks.test.ts` that tests these functions using the `convex-test` library. The tests must:
- Initialize `convexTest` with the schema
- Call the functions via `t.query` and `t.mutation` using the generated `api`
- Verify that `list` returns an empty array initially
- Verify that `create` adds a task and `list` returns it
- Verify that `complete` marks a task as completed
- Verify that `remove` deletes a task

Add a `vitest.config.ts` at the project root that configures the `edge-runtime` test environment (required by `convex-test`).

Your `package.json` must include `convex-test`, `vitest`, and `@edge-runtime/vm` as devDependencies along with `convex` as a regular dependency.

Create only these files:
- `package.json`
- `vitest.config.ts`
- `convex/schema.ts`
- `convex/tasks.ts`
- `convex/tasks.test.ts`

```
