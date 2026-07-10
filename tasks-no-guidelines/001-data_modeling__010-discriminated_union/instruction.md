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
Create a backend that demonstrates a schema using discriminated unions to model different types of notifications.

Create a schema in "convex/schema.ts" that models the following typescript types in a convex schema:
```ts
type MessageNotification = {
  kind: "message";
  senderId: string;
  messageText: string;
} | {
  kind: "friendRequest";
  requesterId: string;
} | {
  kind: "achievement";
  achievementName: string;
  points: number;
};
```

This should be the schema for the "notifications" table.

The schema should demonstrate:
1. A discriminated union using the `kind` field as the discriminator
2. Three different notification types with different fields:
   - Message notifications with sender and text
   - Friend request notifications with requester
   - Achievement notifications with name and points

No functions need to be implemented - this task is for the schema only.
```
