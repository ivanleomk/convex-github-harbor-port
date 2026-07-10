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
Build a small Convex contacts backend that uses the explicit table-name form for all ID-based database reads and writes.

Write this schema to `convex/schema.ts`:

```ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  contacts: defineTable({
    name: v.string(),
    email: v.string(),
    archived: v.boolean(),
  }),
});
```

Implement these functions in `convex/contacts.ts`:

1. A mutation `create` that:
   - Takes arguments `{ name: string, email: string }`
   - Inserts a contact with `archived: false`
   - Returns the new contact ID

2. A query `get` that:
   - Takes `{ id: Id<"contacts"> }`
   - Returns the contact document or `null`
   - Must call `ctx.db.get("contacts", id)`

3. A mutation `rename` that:
   - Takes `{ id: Id<"contacts">, name: string }`
   - Throws if the contact does not exist
   - Updates only the contact name
   - Must call `ctx.db.patch("contacts", id, ...)`

4. A mutation `replaceContact` that:
   - Takes `{ id: Id<"contacts">, name: string, email: string, archived: boolean }`
   - Throws if the contact does not exist
   - Fully replaces the contact document
   - Must call `ctx.db.replace("contacts", id, ...)`

5. A mutation `remove` that:
   - Takes `{ id: Id<"contacts"> }`
   - Deletes the contact if it exists
   - Returns `true` if a contact was deleted and `false` otherwise
   - Must call `ctx.db.delete("contacts", id)`

Important: Use the literal table name `"contacts"` as the first argument to every `ctx.db.get`, `ctx.db.patch`, `ctx.db.replace`, and `ctx.db.delete` call. Do not use legacy forms like `ctx.db.get(id)` or `ctx.db.patch(id, value)`.

Create only these files:
- `package.json`
- `convex/schema.ts`
- `convex/contacts.ts`

```
