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
Build a backend for tracking user online status. Users send periodic heartbeat pings while they are active, and clients query which users are currently online.

The users table is already defined:
```ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  users: defineTable({
    name: v.string(),
    email: v.string(),
  }).index("by_email", ["email"]),
});
```

You may add fields, tables, and indexes as needed. Do not remove or rename the existing users table fields or its by_email index.

Create these functions in `convex/index.ts`:
- A mutation `recordHeartbeat` that takes `{ userId: Id<"users">, nowMs: number }` and records that the user is active at time `nowMs`.
- A query `listOnlineUsers` that takes `{ activeWithinMs: number, nowMs: number }` and returns all users whose last heartbeat is within `nowMs - activeWithinMs`. Return shape: array of objects with `{ userId, name, email, lastHeartbeatMs }`.

Requirements:
- Return an empty array from `listOnlineUsers` when no users are online.
- Calling `recordHeartbeat` multiple times for the same user must not create duplicate records.

Generate only:
- `package.json`
- `convex/schema.ts`
- `convex/index.ts`

```
