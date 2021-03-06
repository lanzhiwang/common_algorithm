# -*- coding: utf-8 -*-
from queue import Queue
import random

class MyQueue():
    def __init__(self):
        self.data = []
        self.head = 0
        self.tail = 0

    def push(self, data):
        self.data.append(data)
        self.tail += 1

    def pop(self):
        ret = self.data[self.head]
        self.head += 1
        return ret

    def count(self):
        return self.tail - self.head

    def is_empty(self):
        return self.head == self.tail

    def print_queue(self):
        print(self.data)
        print("**************")
        print(self.data[self.head:self.tail])


class Node:
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
    return node.get_height()


def my_max(a, b):
    if a > b:
        return a
    return b


def get_right_most(node):
    while node.get_right() is not None:
        node = node.get_right()
    return node.get_data()


def get_left_most(node):
    while node.get_left() is not None:
        node = node.get_left()
    return node.get_data()


def left_rotation(node):
    r'''
    需要左旋转的情况：左子树的高度 - 右子树的高度 = 2
    左子树的高度 | 右子树的高度
    ---------- | ----------
    2             0
    3             1
    4             2
    ...

            A              B
           /              / \
          B       -->    UB  A
         /
        UB


        7-2 node         6-2            6-2
        /               /  \            /  \
      6-2 ret          5-1 7-2         5-1 7-1
      /
     5-1

    #######################################################

            A                      B
           / \                    / \
          B   C                  Bl  A
         / \       -->          /   / \
        Bl  Br                 UB Br  C
       /
     UB


            A-3                         B-3                      B-3
           /   \                       /    \                   /    \
          B-3   C-1                  Bl-2   A-3                Bl-2   A-2
         /   \            -->        /      / \                /      / \
        Bl-2 Br-1                 UB-1   Br-1  C-1           UB-1   Br-1  C-1
       /
     UB-1

    '''
    ret = node.get_left()
    node.set_left(ret.get_right())
    ret.set_right(node)
    h1 = my_max(get_height(node.get_left()), get_height(node.get_right())) + 1
    node.set_height(h1)
    h2 = my_max(get_height(ret.get_left()), get_height(ret.get_right())) + 1
    ret.set_height(h2)
    return ret


def right_rotation(node):
    r'''
    需要右旋转的情况：左子树的高度 - 右子树的高度 = -2
    左子树的高度 | 右子树的高度
    ---------- | ----------
    0            2
    1            3
    2            4
    ...

     A                      C
      \                    / \
       C       -->        A   Cr
        \
         Cr

    7-2 node           8-2             8-2
      \               /   \            / \
      8-2 ret        7-2  9-1        7-1  9-1
        \
        9-1

    #######################################################

        A                      C
       / \                    / \
      B   C                  A   Cr
         / \       -->      / \   \
        Cl  Cr             B  Cl  UB
             \
             UB


         A-3                         C-3                   C-3
       /    \                       /    \                /   \
      B-1   C-3                    A-3   Cr-2           A-2    Cr-2
            / \       -->         /  \     \           /  \     \
         Cl-1  Cr-2             B-1  Cl-1  UB-1      B-1  Cl-1  UB-1
                \
                UB-1

    '''
    ret = node.get_right()
    node.set_right(ret.get_left())
    ret.set_left(node)
    h1 = my_max(get_height(node.get_left()), get_height(node.get_right())) + 1
    node.set_height(h1)
    h2 = my_max(get_height(ret.get_left()), get_height(ret.get_right())) + 1
    ret.set_height(h2)
    return ret


def rl_rotation(node):
    r'''
    需要先右旋转，再左旋转的情况：左子树的高度 - 右子树的高度 = 2
    左子树的高度 | 右子树的高度
    ---------- | ----------
    2             0
    3             1
    4             2
    ...

      A                 A          UB
     /                 /          /  \
    B       -->       UB   -->   B    A
     \               /
      UB            B


      5-2               5-2         4-2
     /                 /            /  \
    3-2       -->     4-2   -->    3-1 5-1
     \               /
      4-1           3-1

    #######################################################

            A              A                    Br
           / \            / \                  /  \
          B   C    RR    Br  C       LR       B    A
         / \       -->  /  \         -->    /     / \
        Bl  Br         B   UB              Bl    UB  C
             \        /
             UB     Bl

    RR = rightrotation   LR = leftrotation

              A-3               A-3                       Br-3
             /   \             /   \                   /       \
           B-3   C-1    RR    Br-3  C-1     LR       B-2       A-2
         /    \       -->     /  \         -->        /       /   \
        Bl-1  Br-2          B-2   UB-1              Bl-1    UB-1  C-1
                \            /
                UB-1       Bl-1

    '''
    node.set_left(right_rotation(node.get_left()))
    return left_rotation(node)


