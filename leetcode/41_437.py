#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
437. 路径总和 III
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
4  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11

path_sum(10, 8)
    path_sum(5, -2)
    path_sum(5, 8)
    path_sum(-3, -2)
    path_sum(-3, 8)

path_sum(5, -2)
    path_sum(3, -7)
    path_sum(3, -2)
    path_sum(2, -7)
    path_sum(2, -2)

path_sum(5, 8)
    path_sum(3, 3)
    path_sum(3, 8)
    path_sum(2, 3)
    path_sum(2, 8)

path_sum(-3, -2)
    path_sum(None, -5)
    path_sum(None, -2)
    path_sum(11, -5)
    path_sum(11, -2)

path_sum(-3, 8)
    path_sum(None, 11)
    path_sum(None, 8)
    path_sum(11, 11)
    path_sum(11, 8)












path_sum(3, -7)
    path_sum(4, -10)
    path_sum(4, -7)
    path_sum(-2, -10)
    path_sum(-2, -7)

path_sum(3, -2)
    path_sum(4, -5)
    path_sum(4, -2)
    path_sum(-2, -5)
    path_sum(-2, -2)

path_sum(2, -7)
    path_sum(None, -9)
    path_sum(None, -7)
    path_sum(1, -9)
    path_sum(1, -7)

path_sum(2, -2)
    path_sum(None, -4)
    path_sum(None, -2)
    path_sum(1, -4)
    path_sum(1, -2)

path_sum(3, 3)
    path_sum(4, 0)
    path_sum(4, 3)
    path_sum(-2, 0)
    path_sum(-2, 3)

path_sum(3, 8)
    path_sum(4, 5)
    path_sum(4, 8)
    path_sum(-2, 5)
    path_sum(-2, 8)

path_sum(2, 3)
    path_sum(None, 1)
    path_sum(None, 3)
    path_sum(1, 1)
    path_sum(1, 3)

path_sum(2, 8)
    path_sum(None, 6)
    path_sum(None, 8)
    path_sum(1, 6)
    path_sum(1, 8)

path_sum(None, -5)
path_sum(None, -2)
path_sum(11, -5)
    path_sum(None, -16)
    path_sum(None, -5)
    path_sum(None, -16)
    path_sum(None, -5)

path_sum(11, -2)
    path_sum(None, -13)
    path_sum(None, -2)
    path_sum(None, -13)
    path_sum(None, -2)

path_sum(None, 11)
path_sum(None, 8)
path_sum(11, 11)
    path_sum(None, 0)
    path_sum(None, 11)
    path_sum(None, 0)
    path_sum(None, 11)

path_sum(11, 8)
    path_sum(None, -3)
    path_sum(None, 8)
    path_sum(None, -3)
    path_sum(None, 8)
















path_sum(4, -10)
    path_sum(None, -16)
    path_sum(None, -5)
    path_sum(None, -16)
    path_sum(None, -5)

path_sum(4, -7)
    path_sum(None, -16)
    path_sum(None, -5)
    path_sum(None, -16)
    path_sum(None, -5)

path_sum(-2, -10)
    path_sum(None, -16)
    path_sum(None, -5)
    path_sum(None, -16)
    path_sum(None, -5)

path_sum(-2, -7)
    path_sum(None, -16)
    path_sum(None, -5)
    path_sum(None, -16)
    path_sum(None, -5)


path_sum(4, -5)
    path_sum(None, -16)
    path_sum(None, -5)
    path_sum(None, -16)
    path_sum(None, -5)

path_sum(4, -2)
    path_sum(None, -16)
    path_sum(None, -5)
    path_sum(None, -16)
    path_sum(None, -5)

path_sum(-2, -5)
    path_sum(None, -16)
    path_sum(None, -5)
    path_sum(None, -16)
    path_sum(None, -5)

path_sum(-2, -2)
    path_sum(None, -16)
    path_sum(None, -5)
    path_sum(None, -16)
    path_sum(None, -5)

