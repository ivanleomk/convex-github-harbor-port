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
Create a backend that finds teams with deleted admins using async iteration.

1. Create this schema in `convex/schema.ts`:
```ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  teams: defineTable({
    name: v.string(),
    adminId: v.id("users"),
  }),

  users: defineTable({
    name: v.string(),
    deleted: v.boolean(),
  }),
});
```

2. Create a query `getTeamsWithDeletedAdmins` in `convex/index.ts` that:
   - Takes no arguments
   - Uses an async iterator to loop through all teams, checking if the admin user is deleted
   - Returns a list of team IDs that match the criteria.
   - Should not include teams with non-existent admins

The implementation should focus on efficient database access patterns and proper
handling of large result sets through async iteration.

Only generate the `getTeamsWithDeletedAdmins` function in `convex/index.ts`. Do not generate any other functions.
Also generate the `package.json` and `convex/schema.ts` files.
```
