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
Create a backend that implements three HTTP endpoints with different methods.

Implement these HTTP handlers in `convex/http.ts`:

1. Create a GET endpoint `/getFoo` that:
2. Create a POST endpoint `/postBar` that:
3. Create a PUT endpoint `/putBaz` that:
4. Create a GET handler for all paths under `/api/*` that:

They should all return a JSON response: `{ ok: true }` and only accept the specified methods (reject other methods with 404). Non-existent paths should return 404.

Also create a query `getSiteURL` that takes no arguments (empty object `{}`) and returns `process.env.CONVEX_SITE_URL!`.
This will require the @types/node npm dev dependency.

Create only the `convex/http.ts` and `package.json` files. Do not generate any other files.
No schema is required since this demo doesn't use the database.

```
