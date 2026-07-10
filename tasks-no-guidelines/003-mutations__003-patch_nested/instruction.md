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
Create a backend that tests patching a deep nested object in a document.

Start by creating this schema in `convex/schema.ts`:
```ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  documents: defineTable({
    metadata: v.object({
      title: v.string(),
      author: v.object({
        name: v.string(),
        contact: v.object({
          email: v.string(),
          phone: v.optional(v.string()),
        }),
      }),
      tags: v.array(v.string()),
    }),
    content: v.string(),
  }),
});
```

Implement the following functions in `convex/index.ts`:

1. Create a mutation `createDocument` that:
   - Takes a complete document object matching the schema as `{ metadata: ..., content: string }`
   - Inserts it into the database
   - Returns the new document's ID

2. Create a mutation `patchDocumentMetadata` that:
   - Takes an argument object `{ documentId: Id<"documents">, metadata: { title: string, author: { name: string, contact: { email: string, phone?: string | undefined } }, tags: string[] } }`
   - Replaces the entire metadata object while preserving content
   - Throws an error if document doesn't exist
   - Returns null (use `returns: v.null()` and `return null`)

3. Create a mutation `patchAuthorInfo` that:
   - Takes an argument object `{ documentId: Id<"documents">, author: { name: string, contact: { email: string, phone?: string | undefined } } }`
   - Updates only the metadata.author portion of the document
   - Throws an error if document doesn't exist
   - Returns null (use `returns: v.null()` and `return null`)

4. Create a query `getDocument` that:
   - Takes an argument object `{ documentId: Id<"documents"> }`
   - Returns the complete document with all nested fields
   - Returns null if document not found

These functions will demonstrate how to:
- Create documents with deeply nested objects
- Replace entire nested objects while preserving siblings
- Update specific nested objects within the document structure
- Retrieve and verify the nested object modifications

The schema and functions should maintain type safety throughout all operations with the nested object structure.

Only generate the `convex/schema.ts`, `convex/index.ts`, and `package.json` files. Do not generate any other files.

```
