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
Create a backend that conditionally fetches and caches external data.

Create this schema in `convex/schema.ts`:
```ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  fetchRequests: defineTable({
    url: v.string(),
    data: v.any(),
  }).index("by_url", ["url"]),
});
```

Implement these functions in `convex/index.ts`:

1. Create a **public query** `getFetchResult` that:
   - Takes arguments:  `{ url: string }`
   - Uses the "by_url" index to look up any existing fetch result
   - Returns the ID of the record if found, null if not found

2. Create a **public mutation** `saveFetchResult` that:
   - Takes arguments:  `{ url: string, data: any }`
   - Inserts a new record, or updates an existing record if the URL already exists (maintaining only one record per URL)
   - Has the handler return type of `Promise<Id<"fetchRequests">>`
   - Returns the ID of the new record

3. Create an action `fetchIfNeeded` that uses the query and mutation to:
   - Takes arguments:  `{ url: string }`
   - Makes a fetch request to the URL, if the result is not already cached in fetchResults.
   - If it isn't cached, write the JSON response to the fetchResults table
   - Has the handler return type of `Promise<Id<"fetchRequests">>`
   - Returns the newly created record ID

The implementation should demonstrate:
- Proper use of indexes for efficient lookups
- Coordination between query, mutation and action
- Proper type handling for external data

Create only the `convex/schema.ts`, `convex/index.ts`, and `package.json` files. Do not generate any other files.

Do not export any functions from `convex/index.ts` other than `getFetchResult`, `saveFetchResult`, and `fetchIfNeeded`.
```
