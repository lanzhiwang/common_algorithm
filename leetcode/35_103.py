#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
103. 二叉树的锯齿形层次遍历
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]

    3
   / \
  9  20
    /  \
   15   7
left_stack = [3]
right_stack = []

[3]
left_stack = []
right_stack = [9, 20]

[3]
[20, 9]
left_stack = [7, 15]
right_stack = []

"""



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Stack(object):
    def __init__(self):
        self.stack = []

    def __bool__(self):
        return bool(self.stack)

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('pop from an empty stack')

    def is_empty(self):
        """ Check if a stack is empty."""
        return not bool(self.stack)




class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        left_stack = Stack()
        right_stack = Stack()
        left_stack.push(root)
        result = []
        while not left_stack.is_empty() or not right_stack.is_empty():
            temp = []
            while not left_stack.is_empty():
                node = left_stack.pop()
                temp.append(node.val)
                if node.left is not None:
                    right_stack.push(node.left)
                if node.right is not None:
                    right_stack.push(node.right)
            if temp:
                result.append(temp)

            temp = []
            while not right_stack.is_empty():
                node = right_stack.pop()
                temp.append(node.val)
                if node.right is not None:
                    left_stack.push(node.right)
                if node.left is not None:
                    left_stack.push(node.left)
            if temp:
                result.append(temp)
        return result
