#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from queue import Queue

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
    def __init__(self, value, parent):
        self.value = value
        self.left = None
        self.right = None
        #Added in order to delete a node easier
        self.parent = parent

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.label = value

    def get_left(self):
        return self.left

    def set_left(self, left):
        self.left = left

    def get_right(self):
        return self.right

    def set_right(self, right):
        self.right = right

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def __str__(self):
        if (self.get_left() is not None) and (self.get_right() is not None):
            return 'value: %s, left: %s, right: %s' % (
                self.get_value(), self.get_left().get_value(), self.get_right().get_value())

        elif (self.get_left() is None) and (self.get_right() is not None):
            return 'label: %s, left: %s, right: %s' % (
                self.get_value(), None, self.get_right().get_value())

        elif (self.get_left() is not None) and (self.get_right() is None):
            return 'label: %s, left: %s, right: %s' % (
                self.get_value(), self.get_left().get_value(), None)

        else:
            return 'label: %s, left: %s, right: %s' % (
                self.get_value(), None, None)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value, None)

        if self.empty():
            self.root = new_node
        else:
            curr_node = self.root
            while curr_node is not None:
                parent_node = curr_node
                if new_node.get_value() < curr_node.get_value():
                    curr_node = curr_node.get_left()
                else:
                    curr_node = curr_node.get_right()

            if new_node.get_value() < parent_node.get_value():
                parent_node.set_left(new_node)
            else:
                parent_node.set_right(new_node)
            new_node.set_parent(parent_node)

    def empty(self):
        if self.root is None:
            return True
        return False

    def get_root(self):
        return self.root

    # 先序(前序)遍历
    def __InOrderTraversal(self, node=None):
        if node is None:
            node = self.get_root()
        node_list = []
        node_list.append(node)
        if node.get_left() is not None:
            node_list.extend(self.__InOrderTraversal(node.get_left()))
        if node.get_right() is not None:
            node_list.extend(self.__InOrderTraversal(node.get_right()))
        return node_list

    # 中序遍历
    def middle_traversal(self, node=None):
        if node is None:
            node = self.get_root()
        node_list = []
        if node.get_left() is not None:
            node_list.extend(self.middle_traversal(node.get_left()))
        node_list.append(node.get_value())
        if node.get_right() is not None:
            node_list.extend(self.middle_traversal(node.get_right()))
        return node_list


    # 广度遍历
    def breadth_traversal(self, node=None):
        if node is None:
            node = self.get_root()
        node_list = []
        queue = Queue()
        queue.put(node)
        while not queue.empty():
            val = queue.get()
            node_list.append(val.get_value())
            if val.get_left() is not None:
                queue.put(val.get_left())
            if val.get_right() is not None:
                queue.put(val.get_right())
        return node_list

    def __str__(self):
        node_list = self.__InOrderTraversal(self.root)
        str = ""
        for x in node_list:
            str = str + " " + x.get_value().__str__()
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
    t = BinarySearchTree()
    for i in [8, 3, 6, 1, 10, 14, 13, 4, 7]:
        t.insert(i)

    #Prints all the elements of the list in order traversal
    print(t)  # 8 3 1 6 4 7 10 14 13

    print(t.breadth_traversal())  # [8, 3, 10, 1, 6, 14, 4, 7, 13]
    print(t.middle_traversal())  # [1, 3, 4, 6, 7, 8, 10, 13, 14]


if __name__ == "__main__":
    testBinarySearchTree()
