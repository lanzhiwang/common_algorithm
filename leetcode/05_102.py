#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
102. 二叉树的层序遍历
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

"""

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
