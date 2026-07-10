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
Create a backend that supports paginated retrieval of items and a React frontend component that paginates through the data in `App.tsx`.

Create these files:

1. `convex/schema.ts`
```ts
export default {
  items: {
    name: string,
    description: string,
  },
};
```
No indexes are required.

2. `convex/items.ts`
```ts
export const paginateItems = query({
  args: {
    paginationOpts: paginationOptsValidator,
  },
  handler: async (ctx, args) => {
    return ctx.db.query("items").order("desc").paginate(args.paginationOpts);
  },
});
```
- DO NOT add a `returns` validator.

Then for `src/App.tsx`, create a React component that lists the paginated items and has a load more button.
It should use the `usePaginatedQuery` hook.

Only create these files:

1. `src/App.tsx`
2. `package.json`
3. `tsconfig.json` that only includes the `src` directory
4. `convex/schema.ts`
5. `convex/items.ts`

```
