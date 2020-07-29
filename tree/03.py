#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
初始化二叉树

         1
        / \
      2    3
     / \  / \
    4  5  6  7

将二叉树改造成带父节点信息的二叉树

add_parent_info(1, None)
    NodeWithParent(1)
    add_parent_info(2, NodeWithParent(1))
    add_parent_info(3, NodeWithParent(1))

add_parent_info(2, NodeWithParent(1))
    NodeWithParent(2)
    add_parent_info(4, NodeWithParent(2))
    add_parent_info(5, NodeWithParent(2))

add_parent_info(3, NodeWithParent(1))
    NodeWithParent(3)
    add_parent_info(6, NodeWithParent(3))
    add_parent_info(7, NodeWithParent(3))

add_parent_info(4, NodeWithParent(2))
    return NodeWithParent(4)

add_parent_info(5, NodeWithParent(2))
    return NodeWithParent(5)

add_parent_info(6, NodeWithParent(3))
    return NodeWithParent(6)

add_parent_info(7, NodeWithParent(3))
    return NodeWithParent(7)



"""


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


class NodeWithParent(object):
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def add_parent_info(node, parent=None):
    if node is None:
        return None

    new_node = NodeWithParent(node.value, None, None, parent)

    if node.left is not None:
        new_node.left = add_parent_info(node.left, new_node)

    if node.right is not None:
        new_node.right = add_parent_info(node.right, new_node)

    return new_node

new_root = add_parent_info(root)
print(new_root.value, new_root.left.value, new_root.right.value, new_root.parent)
print(new_root.left.value, new_root.left.left.value, new_root.left.right.value, new_root.left.parent.value)
print(new_root.right.value, new_root.right.left.value, new_root.right.right.value, new_root.right.parent.value)

print(new_root.left.left.value, new_root.left.left.left, new_root.left.left.right, new_root.left.left.parent.value)
print(new_root.left.right.value, new_root.left.right.left, new_root.left.right.right, new_root.left.right.parent.value)

print(new_root.right.left.value, new_root.right.left.left, new_root.right.left.right, new_root.right.left.parent.value)
print(new_root.right.right.value, new_root.right.right.left, new_root.right.right.right, new_root.right.right.parent.value)


