#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
                    1
           /                 \
          2                   3
      /       \           /       \
     4->       5         6         7
  /     \   /     \   /     \   /     \
 8->     9 10     11 12     13 14     15

connect_with_parent(1, None)
    connect_with_parent(2, 1)

    connect_with_parent(3, 1)

connect_with_parent(2, 1)
    connect_with_parent(4, 2)

    connect_with_parent(5, 2)

connect_with_parent(4, 2)
    connect_with_parent(8, 4)
    4->5
    connect_with_parent(9, 4)

connect_with_parent(8, 4)
    8->9

connect_with_parent(9, 4)
    9->10

"""

# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def is_left(self, node, parent):
        if parent.left is node:
            return True

    def connect_with_parent(self, node, parent):
        if parent is None:
            self.connect_with_parent(node.left, node)
            node.next = None
            self.connect_with_parent(node.right, node)
        else:
            if node.left is None and node.right is None:
                if self.is_left(node, parent):
                    node.next = parent.right
                else:
                    if parent.next is not None:
                        node.next = parent.next.left
                    else:
                        node.next = None
            if node.left is not None:
                self.connect_with_parent(node.left, node)

            if self.is_left(node, parent):
                node.next = parent.right
            else:
                if parent.next is not None:
                    node.next = parent.next.left
                else:
                    node.next = None

            if node.right is not None:
                self.connect_with_parent(node.right, node)

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        if root.left is None and root.right is None:
            root.next = None
            return root
        self.connect_with_parent(root, None)
        return root