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
Build a backend for tracking and counting support tickets per organization.

Write this schema to `convex/schema.ts`:
```ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  tickets: defineTable({
    orgId: v.string(),
    title: v.string(),
    status: v.string(),
  }).index("by_orgId", ["orgId"]),
});
```

Create these functions in `convex/index.ts`:
- A mutation `createTicket` that takes `{ orgId: string, title: string, status: string }` and inserts a new ticket
- A query `getTicketCount` that takes `{ orgId: string }` and returns the total number of tickets for that organization as a number

The tickets table is append-only and can accumulate millions of rows per organization over time. The `getTicketCount` query will be called on every page load, so it must remain efficient regardless of how many tickets exist.

You may modify the schema to add additional tables if needed for efficiency.

```
