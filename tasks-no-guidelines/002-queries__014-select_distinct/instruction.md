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
Create a backend that implements efficient distinct value selection using index range queries.

Create this structure in the `convex` directory:

1. Create a schema in `convex/schema.ts`:
```ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  users: defineTable({
    name: v.string(),
    age: v.number(),
  }).index("by_age", ["age"]),
});
```

2. Create a query function `getDistinctAges` in `convex/index.ts` that:
   - Takes no arguments
   - Uses the "by_age" index to efficiently find distinct age values
   - It should not read every record in the table, but instead skip ahead using the index.
   - Returns an array of numbers representing all distinct age values
   - Should be more efficient than fetching all records and using Set
   - The solution should scale well with large numbers of duplicate age values

The goal is to demonstrate how to efficiently implement DISTINCT-like functionality using Convex's index range queries rather than fetching all records into memory.

Only generate the `getDistinctAges` function in `convex/index.ts`. Do not generate any other functions.
Also generate the `package.json` and `convex/schema.ts` files.

```
