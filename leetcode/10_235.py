#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
235. 二叉搜索树的最近公共祖先
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

示例 1:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6
解释: 节点 2 和节点 8 的最近公共祖先是 6。

[6, 2]
[6, 8]




示例 2:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。

   [6, 2]
[6, 2, 4]



[6, 2, 4, 3]
   [6, 8, 9]

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉搜索树中。
"""

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



def find_path(node, target):
    if node.value == target.value:
        return [node.value]
    else:
        left_result = None
        right_result = None
        if node.left is None and node.right is None:
            return None
        elif node.left is not None and node.right is None:
            left_result = find_path(node.left, target)
        elif node.left is None and node.right is not None:
            right_result = find_path(node.right, target)
        else:
            left_result = find_path(node.left, target)
            right_result = find_path(node.right, target)

        if left_result is not None and right_result is None:
            left_result.insert(0, node.value)
            return left_result
        elif left_result is None and right_result is not None:
            right_result.insert(0, node.value)
            return right_result
        else:
            return None

def lowest_common_ancestor(root, p, q):
    p_path = find_path(root, p)
    q_path = find_path(root, q)
    if p_path is None or q is None:
        return None
    for p_i in p_path[::-1]:
        for q_i in q_path[::-1]:
            if p_i == q_i:
                return p_i
    return None
