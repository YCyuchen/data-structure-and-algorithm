#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/8/4 9:34 PM 
# @Author : Yuchen 
# @File : 1.py 
# @Software: PyCharm

def fun(x):
    if x > 0:
        x -= 1
        fun(x)
        print(x)
        x -= 1
        fun(x)


if __name__ == '__main__':
    fun(4)
