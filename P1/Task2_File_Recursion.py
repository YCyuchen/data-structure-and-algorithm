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
    a = find_files(".c", "/Users/yuchen/Downloads/testdir")
    print(a)
