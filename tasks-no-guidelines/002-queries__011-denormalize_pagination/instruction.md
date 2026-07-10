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
Create a backend that demonstrates pagination over a denormalized index.

Define the following schema in `convex/schema.ts`:
```ts
import { v } from "convex/values";
import { defineSchema, defineTable } from "convex/server";

export default defineSchema({
  // Main owners table
  owners: defineTable({
    name: v.string(),
    age: v.number(),
  }),

  // Dogs table with denormalized owner name for efficient lookups
  dogs: defineTable({
    name: v.string(),
    breed: v.string(),
    ownerId: v.id("owners"),
    ownerAge: v.number(),
  })
    .index("by_owner", ["ownerId"])
    .index("by_owner_age", ["ownerAge"]),
});
```

Create a query `paginateDogsByOwnerAge` in `convex/index.ts` that:
- Takes arguments:  `{ cursor: string | null, numItems: number }`
- Paginates over the dogs table by the owner's age using the index
- Returns an object with this structure:
```ts
{
  dogs: { name: string, breed: string }[],
  continueCursor: string,
}
```

The goal is to demonstrate how denormalization can be used to create efficient lookups on fields from related tables

Only generate the `paginateDogsByOwnerAge` function in `convex/index.ts`. Do not generate any other functions. Also generate the `package.json` and `convex/schema.ts` files.
```
