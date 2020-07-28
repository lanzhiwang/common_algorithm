#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from queue import Queue

r"""
101. 对称二叉树
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3


但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

"""

r"""
    1
   / \
  2   2
 / \ / \
3  4 4  3

is_symmetric(2, 2)
    2 == 2
    3 == 3
    4 == 4
    is_symmetric(3, 3)
    is_symmetric(4, 4)

"""


class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)


def is_symmetric(p, q):
    if p is None and q is None:
        return True

    if p is not None and q is not None and p.val == q.val:
        return is_symmetric(p.left, q.right) and is_symmetric(p.right, q.left)

    return False



print(is_symmetric(root.left, root.right))


