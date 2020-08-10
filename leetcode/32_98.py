#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
98. 验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true

pre = [float('-inf'), 1, 2]
is_valid_bst(2)
    is_valid_bst(1)  return True
    2
    is_valid_bst(3)  return True

is_valid_bst(1)
    is_valid_bst(None)  return True
    1
    is_valid_bst(None)  return True
    return True


is_valid_bst(None)
    return True

示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。


(5, -inf)
(1, -inf)
(None, -inf)
(None, -inf)
(4, -inf)
(3, -inf)
(None, -inf)
(None, -inf)
(6, -inf)
(None, -inf)
(None, -inf)
True


pre = [float('-inf'), 1, 5]
is_valid_bst(5)
    is_valid_bst(1)  return True
    5
    is_valid_bst(4) return False
    return False

is_valid_bst(1)
    is_valid_bst(None)  return True
    1
    is_valid_bst(None)  return True
    return True


is_valid_bst(None)
    return True

is_valid_bst(4)
    is_valid_bst(3)  return False
    return False


is_valid_bst(3)
    is_valid_bst(None)  return True
    3
    is_valid_bst(None)  return True
    return False



           5
        /     \
       1       6
          \     \
           4     7
          /
         3

is_valid_bst(5)
    left_val = inorder_traverse(1, max) 4
    5
    right_val = inorder_traverse(6, min) 6

    is_valid_bst(1)
    is_valid_bst(6)
    return True


is_valid_bst(1)
    left_val = None
    1
    right_val = inorder_traverse(4, min) 3

    is_valid_bst(4)
    return True

is_valid_bst(6)
    left_val = None
    6
    right_val = inorder_traverse(7, min) 7

    is_valid_bst(7)
    return True


is_valid_bst(4)
    left_val = inorder_traverse(3, max) 3
    4
    right_val = None

    is_valid_bst(3)
    return True


is_valid_bst(7)
    return True

is_valid_bst(3)
    return True


          10
      /       \
     5         15
   /   \      /  \
 null  null  6    20




           5
        /     \
       1       6
          \     \
           4     7
          /
         3

pre = [float('-inf'), 1, 3, 4, 5, 6]
is_valid_bst(5)
    is_valid_bst(1)  return True
    5
    is_valid_bst(6)  return True
    return True

is_valid_bst(1)
    is_valid_bst(None)  return True
    1
    is_valid_bst(4)  return True
    return True

is_valid_bst(None)
    return True

is_valid_bst(4)
    is_valid_bst(3)  return True
    4
    is_valid_bst(None)  return True
    return True

is_valid_bst(3)
    is_valid_bst(None)  return True
    3
    is_valid_bst(None)  return True
    return True

is_valid_bst(6)
    is_valid_bst(None)  return True
    6
    is_valid_bst(7)  return True
    return True

is_valid_bst(7)
    is_valid_bst(None)  return True
    7
    is_valid_bst(None)  return True
    return True
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SolutionOther(object):
    def inorder_traverse(self, node):
        result = []
        if node.left is not None:
            result.extend(self.inorder_traverse(node.left))
        result.append(node.val)
        if node.right is not None:
            result.extend(self.inorder_traverse(node.right))
        return result

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        elif root.left is not None and root.right is None:
            left_max = self.inorder_traverse(root.left)[-1]
            if root.val > left_max and self.isValidBST(root.left):
                return True

        elif root.left is None and root.right is not None:
            right_mix = self.inorder_traverse(root.right)[0]
            if root.val < right_mix and self.isValidBST(root.right):
                return True

        else:
            left_max = self.inorder_traverse(root.left)[-1]
            right_mix = self.inorder_traverse(root.right)[0]
            if root.val > left_max and root.val < right_mix and self.isValidBST(root.left) and self.isValidBST(root.right):
                return True

        return False


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


class Solution(object):
    pre = float('-inf')
    def isValidBST(self, root):
        if hasattr(root, 'val'):
            print(root.val, self.__class__.pre)
        else:
            print(root, self.__class__.pre)

        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if self.isValidBST(root.left):
            if root.val > self.__class__.pre:
                self.__class__.pre = root.val
                if self.isValidBST(root.right):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

print(Solution().isValidBST(list_to_tree([0])))
