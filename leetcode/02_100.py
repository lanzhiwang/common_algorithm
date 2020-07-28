#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
100. 相同的树
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false
"""

r"""
示例 1:

输入:        1
          /    \
         2      3
        / \    / \
       4   5  6   7

输入:        1
          /    \
         2      3
        / \    / \
       4   5  6   7

输出: true

is_same_tree(1, 1)
    is_same_tree(2, 2)  return True
    is_same_tree(3, 3)  return True
    return True

is_same_tree(2, 2)
    is_same_tree(4, 4)  return True
    is_same_tree(5, 5)  return True
    return True

is_same_tree(3, 3)
    is_same_tree(6, 6)  return True
    is_same_tree(7, 7)  return True
    return True

is_same_tree(4, 4)
    is_same_tree(None, None)  return True
    is_same_tree(None, None)  return True
    return True

is_same_tree(5, 5)
    is_same_tree(None, None)  return True
    is_same_tree(None, None)  return True
    return True

is_same_tree(6, 6)
    is_same_tree(None, None)  return True
    is_same_tree(None, None)  return True
    return True

is_same_tree(7, 7)
    is_same_tree(None, None)  return True
    is_same_tree(None, None)  return True
    return True

is_same_tree(None, None)
    return True

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_same_tree(p, q):
    if p is not None and q is not None:
        if p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right):
            return True
        else:
            return False
    elif p is None and q is None:
        return True
    else:
        return False


p = Node(1)
p.left = Node(2)
p.right = Node(3)

q = Node(1)
q.left = Node(2)
q.right = Node(4)

print(is_same_tree(p, q))
