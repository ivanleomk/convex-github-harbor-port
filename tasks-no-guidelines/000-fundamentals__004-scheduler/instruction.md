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
Create a demo that demonstrates all of the ways to interact with the scheduler in Convex.

Start by implementing two internal logging functions in `index.ts`:
- An internal mutation `logMutation` that takes a message string argument named "message" and logs it
- An internal action `logAction` that takes a message string argument named "message" and logs it

Then create two public caller functions in `index.ts` to demonstrate scheduler functionality:

1. Create a mutation called `callerMutation` that demonstrates:
   - Takes no arguments
   - Scheduling the logging mutation to run immediately (with runAfter and 0 delay)
   - Canceling a scheduled task using the returned scheduler ID
   - Scheduling the logging action to run 10 seconds in the future using runAt
   - Returning null.

2. Create an action called `callerAction` that demonstrates:
   - Takes no arguments
   - Scheduling the logging action to run after a random delay between 0-10 seconds
   - Scheduling the logging mutation to run immediately and then canceling it
   - Returning null.

All scheduled tasks should call the logging functions with the message "Hello, world!".
```
