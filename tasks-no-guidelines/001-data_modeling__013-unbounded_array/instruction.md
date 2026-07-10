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
Build a backend for a task management app with checklist support.

Design the schema in `convex/schema.ts` and implement the functions in `convex/index.ts`.

Requirements:
- A `tasks` table with fields: `title` (string) and `status` (string)
- Each task can have checklist items. A checklist item has `text` (string) and `completed` (boolean). Tasks can accumulate hundreds or thousands of checklist items over time.

Create these functions in `convex/index.ts`:
- A mutation `createTask` that takes `{ title: string, status: string }`, creates a task, and returns its ID directly
- A mutation `addChecklistItem` that takes `{ taskId: Id<"tasks">, text: string }` and adds a checklist item (defaulting `completed` to false)
- A mutation `toggleChecklistItem` that toggles the `completed` field of a checklist item
- A query `getChecklistItems` that takes a task ID and returns all checklist items for that task

```
