#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
初始化二叉树

         1
        / \
      2    3
     / \  / \
    4  5  6 7

深度遍历的三种情况

二叉树 先序(前序)遍历 -> 打印、左子树、右子树
1 2 4 5 3 6 7

二叉树 中序遍历 -> 左子树、打印、右子树
4 2 5 1 6 3 7

二叉树 后序遍历 -> 左子树、右子树、打印
4 5 2 6 7 3 1

            1-0
         /       \
       2-1      3-2
      /   \     /  \
    4-3  5-4  6-5 7-6

"""

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


# 先序(前序)遍历
def before_traversal(nodes, node):
    print(node.value)
    if node.left != -1:
        before_traversal(nodes, nodes[node.left])
    if node.right != -1:
        before_traversal(nodes, nodes[node.right])


# 中序遍历
def middle_traversal(nodes, node):
    if node.left != -1:
        middle_traversal(nodes, nodes[node.left])
    print(node.value)
    if node.right != -1:
        middle_traversal(nodes, nodes[node.right])


# 后序遍历
def after_traversal(nodes, node):
    if node.left != -1:
        after_traversal(nodes, nodes[node.left])
    if node.right != -1:
        after_traversal(nodes, nodes[node.right])
    print(node.value)


print('先序(前序)遍历')
before_traversal(nodes, node0)
print('中序遍历')
middle_traversal(nodes, node0)
print('后序遍历')
after_traversal(nodes, node0)

