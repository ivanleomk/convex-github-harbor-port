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
Create a backend that writes data and triggers an async HTTP request.

Create this schema in `convex/schema.ts`:
```ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  requests: defineTable({
    url: v.string(),
    status: v.union(v.literal("pending"), v.literal("completed")),
    requestedAt: v.number(),
    completedAt: v.optional(v.number()),
  }).index("by_url", ["url"]),
});
```

Implement these functions in `convex/index.ts`:

1. Create a mutation `initiateRequest` that:
   - Takes arguments:  `{ url: string }`
   - Checks if the URL already exists in the requests table
   - If it does, return the existing record ID
   - If it doesn't, inserts a pending record into requests table
   - Starts an asynchronous action to fetch the URL
   - Returns the ID of the new record

2. Create an internal action `performHttpbinFetch` that:
   - Takes arguments:  `{ url: string, requestId: Id<"requests"> }`
   - Makes a POST request to the URL
   - Updates the requests record by calling an internal mutation `updateRequest` via `ctx.runMutation(internal.index.updateRequest, ...)`
     - Define `updateRequest` as an `internalMutation` that takes arguments: `{ requestId: Id<"requests">, status: "completed", completedAt: number }`
     - It should set the status to "completed" and set `completedAt` to the provided timestamp
   - Returns nothing

Behavioral expectations:
- Multiple concurrent `initiateRequest` calls for the same URL must return the same existing request ID and not create duplicates.
- Requests that fail the POST should not transition to completed; the request should remain `pending` and `completedAt` should be unset.

The implementation should demonstrate:
- Proper scheduling of async work using actions
- Proper state management in the database
- Using mutations and actions together

Create only the `convex/schema.ts`, `convex/index.ts`, and `package.json` files. Do not generate any other files.

The only public function should be `initiateRequest`. Both `updateRequest` and `performHttpbinFetch` should be internal (using `internalMutation` and `internalAction` respectively). Do not export any other functions from `convex/index.ts`.
```
