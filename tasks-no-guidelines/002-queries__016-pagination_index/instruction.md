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
Create a backend that paginates messages within a chat channel using an index.

Write this schema to `convex/schema.ts`:
```ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  messages: defineTable({
    channelId: v.string(),
    content: v.string(),
    author: v.string(),
  }).index("by_channel", ["channelId"]),
  channels: defineTable({
    name: v.string(),
  }),
});
```

Create a query function `paginateChannelMessages` in `convex/index.ts` that:
- Takes arguments:  `{ channelId: Id<"channels">, paginationOpts: { numItems: number, cursor: string | null } }`
- Uses the "by_channel" index to efficiently paginate messages in the given channel
- Orders messages in descending order (newest first)
- Returns the pagination result to be used with usePaginatedQuery, but don't provide a returns validator for it.

Only generate the `paginateChannelMessages` function in `convex/index.ts`. Do not generate any other functions.
Also generate the `package.json` and `convex/schema.ts` files.

The goal is to demonstrate efficient pagination over messages within a specific channel using an appropriate index.
```
