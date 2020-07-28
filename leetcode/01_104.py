#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

"""


r"""

         1
      /    \
     2      3
    / \    /
   4   5  6
      /  /
     7  8
         \
          9

depth_of_tree(1)
    depth_of_tree(2)  # return 3
    depth_of_tree(3)  # return 4
    return 1 + max(3, 4) = 5

depth_of_tree(2)
    depth_of_tree(4)  # return 1
    depth_of_tree(5)  # return 2
    return 1 + max(1, 2) = 3

depth_of_tree(3)
    depth_of_tree(6)  # return 3
    depth_of_tree()  # return 0
    return 1 + max(3, 0) = 4

depth_of_tree(4)
    depth_of_tree()  # return 0
    depth_of_tree()  # return 0
    return 1 + max(0, 0) = 1

depth_of_tree(5)
    depth_of_tree(7)  # return 1
    depth_of_tree()  # return 0
    return 1 + max(1, 0) = 2

depth_of_tree(6)
    depth_of_tree(8)  # return 2
    depth_of_tree()  # return 0
    return 1 + max(2, 0) = 3

depth_of_tree(7)
    depth_of_tree()  return 0
    depth_of_tree()  return 0
    return 1 + max(0, 0) = 1

depth_of_tree(8)
    depth_of_tree()  return 0
    depth_of_tree(9) return 1
    return 1 + max(0, 1) = 2

depth_of_tree(9)
    depth_of_tree()  return 0
    depth_of_tree()  return 0
    return 1 + max(0, 0) = 1

depth_of_tree()
    return 0
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def depth_of_tree(tree):
    if tree is None:
        return 0
    else:
        depth_l_tree = depth_of_tree(tree.left)
        depth_r_tree = depth_of_tree(tree.right)
        if depth_l_tree > depth_r_tree:
            return 1 + depth_l_tree
        else:
            return 1 + depth_r_tree


tree = Node(3)
tree.left = Node(9)
tree.right = Node(20)
tree.right.left = Node(15)
tree.right.right = Node(7)

print(depth_of_tree(tree))
