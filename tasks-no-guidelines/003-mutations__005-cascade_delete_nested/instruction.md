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
Create a backend that safely deletes a user and all associated data across multiple tables.

Create this schema in `convex/schema.ts`:
```ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  users: defineTable({
    name: v.string(),
    email: v.string(),
  }).index("by_email", ["email"]),

  posts: defineTable({
    authorId: v.id("users"),
    title: v.string(),
    content: v.string(),
  }).index("by_author", ["authorId"]),

  comments: defineTable({
    authorId: v.id("users"),
    postId: v.id("posts"),
    content: v.string(),
  })
    .index("by_author", ["authorId"])
    .index("by_post", ["postId"]),

  likes: defineTable({
    userId: v.id("users"),
    postId: v.id("posts"),
  })
    .index("by_user", ["userId"])
    .index("by_post", ["postId"]),
});
```

Implement the following functions in `convex/index.ts`:

2. Create a mutation `deleteUser` that takes `{ userId: Id<"users"> }` and deletes all dependent records.
   Both records that directly depend on the user, records that depend on those records, etc.
   Return nothing.

The implementation should demonstrate:
- Efficient parallel operations where possible
- Proper error handling
- Transaction safety

Create only the `convex/schema.ts`, `convex/index.ts`, and `package.json` files. Do not generate any other files.

Do not export any functions from `convex/index.ts` other than `deleteUser`.

```
