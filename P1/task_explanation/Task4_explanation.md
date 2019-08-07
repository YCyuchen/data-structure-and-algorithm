# Task4_explanation
## Problem description
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.

## Solution
Depth First search is used in this task. The problem can be regarded as search in a binary tree. Where method `add_group(self, group)` is the left child and method `add_user(self, user)` is the right child.
Time complexity **Big O equals to** $O(n^2)$
Space complexity **Big O equals to** $O(n^2)$