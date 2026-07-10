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
Create a backend for a basic file storage system that demonstrates all core file operations in Convex.

Assume the following schema, and output it to `convex/schema.ts`:
```ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
    files: defineTable({
        storageId: v.id("_storage"),
    }),
})
```

1. Create a mutation `generateUploadUrl`:
   - Takes no arguments
   - Returns a string URL for file upload

2. Create a mutation `finishUpload`:
   - Takes a storage ID argument named `storageId`
   - Inserts a new record in the "files" table with the storage ID
   - Returns null

3. Create a query `getFileUrl`:
   - Takes a file ID argument named `fileId`
   - Retrieves the file record from the database, throwing an error if not found
   - Gets the download URL for the storage ID associated with the file.
   - Throws an error if the storage entry is not found
   - Returns the URL as a string

4. Create a query `getFileMetadata`:
   - Takes a file ID argument named `fileId`
   - Retrieves the file record and returns the storage metadata using `ctx.db.system.get()`
   - Returns an object with: `_id`, `_creationTime`, `contentType` (optional string), `sha256`, and `size`
   - Throws an error if the file is not found

5. Create a mutation `deleteFile`:
   - Takes a file ID argument named `fileId`
   - Deletes both the storage object and database record
   - Throws an error if the file is not found

Implement ALL functions in `convex/index.ts`.
```
