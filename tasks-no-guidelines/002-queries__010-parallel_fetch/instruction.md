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
Write this schema to `convex/schema.ts`:
```
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  // Users and their preferences
  users: defineTable({
    name: v.string(),
    email: v.string(),
  }).index("by_email", ["email"]),
  userPreferences: defineTable({
    userId: v.id("users"),
    theme: v.string(),
    notifications: v.boolean(),
  }).index("by_user", ["userId"]),

  // Posts and their reactions
  posts: defineTable({
    authorId: v.id("users"),
    title: v.string(),
    content: v.string(),
  }).index("by_author", ["authorId"]),
  reactions: defineTable({
    postId: v.id("posts"),
    userId: v.id("users"),
    type: v.union(v.literal("like"), v.literal("heart"), v.literal("celebrate")),
  }).index("by_post", ["postId"]),
});
```

Dont forget to write out the above schema.

Write a query named `getAuthorDashboard` in `convex/public.ts` that:
- Takes arguments:  `{ email: string }`, returning null if the user doesn't exist
- Throws an error if the user exists but its preferences are missing
- Returns an object with this structure:
```ts
{
  user: {
    name: string,
    email: string,
    theme: string,
    notifications: boolean,
  },
  posts: {
    title: string,
    reactionCounts: {
      like: number,
      heart: number,
      celebrate: number,
    },
  }[],
}
```
- Returns the user's 15 most recent posts (by creation time, descending)
- Demonstrates efficient parallel fetching:
  * Fetch preferences and posts in parallel
  * Kicks off reactions fetches as posts are streamed in
  * Queries reactions in parallel
```
