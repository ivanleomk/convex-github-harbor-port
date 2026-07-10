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
Create a demo that demonstrates all the ways to call functions from other functions in Convex.

Start by implementing three internal callee functions in `convex/index.ts`:
- An internal query `calleeQuery` that takes numbers named "x" and "y" and returns their sum
- An internal mutation `calleeMutation` that takes numbers named "x" and "y" and returns their difference
- An internal action `calleeAction` that takes numbers named "x" and "y" and returns their product

Then create two caller functions in `convex/index.ts`:

1. Create a mutation called `callerMutation` that demonstrates:
   - Takes no arguments
   - Calling the internal query with x=1 and y=2
   - Using the result to call the internal mutation with y=2 (keep the parameter names "x" and "y")
   - Return the final result

2. Create an action called `callerAction` that demonstrates:
   - Takes no arguments
   - Calling the internal query with x=1 and y=2
   - Using the result to call the internal mutation with y=2
   - Using that result to call the internal action with y=2
   - Return the final result
```
