#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Node(object):
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
    else:
        return node.get_height()


def get_max(a, b):
    return a if a >= b else b


def set_height(node):
    node.set_height(get_max(get_height(node.get_left()), get_height(node.get_right())) + 1)


def get_left_most(node):
    if node is None:
        return None
    temp = node
    while temp is not None and temp.get_left() is not None:
        temp = temp.get_left()
    return temp


def left_rotation(node):
    r"""
        A         B
       /         / \
      B    =>   UB  A
     /
    UB
    """
    ret = node.get_left()
    node.set_left(ret.get_right())
    ret.set_right(node)
    set_height(node)
    set_height(ret)
    return ret


def right_rotation(node):
    r"""
    A            B
     \          / \
      B    =>  A  UB
       \
        UB
    """
    ret = node.get_right()
    node.set_right(ret.get_left())
    ret.set_left(node)
    set_height(node)
    set_height(ret)
    return ret


def lr_rotation(node):
    r"""
    A       A           UB
     \       \         / \
      B  =>  UB   =>  A   B
     /         \
    UB          B
    """
    node.set_right(left_rotation(node.get_right()))
    return right_rotation(node)


def rl_rotation(node):
    r"""
      A          A       UB
     /          /       / \
    B    =>   UB   =>  B   A
     \       /
      UB    B
    """
    node.set_left(right_rotation(node.get_left()))
    return left_rotation(node)


def insert_node(node, data):
    if node is None:
        return Node(data)

    if data < node.get_data():
        temp_node = insert_node(node.get_left(), data)
        node.set_left(temp_node)
        if get_height(node.get_left()) - get_height(node.get_right()) == 2:
            if data < node.get_left().get_data():
                node = left_rotation(node)
            else:
                node = rl_rotation(node)

    elif data > node.get_data():
        temp_node = insert_node(node.get_right(), data)
        node.set_right(temp_node)
        if get_height(node.get_right()) - get_height(node.get_left()) == 2:
            if data < node.get_right().get_data():
                node = lr_rotation(node)
            else:
                node = right_rotation(node)

    set_height(node)
    return node


def del_node(node, data):
    if node is None:
        return None

    if data == node.get_data():
        """
        left     | right
        ---------|---------
        not None | not None
        not None | None
        None     | not None
        None     | None
        """
        if node.get_left() is not None and node.get_right() is not None:
            temp_node = get_left_most(node.get_right())
            node.set_data(temp_node.get_data())
            node.set_right(del_node(node.get_right(), temp_node.get_data()))
        elif node.get_left() is not None and node.get_right() is None:
            node = node.get_left()
        elif node.get_left() is None and node.get_right() is not None:
            node = node.get_right()
        else:
            node = None
    elif data < node.get_data():
        node.set_left(del_node(node.get_left(), data))
    elif data > node.get_data():
        node.set_right(del_node(node.get_right(), data))

    if node is None:
        return None

    if get_height(node.get_left()) - get_height(node.get_right()) == 2:
        if get_height(node.get_left().get_left()) > get_height(node.get_left().get_right()):
            node = left_rotation(node)
        else:
            node = rl_rotation(node)
    elif get_height(node.get_left()) - get_height(node.get_right()) == -2:
        if get_height(node.get_right().get_right()) > get_height(node.get_right().get_left()):
            node = right_rotation(node)
        else:
            node = lr_rotation(node)

    set_height(node)
    return node


class AVLTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = insert_node(self.root, data)

    def del_node(self, data):
        if self.root is None:
            return None
        self.root = del_node(self.root, data)


if __name__ == '__main__':
    t = AVLTree()

    ll = [4, 2, 7, 6, 3, 5, 8, 0, 9, 1]
    print(ll)
    for i in ll:
        t.insert(i)

    print()
    print()
    print()

    for i in ll:
        t.del_node(i)
