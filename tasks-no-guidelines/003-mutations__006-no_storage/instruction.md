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
Create a backend that stores files and tracks their metadata in the database.

Create this schema in `convex/schema.ts`:
```ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  files: defineTable({
    storageId: v.id("_storage"),
    fileName: v.string(),
    size: v.number(),
  }),
});
```

Implement function `uploadFile` and `storeFileMetadata` in `convex/index.ts` that together:
- `uploadFile` takes `{ contents: string, fileName: string }`
- `storeFileMetadata` takes `{ storageId: Id<"_storage">, fileName: string, size: number }`
- Stores the file in Convex Storage
- Creates a database record with the file metadata including:
  - The storage ID from the upload
  - Original filename
  - File size in bytes
- Returns an object containing:
  - fileId: The database ID of the file record
  - storageId: The Convex Storage ID
  - url: The generated URL for accessing the file
- Define the typescript type for their `handler` function return value

Create only the `convex/schema.ts`, `convex/index.ts`, and `package.json` files. Do not generate any other files.

Do not export any functions from `convex/index.ts` other than `uploadFile` and `storeFileMetadata`.
```
