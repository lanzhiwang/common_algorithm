#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
538. 把二叉搜索树转换为累加树
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，
使得每个节点的值是原来的节点值加上所有大于它的节点值之和。


例如：

输入: 原始二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13

2  5  13
20 18 13




9 7 10 5 3 8 6 1 4 2 15 16 18 12 11 13

                  9
              /      \
             7       10
            / \        \
           5   8        15
          / \           / \
         3   6         12  16
        / \            / \   \
       1   4          11 13   18
        \
         2



"""

from queue import Queue

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


def inorder_traverse(node):
    result = []
    if node.left is not None:
        result.extend(inorder_traverse(node.left))
    result.append(node)
    if node.right is not None:
        result.extend(inorder_traverse(node.right))
    return result


# 广度遍历
def breadth_traversal(node):
    result = []
    queue = Queue()
    queue.put(node)
    while not queue.empty():
        node = queue.get()
        result.append(node)

        if node.left is not None:
            queue.put(node.left)

        if node.right is not None:
            queue.put(node.right)
    return result


def convert_bst(node):
    if node is None:
        return 0
    node_list = inorder_traverse(node)[::-1]
    for i, n in enumerate(node_list):
        if i != 0:
            n.value += node_list[i-1].value
    return node
