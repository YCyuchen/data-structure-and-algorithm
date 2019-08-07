#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/8/5 11:16 PM 
# @Author : Yuchen 
# @File : LRU_cache.py 
# @Software: PyCharm


class LRU_Cache():
    def __init__(self, capacity):
        self.num_entries = 0
        self.capacity = capacity
        self.cache_dic = {}
        self.least_visit_num = 0

    def set(self, key, value):
        if self.num_entries < self.capacity:
            self.cache_dic[key] = [value, 0]
            self.num_entries += 1

        else:
            for cache_key in self.cache_dic.keys():
                if self.least_visit_num == self.cache_dic[cache_key][1]:
                    del self.cache_dic[cache_key]
                    self.cache_dic[key] = value
                    break

    def get(self, key):
        for cache_key in self.cache_dic.keys():
            if key == cache_key:
                self.cache_dic[key][1] += 1
                if self.least_visit_num >= self.cache_dic[key][1]:
                    self.least_visit_num = self.cache_dic[key][1]
                return self.cache_dic[key][0]
        return -1


if __name__ == '__main__':
    our_cache = LRU_Cache(5)
    # edge case
    # Test1:  should returns -1
    print("Pass" if our_cache.get(1) == -1 else "Failed")

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    # Test2: should returns 1 and 2
    print("Pass" if our_cache.get(1) == 1 else "Failed")
    print("Pass" if our_cache.get(2) == 2 else "Failed")

    # Test3: should returns -1 because 9 is not present in the cache
    print("Pass" if our_cache.get(9) == -1 else "Failed")

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    # edge case
    # Test4: should returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    print("Pass" if our_cache.get(3) == -1 else "Failed")
