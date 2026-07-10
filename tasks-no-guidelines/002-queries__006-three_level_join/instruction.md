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
  // Organizations have many teams
  organizations: defineTable({
    name: v.string(),
  }),

  // Teams belong to organizations and have many members
  teams: defineTable({
    organizationId: v.id("organizations"),
    name: v.string(),
  }).index("by_org", ["organizationId"]),

  // Team members belong to teams
  teamMembers: defineTable({
    teamId: v.id("teams"),
    userId: v.id("users"),
    role: v.union(v.literal("member"), v.literal("admin")),
  }).index("by_team_role", ["teamId", "role"]),

  users: defineTable({
    name: v.string(),
    profileUrl: v.string(),
  }),
});
```

Write a query named `getProAdminsByOrg` in `convex/public.ts` that:
- Takes arguments:  `{ organizationId: Id<"organizations"> }`
- Returns the unique set of all admins within that organization as a record
  mapping `Id<"users">` to their profileUrl.
- This query should be efficient, assuming that there are many organizations,
  but it can also assume that the number of rows for the queried organization
  is small.
```
