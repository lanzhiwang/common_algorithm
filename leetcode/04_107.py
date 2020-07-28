#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
107. 二叉树的层次遍历 II
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]


    3
   / \
  9  20
    /  \
   15   7

queue1(3) queue2()

[[3]] queue1() queue2(9, 20)
[[3], [9]] queue1() queue2(20)
[[3], [9, 20]] queue1(15, 7) queue2()
[[3], [9, 20], [15]] queue1(7) queue2()
[[3], [9, 20], [15, 7]] queue1() queue2()
"""

from queue import Queue


class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = Node(3)
root.left = Node(9)
root.right = Node(20)
# root.left.left = Node(4)
# root.left.right = Node(5)
root.right.left = Node(15)
root.right.right = Node(7)


def level_order(root):
    if root is None:
        return []
    result = []
    queue1 = Queue()
    queue2 = Queue()
    queue1.put(root)

    temp_result = []
    while not queue1.empty() or not queue2.empty():
        while not queue1.empty():
            node = queue1.get()
            temp_result.append(node.val)
            if node.left is not None:
                queue2.put(node.left)
            if node.right is not None:
                queue2.put(node.right)
        if temp_result:
            result.append(temp_result)
        temp_result = []

        while not queue2.empty():
            node = queue2.get()
            temp_result.append(node.val)
            if node.left is not None:
                queue1.put(node.left)
            if node.right is not None:
                queue1.put(node.right)
        if temp_result:
            result.append(temp_result)
        temp_result = []
    return result

print(level_order(root))

result = level_order(root)
result.reverse()
print(result)
