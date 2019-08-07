#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/7/28 3:30 PM 
# @Author : Yuchen 
# @File : File_Recursion.py 
# @Software: PyCharm
import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    out_list = list()
    if not os.path.exists(path):
        return []

    def traverse(path, out_list):
        for file in os.listdir(path):
            sub_path = os.path.join(path, file)
            if os.path.isdir(sub_path):
                traverse(sub_path, out_list)
            else:
                if sub_path.endswith(suffix):
                    out_list.append(sub_path)

    traverse(path, out_list)
    return out_list


if __name__ == '__main__':
    # edge case: the input path does not exist
    # Test1 should return []
    a = find_files(".c", "")
    print(a)

    # Test2 should return a list of path
    # ['/Users/yuchen/Downloads/testdir/subdir3/subsubdir1/b.c', '/Users/yuchen/Downloads/testdir/t1.c', ...]
    a = find_files(".c", "/Users/yuchen/Downloads/testdir")
    print(a)

    # edge case: the suffix is None
    # Test3 should all the file in the path
    a = find_files("", "/Users/yuchen/Downloads/testdir")
    print(a)
