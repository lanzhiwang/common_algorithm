#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
112. 路径总和
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2

has_path_sum(5, 22)
    has_path_sum(4, 22-5=17) return True
    has_path_sum(8, 22-5=17) return False
    return True

has_path_sum(4, 17)
    has_path_sum(11, 17-4=13) return True
    return True

has_path_sum(8, 17)
    has_path_sum(13, 17-8=9) return False
    has_path_sum(4, 17-8=9) return False
    return False

has_path_sum(11, 13)
    has_path_sum(7, 13-11=2) return False
    has_path_sum(2, 13-11=2) return True
    return True

has_path_sum(13, 9)
    return False

has_path_sum(4, 9)
    has_path_sum(1, 9-4=5) return False
    return False

has_path_sum(7, 2)
    return False

has_path_sum(2, 2)
    return True

has_path_sum(1, 5)
    return False

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

def has_path_sum(node, sum):
    if node is None:
        return False
    if node.left is not None and node.right is not None:
        return has_path_sum(node.left, sum - node.val) or has_path_sum(node.right, sum - node.val)
    elif node.left is not None and node.right is None:
        return has_path_sum(node.left, sum - node.val)
    elif node.left is None and node.right is not None:
        return has_path_sum(node.right, sum - node.val)
    else:
        return node.val == sum
