#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, inspect

'''
构建搜索二叉树

中序遍历 搜索二叉树

判断某个值是否存在

获得最大值和最小值

删除节点
https://blog.csdn.net/zxnsirius/article/details/52131433

'''


class Node:

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

    def getNode(self, label):
        curr_node = None
        if not self.empty():
            curr_node = self.getRoot()
            while (curr_node is not None) and (curr_node.getLabel() != label):
                if label < curr_node.getLabel():
                    curr_node = curr_node.getLeft()
                else:
                    curr_node = curr_node.getRight()
        return curr_node

    def getMax(self, root=None):
        if root is not None:
            curr_node = root
        else:
            curr_node = self.getRoot()

        if not self.empty():
            while curr_node.getRight() is not None:
                curr_node = curr_node.getRight()

        return curr_node

    def getMin(self, root=None):
        if root is not None:
            curr_node = root
        else:
            curr_node = self.getRoot()

        if not self.empty():
            while curr_node.getLeft() is not None:
                curr_node = curr_node.getLeft()

        return curr_node

    def empty(self):
        if self.root is None:
            return True
        return False

    def getRoot(self):
        return self.root

    def delete(self, label):
        if not self.empty():
            node = self.getNode(label)
            if node is not None:
                if node.getLeft() is None and node.getRight() is None:
                    self.__reassignNodes(node, None)
                    node = None

                elif node.getLeft() is None and node.getRight() is not None:
                    self.__reassignNodes(node, node.getRight())

                elif node.getLeft() is not None and node.getRight() is None:
                    self.__reassignNodes(node, node.getLeft())

                else:
                    tmpNode = self.getMax(node.getLeft())
                    self.delete(tmpNode.getLabel())
                    node.setLabel(tmpNode.getLabel())

    def __reassignNodes(self, node, newChildren):
        if newChildren is not None:
            newChildren.setParent(node.getParent())

        if node.getParent() is not None:
            if self.__isRightChildren(node):
                node.getParent().setRight(newChildren)
            else:
                node.getParent().setLeft(newChildren)

    def __isRightChildren(self, node):
        if node == node.getParent().getRight():
            return True
        return False

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

    print(t.__str__())  # 8 3 1 6 4 7 10 14 13

    if t.getNode(6) is not None:
        print("The label 6 exists")
    else:
        print("The label 6 doesn't exist")

    if t.getNode(-1) is not None:
        print("The label -1 exists")
    else:
        print("The label -1 doesn't exist")

    if not t.empty():
        print(("Max Value: ", t.getMax().getLabel()))
        print(("Min Value: ", t.getMin().getLabel()))

    t.delete(13)
    t.delete(10)
    t.delete(8)
    t.delete(3)
    t.delete(6)
    t.delete(14)

    print(t.__str__())  # 7 1 4


if __name__ == "__main__":
    testBinarySearchTree()
