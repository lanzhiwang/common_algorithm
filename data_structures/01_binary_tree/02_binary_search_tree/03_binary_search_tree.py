#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, inspect

'''
构建搜索二叉树

中序遍历 搜索二叉树

判断某个值是否存在

获得最大值和最小值
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
            if not self.empty():
                curr_node = self.getRoot()
                while curr_node.getRight() is not None:
                    curr_node = curr_node.getRight()
        return curr_node

    def getMin(self, root=None):
        if root is not None:
            curr_node = root
        else:
            if not self.empty():
                curr_node = self.getRoot()
                while curr_node.getLeft() is not None:
                    curr_node = curr_node.getLeft()
        return curr_node

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
def display(tree): #In Order traversal of the tree

    if tree is None:
        return

    if tree.getLeft() is not None:
        display(tree.getLeft())

    print(tree.getLabel())

    if tree.getRight() is not None:
        display(tree.getRight())

    return


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

    if (t.getNode(6) is not None):
        print("The label 6 exists")
    else:
        print("The label 6 doesn't exist")

    if (t.getNode(-1) is not None):
        print("The label -1 exists")
    else:
        print("The label -1 doesn't exist")

    if not t.empty():
        print(("Max Value: ", t.getMax().getLabel()))
        print(("Min Value: ", t.getMin().getLabel()))



if __name__ == "__main__":
    testBinarySearchTree()
