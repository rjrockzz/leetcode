# Independent Column Ordering

## Problem Description

### Table Schema

**Table: `Data`**

| Column Name | Type |
|-------------|------|
| first_col   | int  |
| second_col  | int  |

> There is no primary key for this table — it may contain duplicates.

---

## Objective

Write an SQL query to **independently** sort both columns:

- `first_col` — sorted in **ascending** order
- `second_col` — sorted in **descending** order

> **Note:** The two columns are sorted independently of each other. There is no row-level relationship between the sorted `first_col` and `second_col` values.

---

## Example

### Input

**`Data` table:**

| first_col | second_col |
|-----------|------------|
| 4         | 2          |
| 2         | 3          |
| 3         | 1          |
| 1         | 4          |

### Output

| first_col | second_col |
|-----------|------------|
| 1         | 4          |
| 2         | 3          |
| 3         | 2          |
| 4         | 1          |

### Explanation

| Column       | Sort Order  | Result       |
|--------------|-------------|--------------|
| `first_col`  | ASC  (↑)    | 1 → 2 → 3 → 4 |
| `second_col` | DESC (↓)    | 4 → 3 → 2 → 1 |

Each column is sorted on its own — the position in one column does **not** determine the value in the other.

---
