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
Create a cron job demo for Convex that demonstrates all available scheduling patterns.

Start by implementing a single `emptyAction` internal action in `crons.ts` that takes
in an optional `scheduleDescription` string, logs it to the console, and returns null.

Call this action every second using the `interval` syntax and omitting the argument.
Label this cron job "run every second".

Next, call this action every minute using the `interval` syntax.
Label this cron job "run every minute", and pass that in as an argument.

Next, call this action every hour using the `interval` syntax.
Label this cron job "run every hour", and pass that in as an argument.

Finally, call this action every month on the 11th day at 1pm UTC using the `cron` syntax.
Label this cron job "run every month on the 11th day at 1pm UTC", and pass that in as an argument.
```
