# -*- coding: utf-8 -*-
"""

"""


def my_max(a, b):
    pass


class my_node:
    pass


def getheight(node):
    pass


def leftrotation(node):
    pass


def rlrotation(node):
    pass


def lrrotation(node):
    pass


def rightrotation(node):
    pass


# insert_node(self.root, data)
def insert_node(node, data):
    if node is None:
        return my_node(data)

    left_node = node.getleft()
    right_node = node.getright()
    if data < node.getdata():
        new_node = insert_node(left_node, data)
        node.setleft(new_node)
        if getheight(left_node) - getheight(right_node) == 2:
            if data < left_node.getdata():
                node = leftrotation(node)
            else:
                node = rlrotation(node)
    else:
        new_node = insert_node(right_node, data)
        node.setright(new_node)
        if getheight(right_node) - getheight(left_node) == 2:
            if data < right_node.getdata():
                node = lrrotation(node)
            else:
                node = rightrotation(node)

    h = my_max(getheight(node.getleft()), getheight(node.getright())) + 1
    node.setheight(h)
    return node

"""
[1, 7, 4, 6, 5, 3, 8, 0, 2, 9]


[3, 9, 5, 0, 2, 7, 8, 4, 1, 6]


[6, 2, 3, 1, 5, 0, 4, 9, 7, 8]



[3, 6, 4, 2, 0, 9, 8, 5, 1, 7]



[4, 2, 7, 6, 3, 5, 8, 0, 9, 1]
insert:4
 4
*************************************
insert:2
  4
 2  *
*************************************
insert:7
  4
 2  7
*************************************
insert:6
    4
  2    7
 *  *  6  *
*************************************
insert:3
    4
  2    7
 *  3  6  *
*************************************
insert:5
left rotation node: 7
    4
  2    6
 *  3  5  7
*************************************
insert:8
        4
    2        6
  *    3    5    7
 *  *  *  *  *  *  *  8
*************************************
insert:0
        4
    2        6
  0    3    5    7
 *  *  *  *  *  *  *  8
*************************************
insert:9
right rotation node: 7
        4
    2        6
  0    3    5    8
 *  *  *  *  *  *  7  9
*************************************
insert:1
        4
    2        6
  0    3    5    8
 *  1  *  *  *  *  7  9
*************************************



"""