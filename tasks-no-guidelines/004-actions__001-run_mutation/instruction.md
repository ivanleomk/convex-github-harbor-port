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
Create a backend that fetches external data and saves it to the database.

Create this schema in `convex/schema.ts`:
```ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  fetchResults: defineTable({
    url: v.string(),
    data: v.any(),
  }),
});
```

Implement these functions in `convex/index.ts`:

1. Create a mutation `saveFetchResult` that:
   - Takes arguments:  `{ url: string, data: any }`
   - Inserts a new record into the fetchResults table
   - Returns the ID of the new record

2. Create an action `fetchAndSave` that:
   - Takes arguments:  `{ url: string }`
   - Makes a fetch request to the provided URL
   - Parses the response as JSON
   - It's not important to handle errors here
   - Calls the saveFetchResult mutation with the url and parsed data
   - Returns the ID of the new record

The implementation should demonstrate:
- Proper use of Convex actions for external API calls
- Proper mutation usage from within an action

Create only the `convex/schema.ts`, `convex/index.ts`, and `package.json` files. Do not generate any other files.
Add return type annotations to the handler functions of `saveFetchResult` and `fetchAndSave` with `Promise<Id<"fetchResults">>`.

Do not export any functions from `convex/index.ts` other than `saveFetchResult` and `fetchAndSave`.
```
