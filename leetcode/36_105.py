#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
105. 从前序与中序遍历序列构造二叉树
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    root = 3
    root.left = buildTree([9], [9])  return 9
    root.right = buildTree([20, 15, 7], [15, 20, 7])  return 20

buildTree([9], [9])
    root = 9
    root.left = None
    root.right = None
    return 9

buildTree([20, 15, 7], [15, 20, 7])
    root = 20
    root.left = buildTree([15], [15])  return 15
    root.right = buildTree([7], [7])  return 7
    return 20

buildTree([15], [15])
    return 15

buildTree([7], [7])
    return 7


buildTree([1, 2], [1, 2])
    root = 1
    root.left = 
    root.right = 

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        if len(preorder) == 1 and len(inorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index + 1], inorder[0:index])
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return root
