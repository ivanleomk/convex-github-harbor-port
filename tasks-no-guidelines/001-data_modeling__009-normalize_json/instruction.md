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
Create a backend that defines a normalized database schema for representing organizational data.
Only create "convex/schema.ts" (you may also include a minimal package.json so dependencies can install).
Normalize this JSON into three tables named exactly: "organizations", "employees", and "departments", using v.id relationships instead of inlined data:
```json
{
  "organizations": [
    {
      "name": "Acme, Inc.",
      "employees": [
        {
          "name": "Jason",
          "department": {
            "name": "Engineering",
            "manager": "Jane"
          },
          "age": 30,
          "email": "jason@example.com",
          "phone": "1234567890",
          "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "state": "CA",
            "zip": "12345"
          }
        },
        {
          "name": "Jane",
          "department": {
            "name": "Engineering",
            "manager": "Jane"
          },
          "email": "jane@example.com",
        }
      ]
    }
  ]
}
```
For employees, the name and email are required, but phone and address are optional.
For departments, the name is required, but manager is optional.

The "departments" table should be searchable by organization (index on organizationId).
The "employees" table should be searchable by email, department, and organization (indexes on email, departmentId, organizationId).
Do not make multi-column or any other additional indexes for now.

Indexes should be named like `by_<field_name>`, e.g. `by_department` for `departmentId` and multiple fields should be combined with an underscore, e.g. `by_department_organization`.
```
