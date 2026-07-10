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
Create a backend that demonstrates sharing a pure TypeScript helper function between query and mutation functions.

Create this structure in the `convex` directory:

1. Create a schema in `convex/schema.ts`:
```ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  items: defineTable({
    name: v.string(),
    quantity: v.number(),
    lastModified: v.number(),
  }),
});
```

2. Create a helper function `getItemData` in `convex/index.ts` that takes an item ID and fetches it from the database, returning a document like:

```ts
{
  name: item.name,
  quantity: item.quantity,
  lastModified: new Date(item.lastModified).toISOString(),
}
```
Return null if item not found, otherwise returns the formatted data

3. Create more functions in `convex/index.ts`:

a. Create a query `getItem` that:
   - Takes an item ID argument with the name "itemId"
   - Uses the shared helper function to retrieve and transform the item from the database
   - Throws an error if item not found

b. Create a mutation `updateItem` that:
   - Takes an item ID argument with the name "itemId" and a new quantity argument with the name "quantity"
   - Updates the item's quantity and lastModified timestamp
   - Retrieves the item via the shared helper function
   - Throws an error if item not found
   - Returns the updated item

Both functions should use the same `getItemData` helper function. Do not create any more functions than the specified ones.

The goal is to demonstrate how pure TypeScript helper functions can be shared between different Convex functions while maintaining type safety and consistent data formatting.
```
