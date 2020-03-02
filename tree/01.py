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

preorder_traverse(1)
    preorder_traverse(2)  return [2, 4, 5]
    preorder_traverse(3)  return [3, 6, 7]
    return [1, 2, 4, 5, 3, 6, 7]

preorder_traverse(2)
    preorder_traverse(4)  return [4]
    preorder_traverse(5)  return [5]
    return [2, 4, 5]

preorder_traverse(3)
    preorder_traverse(6)  return [6]
    preorder_traverse(7)  return [7]
    return [3, 6, 7]

preorder_traverse(4)
    return [4]

preorder_traverse(5)
    return [5]

preorder_traverse(6)
    return [6]

preorder_traverse(7)
    return [7]

"""

# 先序(前序)遍历
def preorder_traverse(node):
    result = []
    result.append(node.value)
    if node.left is not None:
        result.extend(preorder_traverse(node.left))
    if node.right is not None:
        result.extend(preorder_traverse(node.right))
    return result

print('先序(前序)遍历')
print(preorder_traverse(root))


r"""
         1
        / \
      2    3
     / \  / \
    4  5  6  7

二叉树 中序遍历 -> 左子树、打印、右子树
4 2 5 1 6 3 7

inorder_traverse(1)
    inorder_traverse(2)  return [4, 2, 5]
    ...
    inorder_traverse(3)  return [6, 3, 7]
    return [4, 2, 5, 1, 6, 3, 7]

inorder_traverse(2)
    inorder_traverse(4)  return [4]
    ...
    inorder_traverse(5)  return [5]
    return [4, 2, 5]

inorder_traverse(3)
    inorder_traverse(6)  return [6]
    ...
    inorder_traverse(7)  return [7]
    return [6, 3, 7]

inorder_traverse(4)
    return [4]

inorder_traverse(5)
    return [5]

inorder_traverse(6)
    return [6]

inorder_traverse(7)
    return [7]
"""


# 中序遍历
def inorder_traverse(node):
    result = []
    if node.left is not None:
        result.extend(inorder_traverse(node.left))
    result.append(node.value)
    if node.right is not None:
        result.extend(inorder_traverse(node.right))
    return result

print('中序遍历')
print(inorder_traverse(root))

r"""
         1
        / \
      2    3
     / \  / \
    4  5  6  7

二叉树 后序遍历 -> 左子树、右子树、打印
4 5 2 6 7 3 1

postorder_traverse(1)
    postorder_traverse(2)  return [4, 5, 2]
    postorder_traverse(3)  return [6, 7, 3]
    return [4, 5, 2, 6, 7, 3, 1]

postorder_traverse(2)
    postorder_traverse(4)  return [4]
    postorder_traverse(5)  return [5]
    return [4, 5, 2]

postorder_traverse(3)
    postorder_traverse(6)  return [6]
    postorder_traverse(7)  return [7]
    return [6, 7, 3]

postorder_traverse(4)
    return [4]

postorder_traverse(5)
    return [5]

postorder_traverse(6)
    return [6]

postorder_traverse(7)
    return [7]

"""

# 后序遍历
def postorder_traverse(node):
    result = []
    if node.left is not None:
        result.extend(postorder_traverse(node.left))
    if node.right is not None:
        result.extend(postorder_traverse(node.right))
    result.append(node.value)
    return result


print('后序遍历')
print(postorder_traverse(root))
