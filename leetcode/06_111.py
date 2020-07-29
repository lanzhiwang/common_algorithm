#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
111. 二叉树的最小深度
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.

depth_of_tree(3, 1)
    depth_of_tree(9, 2) return 2
    depth_of_tree(20, 2) return 3
    return 2

depth_of_tree(9, 2)
    return 2

depth_of_tree(20, 2)
    depth_of_tree(15, 3) return 3
    depth_of_tree(7, 3) return 3
    return 3

depth_of_tree(15, 3)
    return 3

depth_of_tree(7, 3)
    return 3



         1
      /    \
     2      3
    / \    /
   4   5  6
      /  /
     7  8
         \
          9

depth_of_tree(1, 1)
    depth_of_tree(2, 2) return 3
    depth_of_tree(3, 2) return 5
    return 3

depth_of_tree(2, 2)
    depth_of_tree(4, 3) return 3
    depth_of_tree(5, 3) return 4
    return 3

depth_of_tree(3, 2)
    depth_of_tree(6, 3) return 5
    return 5

depth_of_tree(4, 3)
    return 3

depth_of_tree(5, 3)
    depth_of_tree(7, 4) return 4
    return 4

depth_of_tree(6, 3)
    depth_of_tree(8, 4) return 5
    return 5

depth_of_tree(7, 4)
    return 4

depth_of_tree(8, 4)
    depth_of_tree(9, 5) return 5
    return 5

depth_of_tree(9, 5)
    return 5

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

tree = Node(3)
tree.left = Node(9)
tree.right = Node(20)
tree.right.left = Node(15)
tree.right.right = Node(7)

def min_depth(node, depth):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return depth

    left_depth =  None
    right_depth = None
    if node.left is not None:
        left_depth = min_depth(node.left, depth + 1)
    if node.right is not None:
        right_depth = min_depth(node.right, depth + 1)

    if left_depth is not None and right_depth is not None:
        return min(left_depth,right_depth)
    elif left_depth is not None and right_depth is None:
        return left_depth
    elif left_depth is None and right_depth is not None:
        return right_depth

print(min_depth(tree, 1))


