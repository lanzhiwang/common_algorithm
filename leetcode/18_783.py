#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
783. 二叉搜索树节点最小距离
给定一个二叉搜索树的根节点 root，返回树中任意两节点的差的最小值。


示例：

输入: root = [4,2,6,1,3,null,null]
输出: 1
解释:
注意，root是树节点对象(TreeNode object)，而不是数组。

给定的树 [4,2,6,1,3,null,null] 可表示为下图:

          4
        /   \
      2      6
     / \
    1   3

最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。
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


def inorder_traverse(node):
    result = []
    if node.left is not None:
        result.extend(inorder_traverse(node.left))
    result.append(node.value)
    if node.right is not None:
        result.extend(inorder_traverse(node.right))
    return result


def min_diff_in_bst(root):
    if root is None:
        return None
    if root.left is None and root.right is None:
        return None
    root_list = inorder_traverse(root)
    min_value = float('inf')
    length = len(root_list)
    for index, value in enumerate(root_list):
        if index <= length - 2:
            min_value = min(min_value, abs(value-root_list[index + 1]))

    return min_value


print(min_diff_in_bst(list_to_tree([27, None, 34, None, 58, 50, None, 44, None, None, None])))




