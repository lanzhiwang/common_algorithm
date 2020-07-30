#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
将列表转为二叉树
输入: [1, 2, 3]
输出:
       1
      / \
     2   3

输入: [-10, 9, 20, None, None, 15, 7]
输出:
   -10
   / \
  9  20
    /  \
   15   7

通过下标确定左右节点
i -> left   right
i -> 2*i+1  2*i+2
0 -> 1      2
1 -> 3      4
2 -> 5      6
3 -> 7      8
4 -> 9      10

list_to_tree([-10, 9, 20, None, None, 15, 7], 0)
    node = Node(-10)
    node.left = list_to_tree([-10, 9, 20, None, None, 15, 7], 1)
    node.right = list_to_tree([-10, 9, 20, None, None, 15, 7], 2)
    return node

list_to_tree([-10, 9, 20, None, None, 15, 7], 1)
    node = Node(9)
    node.left = list_to_tree([-10, 9, 20, None, None, 15, 7], 3)
    node.right = list_to_tree([-10, 9, 20, None, None, 15, 7], 4)
    return node

list_to_tree([-10, 9, 20, None, None, 15, 7], 2)
    node = Node(20)
    node.left = list_to_tree([-10, 9, 20, None, None, 15, 7], 5)
    node.right = list_to_tree([-10, 9, 20, None, None, 15, 7], 6)
    return node

list_to_tree([-10, 9, 20, None, None, 15, 7], 3)
    return None
list_to_tree([-10, 9, 20, None, None, 15, 7], 4)
    return None

list_to_tree([-10, 9, 20, None, None, 15, 7], 5)
    node = Node(15)
    node.left = list_to_tree([-10, 9, 20, None, None, 15, 7], 11)
    node.right = list_to_tree([-10, 9, 20, None, None, 15, 7], 12)
    return node

list_to_tree([-10, 9, 20, None, None, 15, 7], 6)
    node = Node(7)
    node.left = list_to_tree([-10, 9, 20, None, None, 15, 7], 13)
    node.right = list_to_tree([-10, 9, 20, None, None, 15, 7], 14)
    return node

list_to_tree([-10, 9, 20, None, None, 15, 7], 11)
    return None

list_to_tree([-10, 9, 20, None, None, 15, 7], 12)
    return None

list_to_tree([-10, 9, 20, None, None, 15, 7], 13)
    return None

list_to_tree([-10, 9, 20, None, None, 15, 7], 14)
    return None

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

    node = Node(value)
    node.left = list_to_tree(source_list, 2 * index + 1)
    node.right = list_to_tree(source_list, 2 * index + 2)
    return node

tree = list_to_tree([1, 2, 3], 0)
print tree.value
print tree.left.value
print tree.right.value


