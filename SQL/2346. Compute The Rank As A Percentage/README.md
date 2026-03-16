## Problem Description
 
Given a `Students` table, write an SQL query that reports the **rank of each student in their department as a percentage**.
 
---
 
## Schema
 
**Table:** `Students`
 
| Column Name   | Type |
|---------------|------|
| student_id    | int  |
| department_id | int  |
| mark          | int  |
 
- `student_id` is the **primary key** of this table.
- Each row indicates a student's ID, the department they enrolled in, and their exam mark.
 
---
 
## Objective
 
Compute the rank percentage for each student using the formula:
 
$$\text{percentage} = \frac{(\text{student\_rank\_in\_department} - 1) \times 100}{(\text{number\_of\_students\_in\_department} - 1)}$$
 
### Rules
 
- `student_rank_in_department` is determined by **descending `mark`** — the student with the highest mark gets rank `1`.
- If two students have the **same mark**, they receive the **same rank** (i.e., use `DENSE_RANK`).
- `percentage` must be **rounded to 2 decimal places**.
- Return the result table in **any order**.
 
---
 
## Example
 
**Input:**
 
| student_id | department_id | mark |
|------------|---------------|------|
| 2          | 2             | 650  |
| 8          | 2             | 650  |
| 7          | 1             | 920  |
| 1          | 1             | 610  |
| 3          | 1             | 530  |
 
**Output:**
 
| student_id | department_id | percentage |
|------------|---------------|------------|
| 7          | 1             | 0.00       |
| 1          | 1             | 50.00      |
| 3          | 1             | 100.00     |
| 2          | 2             | 0.00       |
| 8          | 2             | 0.00       |
 
**Explanation:**
- **Department 1** has 3 students. Student `7` has the highest mark → rank 1 → `(1-1)*100/(3-1) = 0.00`. Student `1` → rank 2 → `(2-1)*100/(3-1) = 50.00`. Student `3` → rank 3 → `(3-1)*100/(3-1) = 100.00`.
- **Department 2** has 2 students. Both students `2` and `8` share the same mark → both rank 1 → `(1-1)*100/(2-1) = 0.00`.
