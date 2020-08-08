#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
700. 二叉搜索树中的搜索
给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。

例如，

给定二叉搜索树:

        4
       / \
      2   7
     / \
    1   3

和值: 2
你应该返回如下子树:

      2
     / \
    1   3
在上述示例中，如果要找的值是 5，但因为没有节点值为 5，我们应该返回 NULL。

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


def search_bst(root, val):
    if root is None:
        return None
    if root.value != val and root.left is None and root.right is None:
        return None
    if root.value == val:
        return root
    if root.value > val:
        return search_bst(root.left, val)
    else:
        return search_bst(root.right, val)

print(search_bst(list_to_tree([4, 2, 7, 1, 3]) ,2))
