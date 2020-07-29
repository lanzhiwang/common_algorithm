#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \   / \
  5 6   7

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

[1, 2, 5]
[1, 3, 6]
[1, 3, 7]

binary_tree_paths(1)
    binary_tree_paths(2) return [[2, 5]]
    binary_tree_paths(3) return [[3, 6], [3, 7]]
    return [[1, 2, 5], [1, 3, 6], [1, 3, 7]]

binary_tree_paths(2)
    binary_tree_paths(5) return [[5]]
    return [[2, 5]]

binary_tree_paths(3)
    binary_tree_paths(6) return [[6]]
    binary_tree_paths(7) return [[7]]
    return [[3, 6], [3, 7]]

binary_tree_paths(5)
    return [[5]]

binary_tree_paths(6)
    return [[6]]

binary_tree_paths(7)
    return [[7]]

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.right = Node(5)

def binary_tree_paths(node):
    if node is None:
        return []

    if node.left is None and node.right is None:
        return [[node.val]]

    result = []
    if node.left is not None:
        for left_list in binary_tree_paths(node.left):
            left_list.insert(0, node.val)
            result.append(left_list)

    if node.right is not None:
        for right_list in binary_tree_paths(node.right):
            right_list.insert(0, node.val)
            result.append(right_list)
    return result

print(binary_tree_paths(tree))


