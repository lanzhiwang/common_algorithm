#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
124. 二叉树中的最大路径和
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42

解决方法：
https://www.cnblogs.com/ariel-dreamland/p/9166216.html

       1
      / \
     2   3

max_path_sum(1)
    left = max_path_sum(2) return 2
    right = max_path_sum(3) return 3
    max = 6
    return 4

max_path_sum(2)
    left = max_path_sum(None) return 0
    right = max_path_sum(None) return 0
    max = 2
    return 2

max_path_sum(3)
    left = max_path_sum(None) return 0
    right = max_path_sum(None) return 0
    max = 3
    return 3

max_path_sum(None)
    return 0


   -10
   / \
  9  20
    /  \
   15   7

max_path_sum(-10)
    max_path_sum(9) return 9
    max_path_sum(20) return 35
    max = 34
    return 25

max_path_sum(9)
    max_path_sum(None) return 0
    max_path_sum(None) return 0
    max = 9
    return 9

max_path_sum(20)
    max_path_sum(15) return 15
    max_path_sum(7) return 7
    max = 42
    return 35

max_path_sum(15)
    max_path_sum(None) return 0
    max_path_sum(None) return 0
    max = 15
    return 15

max_path_sum(7)
    max_path_sum(None) return 0
    max_path_sum(None) return 0
    max = 7
    return 7

max_path_sum(None)
    return 0

     2
    /
  -1
  /
 10

    2
   /
 -1

max_path_sum(2)
    max_path_sum(-1) return 0
    max_path_sum(None) return 0
    max = 2
    return 2

max_path_sum(-1)
    max_path_sum(None) return 0
    max_path_sum(None) return 0
    max = -1
    return 0

max_path_sum(None)
    return 0

"""

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
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


result = float('-inf')
def max_path_sum(node):
    global result
    if node is None:
        return 0
    left = max_path_sum(node.left)
    right = max_path_sum(node.right)
    result = max(result, left + right + node.value)
    if max(left, right) + node.value > 0:
        return max(left, right) + node.value
    else:
        return 0

tree = Node(2)
tree.left = Node(-1)
max_path_sum(tree)

print result
