#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import inspect

'''
二叉查找树（Binary Search Tree），也称有序二叉树（ordered binary tree）,排序二叉树（sorted binary tree），
是指一棵空树或者具有下列性质的二叉树：

若任意结点的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
若任意结点的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
任意结点的左、右子树也分别为二叉查找树。
没有键值相等的结点（no duplicate nodes）。

构建搜索二叉树

中序遍历 搜索二叉树
'''


class Node(object):
    def __init__(self, label, parent):
        self.label = label
        self.left = None
        self.right = None
        #Added in order to delete a node easier
        self.parent = parent

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def __str__(self):
        if (self.getLeft() is not None) and (self.getRight() is not None):
            return 'label: %s, left: %s, right: %s' % (
                self.getLabel(), self.getLeft().getLabel(), self.getRight().getLabel())

        elif (self.getLeft() is None) and (self.getRight() is not None):
            return 'label: %s, left: %s, right: %s' % (
                self.getLabel(), None, self.getRight().getLabel())

        elif (self.getLeft() is not None) and (self.getRight() is None):
            return 'label: %s, left: %s, right: %s' % (
                self.getLabel(), self.getLeft().getLabel(), None)

        else:
            return 'label: %s, left: %s, right: %s' % (
                self.getLabel(), None, None)



class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, label):
        new_node = Node(label, None)

        if self.empty():
            self.root = new_node
        else:
            curr_node = self.root
            while curr_node is not None:
                parent_node = curr_node
                if new_node.getLabel() < curr_node.getLabel():
                    curr_node = curr_node.getLeft()
                else:
                    curr_node = curr_node.getRight()

            if new_node.getLabel() < parent_node.getLabel():
                parent_node.setLeft(new_node)
            else:
                parent_node.setRight(new_node)
            new_node.setParent(parent_node)

    def empty(self):
        if self.root is None:
            return True
        return False

    def getRoot(self):
        return self.root

    def __InOrderTraversal(self, curr_node):
        nodeList = []
        if curr_node is not None:
            nodeList.insert(0, curr_node)
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getLeft())
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getRight())
        return nodeList

    def __str__(self):
        list = self.__InOrderTraversal(self.root)
        str = ""
        for x in list:
            str = str + " " + x.getLabel().__str__()
        return str


"""
中序遍历
"""
# class display(object):
#     def __call__(self, tree):
#         if tree is None:
#             return
#
#         if tree.getLeft() is not None:
#             self.__call__(tree.getLeft())
#
#         print(tree.getLabel())
#
#         if tree.getRight() is not None:
#             self.__call__(tree.getRight())
#
#         return

def display(tree): #In Order traversal of the tree

    if tree is None:
        return

    if tree.getLeft() is not None:
        display(tree.getLeft())

    print(tree.getLabel())

    if tree.getRight() is not None:
        display(tree.getRight())

    return



"""
中序遍历
"""
class display1(object):
    def __call__(self, tree):
        result = []

        if tree is None:
            return result

        left_node = tree.getLeft()
        if left_node is not None:
            result = result + self.__call__(left_node)

        result = result + [tree.getLabel()]

        right_node = tree.getRight()
        if right_node is not None:
            result = result + self.__call__(right_node)

        return result

# def display1(tree): #In Order traversal of the tree
#     result = []
#
#     if tree is None:
#         return result
#
#     left_node = tree.getLeft()
#     if left_node is not None:
#         result = result + display1(left_node)
#
#     result = result + [tree.getLabel()]
#
#     right_node = tree.getRight()
#     if right_node is not None:
#         result = result + display1(right_node)
#
#     return result


def testBinarySearchTree():
    r'''
    Example
                  8
                 / \
                3   10
               / \    \
              1   6    14
                 / \   /
                4   7 13
    '''

    r'''
    Example After Deletion
                  7
                 / \
                1   4

    '''
    t = BinarySearchTree()
    t.insert(8)
    t.insert(3)
    t.insert(6)
    t.insert(1)
    t.insert(10)
    t.insert(14)
    t.insert(13)
    t.insert(4)
    t.insert(7)

    #Prints all the elements of the list in order traversal
    print(t.__str__())  # 8 3 1 6 4 7 10 14 13

    display(t.getRoot())
    print(display1()(t.getRoot()))


if __name__ == "__main__":
    testBinarySearchTree()
