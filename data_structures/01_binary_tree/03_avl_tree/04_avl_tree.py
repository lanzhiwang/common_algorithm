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
######################################################
del_node(node=root, data)
    del_node(node=root.left, data)
    del_node(node=root.right, data)  # return node
    node.set_right(node)
    # rotation
    # height
    return node

######################################################
del_node(node=root.left, data)
    del_node(node=root.left.left, data)
    del_node(node=root.left.right, data)

del_node(node=root.right, data)
    del_node(node=root.right.left, data)
    del_node(node=root.right.right, data)  # return node
    node.set_right(node)
    # rotation
    # height
    return node

######################################################

del_node(node=root.left.left, data)
    del_node(node=root.left.left.left, data)
    del_node(node=root.left.left.right, data)

del_node(node=root.left.right, data)
    del_node(node=root.left.right.left, data)
    del_node(node=root.left.right.right, data)

del_node(node=root.right.left, data)
    del_node(node=root.right.left.left, data)
    del_node(node=root.right.left.right, data)

del_node(node=root.right.right, data)
    del_node(node=root.right.right.left, data)
    del_node(node=root.right.right.right, data)  # return node
    node.set_right(node)
    # rotation
    # height
    return node


######################################################

del_node(node=root.left.left.left, data)
del_node(node=root.left.left.right, data)

del_node(node=root.left.right.left, data)
del_node(node=root.left.right.right, data)

del_node(node=root.right.left.left, data)
del_node(node=root.right.left.right, data)

del_node(node=root.right.right.left, data)
del_node(node=root.right.right.right, data)
left     | right
---------|---------
not None | not None
not None | None
None     | not None
None     | None


left     | right
---------|---------
not None | not None

temp_data = get_left_most(node.get_right())
node.set_data(temp_data)
node.set_right(del_node(node.get_right(), temp_data))  # 最后左右节点都肯定为 None
node.set_right(node)
# rotation
# height
return node

left     | right
---------|---------
not None | None

node = node.get_left()


left     | right
---------|---------
None     | not None

node = node.get_right()


left     | right
---------|---------
None     | None

node = node.get_right() = None
return node

"""

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
