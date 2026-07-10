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
Create a backend that demonstrates code reuse patterns in Convex by implementing functions to read users and posts.

Required files:
- convex/schema.ts
- convex/users.ts
- convex/posts.ts

Schema should define:
```ts
users: {
  name: string,
  email: string
}
posts: {
  userId: Id<"users">,
  content: string
}
```
With only an index on posts `by_user` and users `by_email`.

Implement these functions:

1. In convex/users.ts:
   - Create an internal query `getUserByEmail` that:
     - Takes arguments:  `{ email: string }`
     - Returns the user document or null

2. In convex/posts.ts:
   - Create an internal query `getPostsByUserId` that:
     - Takes arguments:  `{ userId: Id<"users"> }`
     - Returns array of post documents (empty array if none)
   - Create a query `getUserAndPosts` that:
     - Takes arguments:  `{ email: string }`
     - Fetches the user and their posts
     - Returns an object with the user and their posts
     - If the user does not exist for the given email, return `{ user: null, posts: [] }`

Don't specify returns validators for query/mutations.
Create any helper functions you need to avoid duplicating code.
DO NOT duplicate the code between `getUserByEmail`, `getPostsByUserId`, and `getUserAndPosts`.
The data fetched should be transactionally consistent.
Avoid creating subtransactions when possible, for efficiency.
```
