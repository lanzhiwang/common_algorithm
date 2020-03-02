# -*- coding: utf-8 -*-


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
    ret = node.get_left()
    node.set_left(ret.get_right())
    ret.set_right(node)
    h1 = my_max(get_height(node.get_left()), get_height(node.get_right())) + 1
    node.set_height(h1)
    h2 = my_max(get_height(ret.get_left()), get_height(ret.get_right())) + 1
    ret.set_height(h2)
    return ret


def right_rotation(node):
    ret = node.get_right()
    node.set_right(ret.get_left())
    ret.set_left(node)
    h1 = my_max(get_height(node.get_left()), get_height(node.get_right())) + 1
    node.set_height(h1)
    h2 = my_max(get_height(ret.get_left()), get_height(ret.get_right())) + 1
    ret.set_height(h2)
    return ret


def rl_rotation(node):
    node.set_left(right_rotation(node.get_left()))
    return left_rotation(node)


def lr_rotation(node):
    node.set_right(left_rotation(node.get_right()))
    return right_rotation(node)


"""
###################################################
insert_node(node=root, data)
    insert_node(node=root.left, data)  # return
        node.set_left(return)
    insert_node(node=root.right, data)

###################################################
insert_node(node=root.left, data)
    insert_node(node=root.left.left, data)  # return
        node.set_left(return)
        if get_height(root.get_left()) - get_height(root.get_right()) == 2
            node = rotation(node)
        h1 = my_max(get_height(node.get_right()), get_height(node.get_left())) + 1
        node.set_height(h1)
        return node

    insert_node(node=root.left.right, data)

insert_node(node=root.right, data)
    insert_node(node=root.right.left, data)
    insert_node(node=root.right.right, data)

###################################################
insert_node(node=root.left.left, data)
    insert_node(node=root.left.left.left, data)  # return Node(data)
        node.set_left(Node(data))
        if get_height(root.get_left()) - get_height(root.get_right()) == 2
            pass
        h1 = my_max(get_height(node.get_right()), get_height(node.get_left())) + 1
        node.set_height(h1)
        return node

    insert_node(node=root.left.left.right, data)  # return Node(data)
        node.set_right(Node(data))
        if get_height(root.get_left()) - get_height(root.get_right()) == -2
            pass
        h1 = my_max(get_height(node.get_right()), get_height(node.get_left())) + 1
        node.set_height(h1)
        return node

insert_node(node=root.left.right, data)
    insert_node(node=root.left.right.left, data)  # return Node(data)
    insert_node(node=root.left.right.right, data)  # return Node(data)

insert_node(node=root.right.left, data)
    insert_node(node=root.right.left.left, data)  # return Node(data)
    insert_node(node=root.right.left.right, data)  # return Node(data)

insert_node(node=root.right.right, data)
    insert_node(node=root.right.right.left, data)  # return Node(data)
    insert_node(node=root.right.right.right, data)  # return Node(data)

###################################################
insert_node(node=root.left.left.left, data)
    return Node(data)
insert_node(node=root.left.left.right, data)
    return Node(data)
insert_node(node=root.left.right.left, data)
    return Node(data)
insert_node(node=root.left.right.right, data)
    return Node(data)
insert_node(node=root.right.left.left, data)
    return Node(data)
insert_node(node=root.right.left.right, data)
    return Node(data)
insert_node(node=root.right.right.left, data)
    return Node(data)
insert_node(node=root.right.right.right, data)
    return Node(data)

"""

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
