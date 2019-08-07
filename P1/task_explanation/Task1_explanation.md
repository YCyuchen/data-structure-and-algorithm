# Task1_explanation
## Problem description
For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.

## Solution
In this task, I use python dic{} to implement. As python dic{} is defined as a kind of Hash map which means the time complexity for searching key is O(1), given a specific size of inpit. In our task, the size is 5.
As for Hash-map, time for `get()` and `set()` are both linear.
Time complexity:  **Big O equals to** $O(1)$
Space complexity  **Big O equals to** $O(1)$

## My perspective
I should have completed this task by using a double linked list. But I got stuck and have no idea how to implement through linked list. Thus I implemented through dic{} first