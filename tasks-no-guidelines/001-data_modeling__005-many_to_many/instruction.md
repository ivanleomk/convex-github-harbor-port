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
Create a backend for a course enrollment system where:

1. Students have a name and email
2. Students can be enrolled in multiple courses
3. Courses can have multiple students enrolled
4. Course have the following metadata:
   - name (string)
   - code (string)
   - description (string)
5. We need to track both:
   - All courses a student is enrolled in
   - All students enrolled in a course
6. For each enrollment, we also want to track:
   - The enrollment date, represented as a number (Unix timestamp)
   - The student's grade (if completed), represented as an optional string

Requirements:
- Design the schema to efficiently support these queries with indexes:
  - List a subset of courses a student is enrolled in based on a filter condition (for example: What are the courses that student A is enrolled in that aren't class A or class B?)
  - List a subset students enrolled in a course based on a filter condition (for example: Who are the students in class A that aren't student A or student B?)

Only create the `package.json` and `convex/schema.ts` files. Do NOT create any functions.
```
