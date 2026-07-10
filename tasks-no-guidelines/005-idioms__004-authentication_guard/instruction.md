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
Build a backend for a project export feature where only authenticated users can request exports.

Write this schema to `convex/schema.ts`:
```ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  users: defineTable({
    tokenIdentifier: v.string(),
    email: v.string(),
    name: v.string(),
  }).index("by_tokenIdentifier", ["tokenIdentifier"]),
  exportRequests: defineTable({
    projectName: v.string(),
    requestedByUserId: v.id("users"),
    destinationEmail: v.string(),
    status: v.union(v.literal("queued"), v.literal("sent"), v.literal("failed")),
  }).index("by_requestedByUserId", ["requestedByUserId"]),
});
```

Auth is already configured. Do not create `convex/auth.config.ts`.

Create this mutation in `convex/exports.ts`:
- `requestExport` with args `{ projectName: string, destinationEmail: string }`
- It inserts one row into `exportRequests` with:
  - `projectName` from args
  - `destinationEmail` from args
  - `requestedByUserId` for the caller's user record
  - `status: "queued"`
- Return the inserted `Id<"exportRequests">`.

Only create the files required for this feature.

```
