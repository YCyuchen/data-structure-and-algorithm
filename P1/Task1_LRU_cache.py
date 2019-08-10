#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/8/5 11:16 PM 
# @Author : Yuchen 
# @File : LRU_cache.py 
# @Software: PyCharm

from collections import OrderedDict


# OrderDict is underlying Doubly Linked List implementation for keeping the order.

class LRU_Cache():
    def __init__(self, capacity):
        self.num_entries = 0
        self.capacity = capacity
        self.cache_dic = OrderedDict()

    def set(self, key, value):
        if self.capacity > 0:
            if key in self.cache_dic:
                self.cache_dic.pop(key)
            else:
                if len(self.cache_dic) == self.capacity:
                    self.cache_dic.popitem(last=False)

        else:
            return ("Can't perform operations on 0 capacity cache")

        self.cache_dic[key] = value

    def get(self, key):
        if key not in self.cache_dic:
            return -1
        value = self.cache_dic[key]

        # since the value is in the cache, move to the last
        self.cache_dic.pop(key)
        self.cache_dic[key] = value
        return value


if __name__ == '__main__':
    # Test case1
    our_cache = LRU_Cache(5)
    # should returns -1
    print("Test1:" + "Pass" if our_cache.get(1) == -1 else "Failed")

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    # should returns 1 and 2
    print("Test1:" + "Pass" if our_cache.get(1) == 1 else "Failed")
    print("Test1:" + "Pass" if our_cache.get(2) == 2 else "Failed")

    # Test3: should returns -1 because 9 is not present in the cache
    print("Test1:" + "Pass" if our_cache.get(9) == -1 else "Failed")

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    # should returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    print("Test1:" + "Pass" if our_cache.get(3) == -1 else "Failed")

    # Test case 2
    our_cache = LRU_Cache(0)
    # should return Can't perform operations on 0 capacity cache
    print("\nTest2: " + our_cache.set(1, 1))

    # Test case 3
    our_cache = LRU_Cache(2)
    print("\nTest3:" + "Pass" if our_cache.get(1) == -1 else "Failed")

