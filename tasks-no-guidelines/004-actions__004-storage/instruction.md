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
Create a backend that interacts with Convex file storage to write and read text files.

Implement these functions in `convex/index.ts`:

1. Create an action `writeTextToStorage` that:
   - Takes arguments:  `{ text: string }`
   - Uploads the data to Convex storage
   - Returns an object containing:
     - storageId: The storage ID
     - url: The public URL of the stored file

2. Create an action `readTextFromStorage` that:
   - Takes arguments:  `{ storageId: Id<"_storage"> }`
   - Retrieves the data from storage and returns it as a string
   - If the storageId is invalid or the file doesn't exist, throw an error

The implementation should demonstrate:
- Proper use of Convex storage APIs
- Correct text encoding/decoding

Create only the `convex/index.ts` and `package.json` files. Do not generate any other files.
No schema is required since this demo only uses file storage.

Do not export any functions from `convex/index.ts` other than `writeTextToStorage` and `readTextFromStorage`.
```
