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
Create a backend that demonstrates using the "node" runtime within a Convex action.

Implement this function in `convex/index.ts`:

1. Create an action `processWithNode` that:
   - Takes arguments:  `{ data: string }`
   - Uses Node.js 'crypto' module to generate a hash of the input
   - Uses Node.js 'path' module to manipulate file paths
   - Returns an object containing:
     - hash: The SHA-256 hash of the input string
     - normalizedPath: A normalized version of "/some/test/path"

Behavioral expectations:
- The hash must be a lowercase hexadecimal SHA-256 string of length 64.
- `normalizedPath` must equal "/some/test/path" consistently for all inputs.

This function should assume it needs libraries not available with the default Convex runtime.
This will require the @types/node npm dev dependency.
Create only the `convex/index.ts` and `package.json` files. Do not generate any other files.
No schema is required for this demo since it doesn't use the database.

Do not export any functions from `convex/index.ts` other than `processWithNode`.
```
