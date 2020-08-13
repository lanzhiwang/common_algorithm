#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
         1
     /      \
    2        3
  /           \
 4             5


"""


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Queue(object):
    def __init__(self):
        self.q = []

    def put(self, value):
        self.q.append(value)

    def get(self):
        try:
            return self.q.pop(0)
        except IndexError:
            raise IndexError

    def peek(self):
        if self.q:
            return self.q[0]

    def empty(self):  # 0->True  1->False
        return False if len(self.q) else True

    def __str__(self):
        result = []
        for n in self.q:
            result.append(n.val)
        return '%s' % result


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        queue1 = Queue()
        queue2 = Queue()
        queue1.put(root)
        while not queue1.empty() or not queue2.empty():
            while not queue1.empty():
                node = queue1.get()
                if not queue1.empty():
                    next = queue1.peek()
                else:
                    next = None
                node.next = next

                if node.left is not None:
                    queue2.put(node.left)
                if node.right is not None:
                    queue2.put(node.right)

            while not queue2.empty():
                node = queue2.get()
                if not queue2.empty():
                    next = queue2.peek()
                else:
                    next = None
                node.next = next

                if node.left is not None:
                    queue1.put(node.left)
                if node.right is not None:
                    queue1.put(node.right)

        return root
