#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
初始化二叉树

         1
        / \
      2    3
     / \  / \
    4  5  6  7
         / \
        8   9
找路径
find_path(1, 8)、find_path(1, 1)、find_path(1, 2)、find_path(1, 6)

find_path(1, 8)
    find_path(2, 8) return None
    find_path(3, 8) return [3, 6, 8]
    return [1, 3, 6, 8]

find_path(2, 8)
    find_path(4, 8) return None
    find_path(5, 8) return None
    return None

find_path(3, 8)
    find_path(6, 8) return [6, 8]
    find_path(7, 8) return None
    return [3, 6, 8]

find_path(4, 8)
    return None

find_path(5, 8)
    return None

find_path(6, 8)
    find_path(8, 8) return 8
    find_path(9, 8) return None
    return [6, 8]

find_path(7, 8)
    return None

find_path(8, 8)
    return [8]

find_path(9, 8)
    return None

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
root.right.left.left = Node(8)
root.right.left.right = Node(9)

def find_path(node, target):
    if node.value == target.value:
        return [node.value]
    else:
        left_result = None
        right_result = None
        if node.left is None and node.right is None:
            return None
        elif node.left is not None and node.right is None:
            left_result = find_path(node.left, target)
        elif node.left is None and node.right is not None:
            right_result = find_path(node.right, target)
        else:
            left_result = find_path(node.left, target)
            right_result = find_path(node.right, target)

        if left_result is not None and right_result is None:
            left_result.insert(0, node.value)
            return left_result
        elif left_result is None and right_result is not None:
            right_result.insert(0, node.value)
            return right_result
        else:
            return None

print(find_path(root, Node(1)))
print(find_path(root, Node(2)))
print(find_path(root, Node(6)))
print(find_path(root, Node(8)))
print(find_path(root, Node(10)))
