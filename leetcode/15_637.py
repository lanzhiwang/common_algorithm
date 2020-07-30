#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
637. 二叉树的层平均值
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

示例 1：

输入：
    3
   / \
  9  20
    /  \
   15   7
输出：[3, 14.5, 11]
解释：
第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
"""


from queue import Queue


class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
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


def average_of_levels(node):
    # [[3], [9, 20], [15, 7]]
    result = []
    result_list = level_order(node)
    for l in result_list:
        result.append(float(sum(l))/float(len(l)))
    return result


print average_of_levels(list_to_tree([3, 9, 20, None, None, 15, 7]))
