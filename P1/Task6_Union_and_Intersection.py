#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/7/31 11:44 PM 
# @Author : Yuchen 
# @File : Union_and_Intersection.py 
# @Software: PyCharm
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    # assert two linkedlist are not empty
    union_value_list = list()
    union_linkedlist = LinkedList()
    node1, node2 = llist_1.head, llist_2.head
    # append the node value to a list
    while node1:
        union_value_list.append(node1.value)
        node1 = node1.next

    while node2:
        union_value_list.append(node2.value)
        node2 = node2.next

    union_value_list = set(union_value_list)
    for i in union_value_list:
        union_linkedlist.append(i)

    return union_linkedlist


def intersection(llist_1, llist_2):
    # Your Solution Here
    l1_value_list = list()
    intersection_list = list()
    intersection_linkedlist = LinkedList()
    node1, node2 = llist_1.head, llist_2.head
    # append the node value to a list
    while node1:
        l1_value_list.append(node1.value)
        node1 = node1.next
    l1_value_list = list(set(l1_value_list))
    # judge if node2 in node1
    while node2:
        if node2.value in l1_value_list:
            intersection_list.append(node2.value)
        node2 = node2.next
    intersection_list = set(intersection_list)
    for i in intersection_list:
        intersection_linkedlist.append(i)
    return intersection_linkedlist


if __name__ == '__main__':
    # Test case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [1, 2, 3, 4, 5]
    element_2 = [5, 6, 7, 8, 9]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)
    print("\ntest 1")
    print("union", union(linked_list_1, linked_list_2))
    print("intersection", intersection(linked_list_1, linked_list_2))

    # edge case
    # Test case 2 both should be empty
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = []
    element_2 = []

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)
    print("\ntest 2")
    print("union", union(linked_list_3, linked_list_4))
    print("intersection", intersection(linked_list_3, linked_list_4))

    # edge case
    # Task 3: union should be [1,3]  intersection should be empty
    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    element_1 = [3]
    element_2 = [1]

    for i in element_1:
        linked_list_5.append(i)

    for i in element_2:
        linked_list_6.append(i)
    print("\ntest 3")
    print("union", union(linked_list_5, linked_list_6))
    print("intersection", intersection(linked_list_5, linked_list_6))
