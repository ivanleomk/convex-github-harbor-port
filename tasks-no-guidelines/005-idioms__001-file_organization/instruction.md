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
Create a backend that implements organized CRUD operations for users and posts using this schema in `convex/schema.ts`:

```ts
users: {
  name: string
  email: string
}
posts: {
  userId: Id<"users">
  title: string
  content: string
}
```
Posts should have an index to look up posts by userId and user by email.

Each set of operations should be organized into a separate file.
For each table, export a public function called `get`, `create`, and `destroy`.
Only the `get` and `create` functions return anything (the full document, or the id of the created document).
You don't need to specify a returns validator for any function.

Error behavior for missing documents:
- For `users.get`, if the user does not exist, throw an error with the message "User not found".
- For `posts.get`, if the post does not exist, throw an error with the message "Post not found".
- `destroy` should not return a value.

Function argument specifications:

- `convex/users.ts`:
  - `get`: Takes arguments:  `{ id: Id<"users"> }`
  - `create`: Takes arguments:  `{ name: string, email: string }`
  - `destroy`: Takes arguments:  `{ id: Id<"users"> }`

- `convex/posts.ts`:
  - `get`: Takes arguments:  `{ id: Id<"posts"> }`
  - `create`: Takes arguments:  `{ userId: Id<"users">, title: string, content: string }`
  - `destroy`: Takes arguments:  `{ id: Id<"posts"> }`

```
