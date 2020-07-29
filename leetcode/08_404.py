#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
404. 左叶子之和
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7
   /     \
  2       8

在这个二叉树中，有三个左叶子，分别是 9 和 2，所以返回 11


sum_of_left_leaves(3, is_left=False)
    sum_of_left_leaves(9, is_left=True) return 9
    sum_of_left_leaves(20, is_left=False) return 2
    return 11

sum_of_left_leaves(9, is_left=True)
    return 9

sum_of_left_leaves(20, is_left=False)
    sum_of_left_leaves(15, is_left=True) return 2
    sum_of_left_leaves(7, is_left=False) return 0
    return 2

sum_of_left_leaves(15, is_left=True)
    sum_of_left_leaves(2, is_left=True) return 2
    return 2

sum_of_left_leaves(7, is_left=False)
    sum_of_left_leaves(8, is_left=False) return 0
    return 0

sum_of_left_leaves(2, is_left=True)
    return 2

sum_of_left_leaves(8, is_left=False)
    return 0

     1
    / \
   2   3
  / \
 4   5
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def sum_of_left_leaves(node, is_left):
    if node is None:
        return 0
    sum = 0
    if node.left is not None and node.right is not None:
        sum = sum_of_left_leaves(node.left, True) + sum_of_left_leaves(node.right, False)
    elif node.left is not None and node.right is None:
        sum = sum_of_left_leaves(node.left, True)
    elif node.left is None and node.right is not None:
        sum = sum_of_left_leaves(node.right, False)
    else:
        if is_left:
            sum = node.val
        else:
            sum = 0
    return sum
