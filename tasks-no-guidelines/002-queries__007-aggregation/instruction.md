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
Write this schema to `convex/schema.ts`:
```
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  orders: defineTable({
    customerId: v.string(),
    productId: v.string(),
    quantity: v.number(),
    pricePerUnit: v.number(),
  }).index("by_customer", ["customerId"]),
});
```

Write a query named `getCustomerStats` in `convex/public.ts` that:
- Takes arguments:  `{ customerId: string }`
- Returns an object with:
  * totalOrders: number of orders
  * totalItems: sum of all quantities
  * totalSpent: sum of (quantity * pricePerUnit) for all orders
  * averageOrderValue: totalSpent / totalOrders
- All return value fields should be numbers
- You can assume that the number of orders for each customer is small.
- Handle the case where customer has no orders and returns zero for all fields.
- Format monetary values appropriately (2 decimal places)
```
