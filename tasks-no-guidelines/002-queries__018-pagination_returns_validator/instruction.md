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
Create a backend that implements paginated queries with proper type safety using pagination returns validators.

Required files:

`convex/schema.ts`:
```ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  posts: defineTable({
    title: v.string(),
    content: v.string(),
  }),
});
```

Create a query function `paginatePosts` in `convex/index.ts` that:
- Takes arguments:  `{ paginationOpts: { numItems: number, cursor: string | null } }`
- Paginates posts in the default order
- Must include a proper returns validator that accurately types the pagination result
- Should be compatible with the usePaginatedQuery hook

Files to create:
- `convex/schema.ts` with the schema above
- `convex/index.ts` with the paginated query including returns validator
- `package.json` with necessary dependencies

The focus should be on implementing correct typing and runtime validation for the pagination result structure while maintaining efficient database access patterns.
```
