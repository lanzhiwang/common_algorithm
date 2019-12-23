# -*- coding: utf-8 -*-

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next
            return item

    def is_empty(self):
        return self.head is None

"""

head = None

第一个元素
Node(1, None)
^

第二个元素
Node(2, node1) Node(1, None)
^

第三个元素
Node(3, ->) Node(2, ->) Node(1, None)
^

"""
