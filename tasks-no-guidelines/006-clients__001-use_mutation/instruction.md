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
Create a backend that implements message sending functionality with a React frontend component.

Required files:
- convex/schema.ts
```ts
messages: {
  author: string,
  body: string,
}
```
No indexes are required.

- convex/messages.ts
```ts
export const sendMessage = mutation({
  args: {
    author: v.string(),
    body: v.string()
  },
  handler: async (ctx, args) => {
    return await ctx.db.insert("messages", {
      author: args.author,
      body: args.body
    });
  }
});
```

- src/App.tsx
  - Create a React component that:
    - Uses a form with two text inputs:
      - Author name input
      - Message body input
    - Sends a message using the sendMessage mutation when the form is submitted
    - Assume it's inside of a ConvexProvider already
    - Shows "Sending..." while the mutation is in progress

- package.json
  Include convex and React dependencies, including typescript types.

- tsconfig.json
  - Only include `src` in the `include` field.

Focus only on implementing the message sending functionality.
Don't implement any message listing or retrieval features.

```
