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
Create a backend that implements message listing functionality with a React frontend component.

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
export const getAllMessages = query({
  args: {},
  handler: async (ctx) => {
    return ctx.db.query("messages").order("desc").collect();
  }
});
```

- src/App.tsx
  - Create a React component that:
    - Uses a hook to fetch messages from `getAllMessages`
    - Handles loading state by showing "Loading..."
    - Handles empty state by showing "No messages yet"
    - Renders messages in a `<ul>` list with "author: body" in `<li>` elements.

- package.json
  Include convex and React dependencies, including typescript types.

- tsconfig.json
  - Only include `src` in the `include` field.

Don't add any message creation functionality - focus only on listing existing messages.

```
