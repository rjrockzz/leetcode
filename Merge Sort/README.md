### Merge Sort
Since this Sort has been a nightmare for a long time, we're gonna create a separate folder to understand all the details that there is to Merge Sort.

#### What it is?
- A Divide and Conquer Algorithm:
  - Breaks down problems into multiple subproblems recursively until they can be solved easily.
  - Solutions are then combined to solve the Original Problem.
- O (n * log(n))
  - Optimal Running time for Comparison Based Algorithms.
 
#### General Principle?   
- Split the Array in Half.
- Call Merge Sort on each half to Sort it recursively.
  - Will eventually become arrays of size one, which is easy since array of size 1 are always sorted!   
- Merge both Sorted Half into One Sorted Array.

![image](https://github.com/rjrockzz/leetcode/assets/24719007/f6fa4e57-297d-4b4f-aa92-5a3993fd9ef9)
