#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""

1,0,1,0,0,0,1
           1-0
       /        \
     0-1        1-2
    /   \      /   \
   0-3  0-4  0-5   1-6

           1-0
       /        \
     None        1-2
    /   \      /   \
   None  None None   1-6

prune_tree(1-0, None, None)
    prune_tree(0-1, 1-0, left)  return True
    prune_tree(1-2, 1-0, right)  return False
    return False

prune_tree(0-1, 1-0, left)
    prune_tree(0-3, 1-0, left)  return True
    prune_tree(0-4, 1-0, right)  return True
    1-0.left = None
    return True

prune_tree(1-2, 1-0, right)
    prune_tree(0-5, 1-2, left)  return True
    prune_tree(1-6, 1-2, right)  return False
    return False

prune_tree(0-3, 1-0, left)
    prune_tree(None, )  return True
    prune_tree(None, )  return True
    1-0.left = None
    return True

prune_tree(0-4, 1-0, right)
    prune_tree(None, )  return True
    prune_tree(None, )  return True
    1-0.right = None
    return True

prune_tree(0-5, 1-2, left)
    prune_tree(None, )  return True
    prune_tree(None, )  return True
    1-2.left = None
    return True

prune_tree(1-6, 1-2, right)
    prune_tree(None, )  return True
    prune_tree(None, )  return True
    return False

prune_tree(None, )
    return True

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def prune_tree(self, node, parent, direction):
        if node is None:
            return True
        left_tree = self.prune_tree(node.left, node, 'left')
        right_tree = self.prune_tree(node.right, node, 'right')
        if node.val == 0 and left_tree and right_tree:
            if direction is not None:
                setattr(parent, direction, None)
            return True
        else:
            return False

    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if self.prune_tree(root, None, None):
            return None
        else:
            return root
