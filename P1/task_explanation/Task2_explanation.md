# Task2_explanation
## Problem description
For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

# Solution
This is a very classic recursion problem.The structure of the *testdir* is similar to a tree. And I use Depth first search algorithm to solve the problem.
Time complexity:
Time  complexity is consumed by the DFS algorithm **Big O equals to** $O(n^2)$
Space complexity:
We use a list `out_list` to append the result  **Big O equals to** $O(n)$