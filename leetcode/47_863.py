#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
863. 二叉树中所有距离为 K 的结点
给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。

返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。

示例 1：

输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
输出：[7,4,1]
解释：
所求结点为与目标结点（值为 5）距离为 2 的结点，
值分别为 7，4，以及 1

              3
         /         \
        5           1
      /   \       /   \
     6     2     0     8
          / \
         7   4

target_to_root(3, 2, 0, None)
    target_to_root(5, 2, 1, l) return (2, l)
    target_to_root(1, 2, 1, r) return None
    return (2, l)

target_to_root(5, 2, 1, l)
    target_to_root(6, 2, 2, l) return None
    target_to_root(2, 2, 2, l) return (2, l)
    return (2, l)

target_to_root(1, 2, 1, r)
    target_to_root(0, 2, 2, r) return None
    target_to_root(8, 2, 2, r) return None
    return None

target_to_root(6, 2, 2, l)
    target_to_root(None, 2, 3, l) return None
    target_to_root(None, 2, 3, l) return None
    return None

target_to_root(2, 2, 2, l)
    target_to_root(7, 2, 3, l) return None
    target_to_root(4, 2, 3, l) return None
    return (2, l)

target_to_root(0, 2, 2, r)
    target_to_root(None, 2, 3, r) return None
    target_to_root(None, 2, 3, r) return None
    return None

target_to_root(8, 2, 2, r)
    target_to_root(None, 2, 3, r) return None
    target_to_root(None, 2, 3, r) return None
    return None

target_to_root(None, 2, 3, l)
target_to_root(None, 2, 3, l)
target_to_root(7, 2, 3, l)
    target_to_root(None, 2, 4, l) return None
    target_to_root(None, 2, 4, l) return None
    return None

target_to_root(4, 2, 3, l)
    target_to_root(None, 2, 4, l) return None
    target_to_root(None, 2, 4, l) return None
    return None

target_to_root(None, 2, 3, r)
target_to_root(None, 2, 3, r)

target_to_root(None, 2, 3, r)
target_to_root(None, 2, 3, r)






0 1 None 3 2
2
        0
       /
      1
     / \
    3   2
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    result = []
    def target_to_root(self, node, target, dis, direction):
        if node is None:
            return None
        if direction is not None:
            left_dis = self.target_to_root(node.left, target, dis + 1, direction)
            right_dis = self.target_to_root(node.right, target, dis + 1, direction)
        else:
            left_dis = self.target_to_root(node.left, target, dis + 1, 'l')
            right_dis = self.target_to_root(node.right, target, dis + 1, 'r')

        if left_dis is None and right_dis is None:
            if node.val == target.val:
                return (dis, direction)
            else:
                return None
        else:
            if left_dis is not None and right_dis is None:
                return left_dis
            elif left_dis is None and right_dis is not None:
                return right_dis

    def find_node_with_dis(self, node, target, node_dis, target_dis, node_direction, target_direction):
        if node is None:
            return None
        if node_direction is not None:
            left_dis = self.find_node_with_dis(node.left, target, node_dis + 1, target_dis, node_direction, target_direction)
            right_dis = self.find_node_with_dis(node.right, target, node_dis + 1, target_dis, node_direction, target_direction)
        else:
            left_dis = self.find_node_with_dis(node.left, target, node_dis + 1, target_dis, 'l', target_direction)
            right_dis = self.find_node_with_dis(node.right, target, node_dis + 1, target_dis, 'r', target_direction)
        if left_dis is None and right_dis is None:
            if node_dis == target_dis and node_direction in target_direction and node.val != target.val:
                self.__class__.result.append(node.val)
            else:
                return None
        else:
            if left_dis is not None and right_dis is None:
                return left_dis
            elif left_dis is None and right_dis is not None:
                return right_dis

    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        if root is None:
            return []
        self.__class__.result = []
        if root.val == target.val:
            self.find_node_with_dis(root, target, 0, K, None, ['l', 'r', None])
            return self.__class__.result
        target_to_root = self.target_to_root(root, target, 0, None)  # (3, l) (3, r) (0, None)
        if target_to_root is None:
            return []
        self.find_node_with_dis(root, target, 0, target_to_root[0] + K, None, [target_to_root[1], None])
        if target_to_root[0] - K >= 0:
            self.find_node_with_dis(root, target, 0, target_to_root[0] - K, None, [target_to_root[1], 'None'])
        else:
            if target_to_root[1] == 'l':
                self.find_node_with_dis(root, target, 0, abs(target_to_root[0] - K), None, ['r', None])
            if target_to_root[1] == 'r':
                self.find_node_with_dis(root, target, 0, abs(target_to_root[0] - K), None, ['l', None])
        return self.__class__.result