def lr_rotation(node):
    r"""
    需要先左旋转，再右旋转的情况：左子树的高度 - 右子树的高度 = -2
    左子树的高度 | 右子树的高度
    ---------- | ----------
    0             2
    1             3
    2             4
    ...

     A            A                  B
      \            \                / \
       C     -->    B     -->      A   C
      /              \
     B                C

     A-2            A-2                   B-2
      \               \                  /   \
       C-2     -->    B-2     -->      A-1   C-1
      /                 \
     B-1                C-1

    #######################################################

        A                   A                    Cl
       / \                 / \                   / \
      B   C               B  Cl                 A   C
         / \    -->          / \    -->        / \   \
        Cl  Cr              UB  C             B  UB  Cr
        /                        \
       UB                        Cr

    UB = unbalanced node

             A-3                        A-3                        Cl-3
            /  \                      /    \                      /     \
         B-1   C-3                   B-1  Cl-3                  A-2     C-2
             /    \    -->                /   \         -->    /   \      \
           Cl-2  Cr-1                   UB-1  C-2             B-1  UB-1  Cr-1
           /                                    \
         UB-1                                  Cr-1

    """
    node.set_right(left_rotation(node.get_right()))
    return right_rotation(node)


def insert_node(node, data):
    if node is None:
        return Node(data)

    if data < node.get_data():
        node.set_left(insert_node(node.get_left(), data))
        if get_height(node.get_left()) - get_height(node.get_right()) == 2:
            if data < node.get_left().get_data():
                node = left_rotation(node)
            else:
                node = rl_rotation(node)
    else:
        node.set_right(insert_node(node.get_right(), data))
        if get_height(node.get_right()) - get_height(node.get_left()) == 2:
            if data < node.get_right().get_data():
                node = lr_rotation(node)
            else:
                node = right_rotation(node)

    h1 = my_max(get_height(node.get_right()), get_height(node.get_left())) + 1
    node.set_height(h1)
    return node


def del_node(node, data):
    if data < node.get_data():
        if node.get_left() is None:
            return node
        else:
            node.set_left(del_node(node.get_left(), data))
    elif data > node.get_data():
        if node.get_right() is None:
            return node
        else:
            node.set_right(del_node(node.get_right(), data))
    elif data == node.get_data():
        if node.get_left() is not None and node.get_right() is not None:
            temp_data = get_left_most(node.get_right())
            node.set_data(temp_data)
            node.set_right(del_node(node.get_right(), temp_data))

        elif node.get_left() is not None and node.get_right() is None:
            node = node.get_left()

        elif node.get_left() is None and node.get_right() is not None:
            node = node.get_right()

        elif node.get_left() is None and node.get_right() is None:
            node = None

    if node is None:
        return node

    if get_height(node.get_left()) - get_height(node.get_right()) == 2:
        if get_height(node.get_left().get_left()) > get_height(node.get_left().get_right()):
            node = left_rotation(node)
        else:
            node = rl_rotation(node)
    elif get_height(node.get_right()) - get_height(node.get_left()) == 2:
        if get_height(node.get_right().get_right()) > get_height(node.get_right().get_left()):
            node = right_rotation(node)
        else:
            node = lr_rotation(node)

    height = my_max(get_height(node.get_right()), get_height(node.get_left())) + 1
    node.set_height(height)
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

    def traver_sale(self):
        result = []
        if self.root is not None:
            queue = Queue()
            queue.put(self.root)
            while not queue.empty():
                node = queue.get()
                result.append(node.get_data())

                if node.get_left() is not None:
                    queue.put(node.get_left())

                if node.get_right() is not None:
                    queue.put(node.get_right())
            return result


if __name__ == "__main__":
    t = AVLTree()
    l = list(range(10))
    random.shuffle(l)
    print(l)
    for i in l:
        t.insert(i)
    print(t.traver_sale())
    print()

    random.shuffle(l)
    print(l)
    for i in l:
        t.del_node(i)
    print(t.traver_sale())
    print()
