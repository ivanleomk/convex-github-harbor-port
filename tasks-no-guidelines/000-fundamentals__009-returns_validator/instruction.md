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
Create a backend that demonstrates defining return data types for Convex queries.

Create this structure in the `convex` directory:

1. Create a schema in `convex/schema.ts`:
```ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  posts: defineTable({
    title: v.string(),
    content: v.string(),
    authorId: v.id("users"),
  }),
  users: defineTable({
    name: v.string(),
    email: v.string(),
  }),
});
```

2. Create three query functions in `convex/index.ts`:

a. Create a query `getPost` that:
   - Takes a post ID argument named `postId`
   - Returns the raw document from the "posts" table
   - If the post does not exist, throw an error with the message: "Post not found"

b. Create a query `getPostWithStatus` that:
   - Takes a post ID argument named `postId`
   - Returns a discriminated union type:
     ```ts
     { success: true, post: Doc<"posts"> } |
     { success: false, error: string }
     ```
   - Return `{ success: false, error: "Post not found" }` if the post does not exist
   - Return `{ success: false, error: "Post title cannot be empty" }` if the title is an empty string

c. Create a query `getPostWithAuthor` that:
   - Takes a post ID argument named `postId`
   - Returns an array that contains Doc<"users"> and Doc<"posts">, in this order: `[user, post]`
   - Throw an error with the message: "Post not found" if the post does not exist

Define a return validator for each of them.
```
