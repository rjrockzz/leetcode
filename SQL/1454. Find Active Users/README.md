# Active Users — Gaps & Islands SQL Problem
 
> This problem is a variation of the famous **Gaps and Islands** problem. The idea behind solving it is a core pattern that comes up frequently in SQL interviews.
 
---
 
## Table Schemas
 
### Accounts
 
| Column Name | Type    |
|-------------|---------|
| id          | int     |
| name        | varchar |
 
- `id` is the **primary key** for this table.
- Contains the account ID and username for each account.
 
---
 
### Logins
 
| Column Name | Type |
|-------------|------|
| id          | int  |
| login_date  | date |
 
- **No primary key** — may contain duplicates.
- Contains the account ID of the user who logged in and the login date.
- A user may log in **multiple times in a day**.
 
---
 
## Problem Statement
 
**Active users** are those who logged in to their accounts for **five or more consecutive days**.
 
Write an SQL query to find the `id` and `name` of all active users.
 
Return the result table **ordered by `id`**.
 
---
 
## Example
 
### Input
 
**Accounts table:**
 
| id | name     |
|----|----------|
| 1  | Winston  |
| 7  | Jonathan |
 
**Logins table:**
 
| id | login_date |
|----|------------|
| 7  | 2020-05-30 |
| 1  | 2020-05-30 |
| 7  | 2020-05-31 |
| 7  | 2020-06-01 |
| 7  | 2020-06-02 |
| 7  | 2020-06-02 |
| 7  | 2020-06-03 |
| 1  | 2020-06-07 |
| 7  | 2020-06-10 |
 
### Output
 
| id | name     |
|----|----------|
| 7  | Jonathan |
 
### Explanation
 
| User     | id | Distinct Login Days | Consecutive Days? | Active? |
|----------|----|---------------------|-------------------|---------|
| Winston  | 1  | 2                   | ❌                | ❌      |
| Jonathan | 7  | 6                   | ✅ (5 in a row)   | ✅      |
 
- **Winston** logged in on only 2 different days → not active.
- **Jonathan** logged in on 6 different days, **5 of which were consecutive** → active user.
 
