#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
508. 出现次数最多的子树元素和
给你一个二叉树的根结点，请你找出出现次数最多的子树元素和。一个结点的「子树元素和」定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。

你需要返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。


示例 1：
输入:

  5
 /  \
2   -3
返回 [2, -3, 4]，所有的值均只出现一次，以任意顺序返回所有值。

示例 2：
输入：

  5
 /  \
2   -5
返回 [2]，只有 2 出现两次，-5 只出现 1 次。

提示： 假设任意子树元素和均可以用 32 位有符号整数表示。


find_frequent_tree_sum(5)
    find_frequent_tree_sum(2)  return 2
    find_frequent_tree_sum(-3)  return -3
    return 2+(-3)+5 = 4


find_frequent_tree_sum(2)
    find_frequent_tree_sum(None)  return 0
    find_frequent_tree_sum(None)  return 0
    return 2

find_frequent_tree_sum(-3)
    find_frequent_tree_sum(None)  return 0
    find_frequent_tree_sum(None)  return 0
    return -3

find_frequent_tree_sum(None)
    return 0

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import Counter

class Solution(object):
    count = []
    def find_frequent_tree_sum(self, node):
        if node is None:
            return 0
        result = node.val + self.find_frequent_tree_sum(node.left) + self.find_frequent_tree_sum(node.right)
        self.__class__.count.append(result)
        return result

    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        self.__class__.count = []
        self.find_frequent_tree_sum(root)
        count_list = sorted(Counter(self.__class__.count).items(), key=lambda x:x[1], reverse = True)
        count_max = count_list[0][1]
        result = []
        for l in count_list:
            if l[1] == count_max:
                result.append(l[0])
        return result
