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
Create a backend that demonstrates different ways of handling optional and nullable fields in a Convex schema.

Create a schema in `convex/schema.ts` that has one table called `optionals`.
The `optionals` table should have three fields to demonstrate three different patterns for optional/nullable fields:
1. `nullable`: Allows either null or string values, but the field must always be present
2. `maybe_nullable`: Allows the field to be null or a string, but the field also might be missing / unset.
3. `maybe`: Allows the field to be either absent or contain a string, but cannot be explicitly null.

No additional functions need to be implemented - this task focuses purely on schema definition and type patterns.

Note that this schema will enforce these constraints:
- Records cannot be inserted without a `nullable` field (must be explicitly null or a string)
- `maybe_nullable` can be omitted, set to null, or set to a string
- `maybe` can be omitted or set to a string, but cannot be explicitly null
```
