#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
897. 递增顺序查找树
给你一个树，请你 按中序遍历 重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。


示例 ：

输入：[5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9


提示：

给定树中的结点数介于 1 和 100 之间。
每个结点都有一个从 0 到 1000 范围内的唯一整数值。

"""

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right


def list_to_tree(source_list, index=0):
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

r"""
                    5
             /             \
            3               6
         /     \         /     \
        2       4       N       8
      /   \   /   \   /   \   /   \
     1     N N     N N     N 7     9

"""


def inorder_traverse(node):
    result = []
    if node.left is not None:
        result.extend(inorder_traverse(node.left))
    result.append(node.value)
    if node.right is not None:
        result.extend(inorder_traverse(node.right))
    return result


def increasing_bst(root):
    node_list = inorder_traverse(root)
    last_node = None
    for value in node_list[::-1]:
        temp = Node(value)
        temp.right = last_node
        last_node = temp
    return last_node


tree = list_to_tree([5, 3, 6, 2, 4, None, 8, 1, None, None, None, None, None, 7, 9])
print(inorder_traverse(tree))
