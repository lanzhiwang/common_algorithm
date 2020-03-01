#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
from queue import Queue
queue = Queue()
queue.put()
queue.get()
queue.empty()
"""
from queue import Queue


r"""
初始化二叉树

         1
        / \
      2    3
     / \  / \
    4  5  6 7

广度遍历
1 2 3 4 5 6 7

"""


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return 'value=%s, left=%s, right=%s' % (self.value, self.left.value, self.right.value)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


# 广度遍历
def breadth_traversal(node):
    result = []
    queue = Queue()
    queue.put(root)
    while not queue.empty():
        node = queue.get()
        result.append(node.value)

        if node.left is not None:
            queue.put(node.left)

        if node.right is not None:
            queue.put(node.right)
    return result


print('广度遍历')
print(breadth_traversal(root))
