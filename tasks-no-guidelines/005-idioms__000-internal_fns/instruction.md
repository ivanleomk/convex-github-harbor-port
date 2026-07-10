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
Create a backend that demonstrates different types of Convex functions with varying visibility and access patterns.

Implement these functions in `convex/index.ts`:

1. Create a query `getPublicStats` that:
   - Takes no arguments
   - Returns a static object containing { totalUsers: 100, version: "1.0.0" }
   - Should be accessible to client applications

2. Create a mutation `logClientEvent` that:
   - Takes arguments:  `{ eventName: string, data: any }`
   - Logs the event to the console
   - Returns the current timestamp
   - Should be accessible to client applications

3. Create an action `dailyCleanup` that:
   - Takes no arguments
   - Is meant to be run from the dashboard
   - Logs "Running daily cleanup" to console
   - Does nothing else
   - Returns nothing (use `return null`)
   - Should NOT be accessible to clients

4. Create a mutation `resetCounter` that:
   - Takes no arguments
   - Is meant to be called from CLI or scheduled asynchronously from another function
   - Does nothing but logs "Resetting counter" to console
   - Returns nothing (use `return null`)
   - Should NOT be accessible to clients

Function visibility and access expectations:
- `getPublicStats` and `logClientEvent` must be public and callable by regular clients.
- `dailyCleanup` (action) and `resetCounter` (mutation) must be internal-only and not callable by regular clients; they should be callable by admin clients.


Create only the `convex/index.ts` and `package.json` files. Do not generate any other files.
No schema is required since this demo doesn't use the database.
```
