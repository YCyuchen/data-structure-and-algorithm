# Task6_explanation
## Problem description
Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.

## Solution
- union, For method `union(llist_1, llist_2)`
 ***The general idea is to append each node's value in two linked list to a list_array and set the unique, the convert the list_array to linked list.***
 firstly I traverse two linked list and append each element to the list() called `union_value_list`, Since the traverse time is linear, this will cost $O(n)$ 
 Then I use `set(union_value_list)` to get the unique element in the list, this will cost $O(nlogn)$ 
 Finally the unique element in union_value_list will be assigned to a linked list, this will cost $O(n)$
 
    Time complexity **Big O equals to** $O(nlogn)$
    Space complexity**Big O equals to** $O(n)$ 
    
-------
- intersection, For method intersection(llist_1, llist_2).   
***The general idea is to append and set the node's value in linked_list1 first. Then traverse linked_list2 and judge if the node value is in list1. If node value in linked_list2 also in linked_list1, append that value into a list called `intersection_list`. Finally convert the intersection_list to linked list.***
  - Traverse and set linked_list1 cost $O(n) + O(nlongn)->O(nlongn)$
  - Traverse linked_list2 for judge whether node value in linked_list2 is in linked_list1 cost, and then append value into intersection_list costs $O(n^2)+O(n)->O(n^2)$

Time complexity **Big O equals to** $O(nlongn)+O(n^2) ->O(n^2)$
Space complexity**Big O equals to** $O(n)$ (cost by appending value to list)

