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
Create a backend for a database CRUD system that manages location data.

Use the following schema at `convex/schema.ts`:
```ts
import { v } from "convex/values";
import { defineSchema, defineTable } from "convex/server";

export default defineSchema({
    locations: defineTable({
        name: v.string(),
        latitude: v.number(),
        longitude: v.number(),
    })
})
```

Implement the following functions in `convex/public.ts`:

1. Create a mutation `createLocation` that:
   - Takes arguments named `name` (string), `latitude` (number), and `longitude` (number)
   - Inserts a new location into the "locations" table
   - Returns the new location's ID

2. Create a query `readLocation` that:
   - Takes a location ID argument named `id`
   - Returns either null or the object containing the location's name, latitude, longitude, and its system fields
   - Use proper union typing for the return value

3. Create a mutation `updateLocation` that:
   - Takes arguments named `id`, `name`, `latitude`, and `longitude`
   - Replaces the existing location with new data
   - Throws an error if the location doesn't exist
   - Returns null

4. Create a mutation `patchLocation` that:
   - Takes arguments named `id` and `name`
   - Updates only the name field
   - Returns null

5. Create a mutation `deleteLocation` that:
   - Takes a location ID argument named `id`
   - Deletes the location from the database, throwing an error if it doesn't exist
   - Returns null
```
