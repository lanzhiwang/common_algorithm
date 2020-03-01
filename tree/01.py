#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
初始化二叉树

         1
        / \
      2    3
     / \  / \
    4  5  6  7

深度遍历的三种情况

二叉树 先序(前序)遍历 -> 打印、左子树、右子树
1 2 4 5 3 6 7

二叉树 中序遍历 -> 左子树、打印、右子树
4 2 5 1 6 3 7

二叉树 后序遍历 -> 左子树、右子树、打印
4 5 2 6 7 3 1

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


r"""
         1
        / \
      2    3
     / \  / \
    4  5  6  7

二叉树 先序(前序)遍历 -> 打印、左子树、右子树
1 2 4 5 3 6 7

before_traversal(1)
    before_traversal(2)  return [2, 4, 5]
    before_traversal(3)  return [3, 6, 7]
    return [1, 2, 4, 5, 3, 6, 7]

before_traversal(2)
    before_traversal(4)  return [4]
    before_traversal(5)  return [5]
    return [2, 4, 5]

before_traversal(3)
    before_traversal(6)  return [6]
    before_traversal(7)  return [7]
    return [3, 6, 7]

before_traversal(4)
    return [4]

before_traversal(5)
    return [5]

before_traversal(6)
    return [6]

before_traversal(7)
    return [7]

"""

# 先序(前序)遍历
def before_traversal(node):
    result = []
    result.append(node.value)
    if node.left is not None:
        result.extend(before_traversal(node.left))
    if node.right is not None:
        result.extend(before_traversal(node.right))
    return result

print('先序(前序)遍历')
print(before_traversal(root))


r"""
         1
        / \
      2    3
     / \  / \
    4  5  6  7

二叉树 中序遍历 -> 左子树、打印、右子树
4 2 5 1 6 3 7

middle_traversal(1)
    middle_traversal(2)  return [4, 2, 5]
    ...
    middle_traversal(3)  return [6, 3, 7]
    return [4, 2, 5, 1, 6, 3, 7]

middle_traversal(2)
    middle_traversal(4)  return [4]
    ...
    middle_traversal(5)  return [5]
    return [4, 2, 5]

middle_traversal(3)
    middle_traversal(6)  return [6]
    ...
    middle_traversal(7)  return [7]
    return [6, 3, 7]

middle_traversal(4)
    return [4]

middle_traversal(5)
    return [5]

middle_traversal(6)
    return [6]

middle_traversal(7)
    return [7]
"""


# 中序遍历
def middle_traversal(node):
    result = []
    if node.left is not None:
        result.extend(middle_traversal(node.left))
    result.append(node.value)
    if node.right is not None:
        result.extend(middle_traversal(node.right))
    return result

print('中序遍历')
print(middle_traversal(root))

r"""
         1
        / \
      2    3
     / \  / \
    4  5  6  7

二叉树 后序遍历 -> 左子树、右子树、打印
4 5 2 6 7 3 1

after_traversal(1)
    after_traversal(2)  return [4, 5, 2]
    after_traversal(3)  return [6, 7, 3]
    return [4, 5, 2, 6, 7, 3, 1]

after_traversal(2)
    after_traversal(4)  return [4]
    after_traversal(5)  return [5]
    return [4, 5, 2]

after_traversal(3)
    after_traversal(6)  return [6]
    after_traversal(7)  return [7]
    return [6, 7, 3]

after_traversal(4)
    return [4]

after_traversal(5)
    return [5]

after_traversal(6)
    return [6]

after_traversal(7)
    return [7]

"""

# 后序遍历
def after_traversal(node):
    result = []
    if node.left is not None:
        result.extend(after_traversal(node.left))
    if node.right is not None:
        result.extend(after_traversal(node.right))
    result.append(node.value)
    return result


print('后序遍历')
print(after_traversal(root))
