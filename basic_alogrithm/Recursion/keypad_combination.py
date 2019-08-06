#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/7/20 11:46 AM 
# @Author : Yuchen 
# @File : keypad_combination.py 
# @Software: PyCharm
"""
A keypad on a cellphone has alphabets for all numbers between 2 and 9.

You can make different combinations of alphabets by pressing the numbers.

For example, if you press 23, the following combinations are possible:

`ad, ae, af, bd, be, bf, cd, ce, cf`

Note that because 2 is pressed before 3, the first letter is always an alphabet on the number 2.
Likewise, if the user types 32, the order would be

`da, db, dc, ea, eb, ec, fa, fb, fc`


Given an integer `num`, find out all the possible strings that can be made using digits of input `num`.
Return these strings in a list. The order of strings in the list does not matter. However, as stated earlier,
the order of letters in a particular string matters.
"""


def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""


# Todo: implement keypad function
def keypad(num):
    if num <= 1:
        return [""]
    elif 1 < num <= 9:
        return list(get_characters(num))

    last_digit = num % 10  # 末位数
    key_pad = get_characters(last_digit)  # 末位数对应的键盘上的字母
    front_part = num // 10  # 除去末位数，之前的那几位数
    front_part_strlist = keypad(front_part)
    output = list()
    for char in front_part_strlist:
        for item in key_pad:
            new_item = char + item
            output.append(new_item)
    return output


# official version
def keypad(num):
    if num <= 1:
        return [""]
    elif 1 < num <= 9:
        return list(get_characters(num))

    last_digit = num % 10
    small_output = keypad(num // 10)
    keypad_string = get_characters(last_digit)
    output = list()
    for character in keypad_string:
        for item in small_output:
            new_item = item + character
            output.append(new_item)
    return output


if __name__ == '__main__':
    print(keypad(234))
