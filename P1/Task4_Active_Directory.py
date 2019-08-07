#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/8/2 10:01 AM 
# @Author : Yuchen 
# @File : Active_Directory.py 
# @Software: PyCharm


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    def traverse(node):
        current_user = node.get_users()
        if user in current_user:
            return True

        for sub_node in node.get_groups():
            if traverse(sub_node):
                return True

        return False

    return traverse(group)


if __name__ == '__main__':
    parent = Group("parent")
    parent.add_user("parent user")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)
    # edge case
    # Test1 user not exist in any group
    print("Pass" if is_user_in_group("xxx", parent) is False else "Failed")

    # Test2 user  exist in sub_child group
    print("Pass" if is_user_in_group("sub_child_user", parent) is True else "Failed")

    # edge case
    # Test3 upper group user not exist sub group
    print("Pass" if is_user_in_group("parent user", sub_child) is False else "Failed")
