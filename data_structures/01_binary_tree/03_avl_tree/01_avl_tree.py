# -*- coding: utf-8 -*-
"""

"""


class my_queue:
    def __init__(self):
        self.data = []
        self.head = 0
        self.tail = 0

    """
    push(1)
    push(2)
    push(3)
    
    [1, 2, 3]
    head=0   tail=3
    """
    def push(self, data):
        self.data.append(data)
        self.tail = self.tail + 1

    """
    [1, 2, 3]
    head=0   tail=3
    
    [1, 2, 3]
    head=1 tail=3
    """
    def pop(self):
        ret = self.data[self.head]
        self.head = self.head + 1
        return ret

    """
    [1, 2, 3]
    head=1 tail=3
    
    tail-head = 2
    """
    def count(self):
        return self.tail - self.head

    def isEmpty(self):
        return self.head == self.tail

    def print(self):
        print(self.data)
        print("**************")
        print(self.data[self.head:self.tail])


class my_node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def getdata(self):
        return self.data

    def getleft(self):
        return self.left

    def getright(self):
        return self.right

    def getheight(self):
        return self.height

    def setdata(self, data):
        self.data = data
        return

    def setleft(self, node):
        self.left = node
        return

    def setright(self, node):
        self.right = node
        return

    def setheight(self, height):
        self.height = height
        return


def getheight(node):
    if node is None:
        return 0
    return node.getheight()


def my_max(a, b):
    if a > b:
        return a
    return b


def getRightMost(root):
    while root.getright() is not None:
        root = root.getright()
    return root.getdata()


def getLeftMost(root):
    while root.getleft() is not None:
        root = root.getleft()
    return root.getdata()
