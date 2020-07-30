#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
563. 二叉树的坡度
给定一个二叉树，计算整个树的坡度。

一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。空结点的的坡度是0。

整个树的坡度就是其所有节点的坡度之和。


示例：

输入：
         1
       /   \
      2     3
输出：1
解释：
结点 2 的坡度: 0
结点 3 的坡度: 0
结点 1 的坡度: |2-3| = 1
树的坡度 : 0 + 0 + 1 = 1

提示：

任何子树的结点的和不会超过 32 位整数的范围。
坡度的值不会超过 32 位整数的范围。

         1
       /   \
      2     3

find_tilt(1)
    find_tilt(2) return 2
    find_tilt(3) return 3
    tilt = 1
    return 6

find_tilt(2)
    find_tilt(None) return 0
    find_tilt(None) return 0
    tilt = 0
    return 2

find_tilt(3)
    find_tilt(None) return 0
    find_tilt(None) return 0
    tilt = 0
    return 3

find_tilt(None)
    return 0

"""

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def list_to_tree(source_list, index):
    if not source_list:
        return None
    try:
        value = source_list[index]
        if value is None:
            return None
    except IndexError:
        return None

    root = Node(value)
    root.left = list_to_tree(source_list, 2 * index + 1)
    root.right = list_to_tree(source_list, 2 * index + 2)
    return root


class Solution(object):
    tilt = 0
    def find_tilt(self, node):
        if node is None:
            return 0
        left_sum = self.find_tilt(node.left)
        right_sum = self.find_tilt(node.right)
        self.__class__.tilt += abs(left_sum - right_sum)
        return left_sum + node.val + right_sum

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.find_tilt(root)
        result = self.__class__.tilt
        self.__class__.tilt = 0
        return result

