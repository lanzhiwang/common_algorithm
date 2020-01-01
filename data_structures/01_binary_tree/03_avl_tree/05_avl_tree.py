# -*- coding: utf-8 -*-
"""

"""

import math
import random


def getheight(node):
    pass


def insert_node(node, data):
    pass


def del_node(root,data):
    pass


class my_queue:
    pass


class AVLtree:
    def __init__(self):
        self.root = None

    def getheight(self):
        return getheight(self.root)

    def insert(self, data):
        print("insert:" + str(data))
        self.root = insert_node(self.root, data)

    def del_node(self, data):
        print("delete:" + str(data))
        if self.root is None:
            print("Tree is empty!")
            return
        self.root = del_node(self.root, data)

    def traversale(self):
        q = my_queue()
        q.push(self.root)
        layer = self.getheight()
        if layer == 0:
            return
        cnt = 0
        while not q.isEmpty():
            node = q.pop()
            space = " " * int(math.pow(2, layer - 1))
            print(space, end="")
            if node is None:
                print("*", end="")
                q.push(None)
                q.push(None)
            else:
                print(node.getdata(), end="")
                q.push(node.getleft())
                q.push(node.getright())
            print(space, end="")
            cnt = cnt + 1
            for i in range(100):
                if cnt == math.pow(2, i) - 1:
                    layer = layer - 1
                    if layer == 0:
                        print()
                        print("*************************************")
                        return
                    print()
                    break
        print()
        print("*************************************")
        return

    def test(self):
        getheight(None)
        print("****")
        self.getheight()


if __name__ == "__main__":
    t = AVLtree()
    t.traversale()
    l = list(range(10))
    random.shuffle(l)
    print(l)
    for i in l:
        t.insert(i)
        t.traversale()

    random.shuffle(l)
    print(l)
    for i in l:
        t.del_node(i)
        t.traversale()
