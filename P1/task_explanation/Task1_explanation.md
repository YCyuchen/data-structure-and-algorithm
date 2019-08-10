# Task1_explanation
## Problem description
For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.

## Solution
In this task, I use python OrderDic to implement. As python dic{} is defined as a kind of Hash map which means the time complexity for searching key is O(1). OrderDic has some special character(preserve the order in which key are inserted), more detail for OrderDic example can be found [here](https://www.geeksforgeeks.org/ordereddict-in-python/)

As for Hash-map, time for `.get()` method is constant, given a specific size of input. In our task, the size is 5. 
Time complexity: 
 **Big O equals to** $O(1)$
Space complexity: as the length of the OrderDic are enlarging when we use `set()` method repeatedly.
 **Big O equals to** $O(n)$ 

## My perspective
I should have completed this task by using a double linked list. But I got stuck and have no idea how to implement through linked list. Thus I implemented through dic{} first