path_sum(None, -9)
path_sum(None, -7)
path_sum(1, -9)
    path_sum(None, -16)
    path_sum(None, -5)
    path_sum(None, -16)
    path_sum(None, -5)

path_sum(1, -7)
    path_sum(None, -16)
    path_sum(None, -5)
    path_sum(None, -16)
    path_sum(None, -5)

path_sum(None, -4)
path_sum(None, -2)
path_sum(1, -4)
    path_sum(None, -16)
    path_sum(None, -5)
    path_sum(None, -16)
    path_sum(None, -5)

path_sum(1, -2)
    path_sum(None, -16)
    path_sum(None, -5)
    path_sum(None, -16)
    path_sum(None, -5)

path_sum(4, 0)
    path_sum(None, -16)
    path_sum(None, -5)
    path_sum(None, -16)
    path_sum(None, -5)

path_sum(4, 3)
    path_sum(None, -16)
    path_sum(None, -5)
    path_sum(None, -16)
    path_sum(None, -5)

path_sum(-2, 0)
    path_sum(None, -16)
    path_sum(None, -5)
    path_sum(None, -16)
    path_sum(None, -5)

path_sum(-2, 3)
    path_sum(None, -16)
    path_sum(None, -5)
    path_sum(None, -16)
    path_sum(None, -5)

path_sum(4, 5)
    path_sum(None, -16)
    path_sum(None, -5)
    path_sum(None, -16)
    path_sum(None, -5)

path_sum(4, 8)
    path_sum(None, -16)
    path_sum(None, -5)
    path_sum(None, -16)
    path_sum(None, -5)

path_sum(-2, 5)
    path_sum(None, -16)
    path_sum(None, -5)
    path_sum(None, -16)
    path_sum(None, -5)

path_sum(-2, 8)
    path_sum(None, -16)
    path_sum(None, -5)
    path_sum(None, -16)
    path_sum(None, -5)

path_sum(None, 1)
path_sum(None, 3)
path_sum(1, 1)
    path_sum(None, -16)
    path_sum(None, -5)
    path_sum(None, -16)
    path_sum(None, -5)

path_sum(1, 3)
    path_sum(None, -16)
    path_sum(None, -5)
    path_sum(None, -16)
    path_sum(None, -5)

path_sum(None, 6)
path_sum(None, 8)
path_sum(1, 6)
    path_sum(None, -16)
    path_sum(None, -5)
    path_sum(None, -16)
    path_sum(None, -5)

path_sum(1, 8)
    path_sum(None, -16)
    path_sum(None, -5)
    path_sum(None, -16)
    path_sum(None, -5)


path_sum(None, -5)
path_sum(None, -2)

path_sum(None, -16)
path_sum(None, -5)
path_sum(None, -16)
path_sum(None, -5)

path_sum(None, -13)
path_sum(None, -2)
path_sum(None, -13)
path_sum(None, -2)

path_sum(None, 11)
path_sum(None, 8)

path_sum(None, 0)
path_sum(None, 11)
path_sum(None, 0)
path_sum(None, 11)


path_sum(None, -3)
path_sum(None, 8)
path_sum(None, -3)
path_sum(None, 8)



















"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    count = 0
    def path_sum(self, root, sum):
        if root.left is None and root.right is None:
            if root.val == sum or sum == 0:
                self.__class__.count += 1
        elif root.left is not None and root.right is None:
            if root.val == sum:
                self.__class__.count += 1
            else:
                self.path_sum(root.left, sum - root.val)
                self.path_sum(root.left, sum)
        elif root.left is None and root.right is not None:
            if root.val == sum:
                self.__class__.count += 1
            else:
                self.path_sum(root.right, sum - root.val)
                self.path_sum(root.right, sum)
        else:
            if root.val == sum:
                self.__class__.count += 1
            else:
                self.path_sum(root.left, sum - root.val)
                self.path_sum(root.left, sum)
                self.path_sum(root.right, sum - root.val)
                self.path_sum(root.right, sum)

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0
        self.__class__.count = 0
        self.path_sum(root, sum)
        return self.__class__.count
