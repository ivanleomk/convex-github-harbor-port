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
Create a backend that joins user data while paginating messages.

Required files:

1. `convex/schema.ts`:
```ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  messages: defineTable({
    authorId: v.id("users"),
    content: v.string(),
  }),

  users: defineTable({
    name: v.string(),
  }),
});
```

2. Create a query function `paginateMessagesWithAuthors` in `convex/index.ts` that:
   - Takes arguments:  `{ paginationOpts: { numItems: number, cursor: string | null } }`
   - Paginates messages in descending order (newest first)
   - Adds the author's name to each message as an `author` field (string)
   - Returns the pagination result to be used with usePaginatedQuery.
   - Should be compatible with usePaginatedQuery hook
   - Don't provide a returns validator for this example
   - Throw an error if the author is not found

Each message in the returned page should have this structure:
```ts
{
  _id: Id<"messages">,
  _creationTime: number,
  authorId: Id<"users">,
  content: string,
  author: string,  // The author's name
}
```

Only implement the `paginateMessagesWithAuthors` function in `convex/index.ts`. Do not generate any other functions.

The goal is to demonstrate efficient pagination while joining related data from another table.

Files to create:
- `convex/schema.ts` with the schema above
- `convex/index.ts` with the pagination query
- `package.json` with necessary dependencies
```
