#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
100. 相同的树

给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

isSameTree(1, 1)
    1 == 1
    isSameTree(2, 2)  return True
    isSameTree(3, 3)  return True
    return True


isSameTree(2, 2)
    2 == 2
    isSameTree(None, None)  return True
    isSameTree(None, None)  return True
    return True


isSameTree(3, 3)
    3 == 3
    isSameTree(None, None)  return True
    isSameTree(None, None)  return True
    return True


isSameTree(None, None)
    return True
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


def is_same_tree(p, q):
    if p is None and q is None:
        return True
    if p is not None and q is not None:
        if is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right) and p.value == q.value:
            return True
    return False

print(is_same_tree(list_to_tree([1, 2, 3]), list_to_tree([1, 2, 3])))
print(is_same_tree(list_to_tree([1, 2]), list_to_tree([1, None, 2])))
print(is_same_tree(list_to_tree([1, 2, 1]), list_to_tree([1, 1, 2])))
