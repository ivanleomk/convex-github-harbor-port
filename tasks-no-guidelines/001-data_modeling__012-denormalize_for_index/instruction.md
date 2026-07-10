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
Create a backend that demonstrates denormalization for indexing.

Given this existing schema:
```ts
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
  }),
});
```

1. Generate a "convex/schema.ts" schema that allows sorting and paginating over the dogs table by the owner's age or the owner's ID (index `by_owner`).

2. Create these functions in `convex/index.ts`:

a. Create a mutation `createDog` that:
   - Takes arguments: `{ dogName: string, breed: string, ownerId: Id<"owners"> }`
   - Creates a new dog record
   - Returns the new dog's ID
   - Throws if owner not found

b. Create a mutation `updateOwnerAge` that:
   - Takes arguments: `{ ownerId: Id<"owners">, newAge: number }`
   - Updates the owner's age in the owners table and any associated dog records.
   - Returns null
   - Throws if owner not found

c. Create a query `getDogsByOwnerAge` that:
   - Takes arguments: `{ age: number }`
   - Returns an array of dog records { name, breed } that have an owner with the given age

The goal is to demonstrate how denormalization can be used to create efficient lookups on fields from related tables, while maintaining data consistency through update functions.

```
