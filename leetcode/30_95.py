#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
95. 不同的二叉搜索树 II
给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。


示例：

输入：3
输出：
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释：
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

提示：

0 <= n <= 8

generate_trees([1, 2, 3, 4, 5])
    generate_trees([]) root = 1 generate_trees([2, 3, 4, 5])
    generate_trees([1]) root = 2 generate_trees([3, 4, 5])
    generate_trees([1, 2]) root = 3 generate_trees([4, 5])
    generate_trees([1, 2, 3]) root = 4 generate_trees([5])
    generate_trees([1, 2, 3, 4]) root = 5 generate_trees([])

generate_trees([2, 3, 4, 5])
    generate_trees([]) root = 2 generate_trees([3, 4, 5])
    generate_trees([2]) root = 3 generate_trees([4, 5])
    generate_trees([2, 3]) root = 4 generate_trees([5])
    generate_trees([2, 3, 4]) root = 5 generate_trees([])

generate_trees([1, 2, 3, 4])
    generate_trees([]) root = 1 generate_trees([2, 3, 4])
    generate_trees([1]) root = 2 generate_trees([3, 4])
    generate_trees([1, 2]) root = 3 generate_trees([4])
    generate_trees([1, 2, 3]) root = 4 generate_trees([])

generate_trees([3, 4, 5])
    generate_trees([]) root = 3 generate_trees([4, 5])
    generate_trees([3]) root = 4 generate_trees([5])
    generate_trees([3, 4]) root = 5 generate_trees([])

generate_trees([1, 2, 3])
    generate_trees([]) root = 1 generate_trees([2, 3])
    generate_trees([1]) root = 2 generate_trees([3])
    generate_trees([1, 2]) root = 3 generate_trees([])

generate_trees([2, 3, 4])
    generate_trees([]) root = 2 generate_trees([3, 4])
    generate_trees([2]) root = 3 generate_trees([4])
    generate_trees([2, 3]) root = 4 generate_trees([])

generate_trees([1, 2])
    return [root(1), root(2)]

generate_trees([2, 3])
    return [root(2), root(3)]

generate_trees([4, 5])
    return [root(4), root(5)]

generate_trees([3, 4])
    return [root(3), root(4)]

generate_trees([1])
    return [root(1)]

generate_trees([5])
    return [root(5)]

generate_trees([2])
    return [root(2)]

generate_trees([4])
    return [root(4)]

generate_trees([3])
    return [root(3)]

generate_trees([])
    return []

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def generate_trees(self, l):
        length = len(l)
        if length == 0:
            return []
        if length == 1:
            return [TreeNode(l[0])]
        if length == 2:
            return [
                TreeNode(l[0], left=None, right=TreeNode(l[1])),
                TreeNode(l[1], left=TreeNode(l[0]), right=None)
            ]
        """
        5
        0+1+4
        1+1+3
        2+1+2
        3+1+1
        4+1+0
        """
        result = []
        for i in range(length):
            left_list = self.generate_trees(l[0:i])
            right_list = self.generate_trees(l[i + 1:])
            if left_list and right_list:
                for left in left_list:
                    for right in right_list:
                        result.append(TreeNode(l[i], left=left, right=right))
            elif not left_list and right_list:
                for right in right_list:
                    result.append(TreeNode(l[i], left=None, right=right))
            elif left_list and not right_list:
                for left in left_list:
                    result.append(TreeNode(l[i], left=left, right=None))
            else:
                pass
        return result


    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.generate_trees(range(1, n+1))

