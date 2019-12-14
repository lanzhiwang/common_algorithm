#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
队列，先进先出

入队 put()
出队 get()
队列为空 empty()

"""


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

    def empty(self):  # 0->True  1->False
        return False if len(self.q) else True

    def __str__(self):
        return '%s' % self.q


class Node(object):
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return 'value=%s, left=%s, right=%s' % (self.value, self.left, self.right)


node0 = Node(1, 1, 2)
node1 = Node(2, 3, 4)
node2 = Node(3, 5, 6)
node3 = Node(4, -1, -1)
node4 = Node(5, -1, -1)
node5 = Node(6, -1, -1)
node6 = Node(7, -1, -1)

nodes = [node0, node1, node2, node3, node4, node5, node6]


# 广度遍历
def breadth_traversal(nodes, root):
    result = []
    queue = Queue()
    queue.put(root)
    while not queue.empty():
        node = queue.get()
        result.append(node.value)

        if node.left != -1:
            queue.put(nodes[node.left])

        if node.right != -1:
            queue.put(nodes[node.right])
    return result


print('广度遍历')
print(breadth_traversal(nodes, node0))
