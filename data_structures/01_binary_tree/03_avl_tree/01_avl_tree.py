# -*- coding: utf-8 -*-
"""
AVL 树的特性让二叉搜索树的节点实现平衡(balance)，AVL树要求: 任一节点的左子树深度和右子树深度相差不超过1
avl 平衡二叉树使用到的相关辅助对象和函数

"""

class MyQueue():
    def __init__(self):
        self.data = []
        self.head = 0
        self.tail = 0

    def push(self, data):
        self.data.append(data)
        self.tail += 1

    def pop(self):
        ret = self.data[self.head]
        self.head += 1
        return ret

    def count(self):
        return self.tail - self.head

    def is_empty(self):
        return self.head == self.tail

    def print_queue(self):
        print(self.data)
        print("**************")
        print(self.data[self.head:self.tail])


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_height(self):
        return self.height

    def set_data(self, data):
        self.data = data

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

    def set_height(self, height):
        self.height = height


def get_height(node):
    if node is None:
        return 0
    return node.get_height()


def my_max(a, b):
    if a > b:
        return a
    return b


def get_right_most(node):
    while node.get_right() is not None:
        node = node.get_right()
    return node.get_data()


def get_left_most(node):
    while node.get_left() is not None:
        node = node.get_left()
    return node.get_data()
