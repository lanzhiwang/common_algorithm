#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
https://www.youtube.com/watch?v=Jakbj4vaIbE

测试数据一:
[4, 1, 1, 9, 1] -> 13

测试数据二:
[1, 2, 4, 1, 7, 8, 3]
 0  1  2  3  4  5  6

opt(6) -> 15
 选   3 + opt(4) -> 3+12
 不选 opt(5) -> 13

opt(5) -> 13
 选   8 + opt(3) -> 8+5
 不选 opt(4) -> 12

opt(4) -> 12
 选   7 + opt(2) -> 7+5
 不选 opt(3) -> 5

opt(3) -> 5
 选   1 + opt(1) -> 1+2
 不选 opt(2) -> 5

opt(2) -> 5
 选   4 + opt(0) -> 4+1
 不选 opt(1) -> 2

opt(1) -> 2
 选   2 + opt(None) -> 2
 不选 opt(0) -> 1

opt(0) -> 1
 选   1
 不选 None

opt(i)
 选   vi + opt(i-2)
 不选 opt(i-1)

i prev(i) opt(i)
0 None    1
1 None    2
2 0       5
3 1       5
4 2       12
5 3       13
6 4       15

"""


class Node(object):
    def __init__(self, value, prev=None, no_select=0, select=0):
        self.value = value
        self.prev = prev
        self.no_select = no_select
        self.select = select

    def __str__(self):
        return 'value: %s, prev: %s, no_select: %s, select: %s' % (self.value, self.prev, self.no_select, self.select)


if __name__ == '__main__':
    nodes = []
    for t in [1, 2, 4, 1, 7, 8, 3]:
        nodes.append(Node(t))

    for i in range(len(nodes)):  # 0 1 2 3 4 5 6
        if i - 2 >= 0:
            nodes[i].prev = i - 2
        else:
            nodes[i].prev = None

    for node in nodes:
        print(node)
    """
    value: 1, prev: None
    value: 2, prev: None
    value: 4, prev: 0
    value: 1, prev: 1
    value: 7, prev: 2
    value: 8, prev: 3
    value: 3, prev: 4
    """

    nodes[0].no_select = 0
    nodes[0].select = nodes[0].value
    opt = [None] * len(nodes)
    opt[0] = nodes[0].value
    for i in range(1, len(nodes)):  # 1 2 3 4 5 6
        if nodes[i].prev is None:
            select = nodes[i].value
        else:
            select = nodes[i].value + opt[nodes[i].prev]
        no_select = opt[i-1]
        nodes[i].no_select = no_select
        nodes[i].select = select
        opt[i] = max(select, no_select)

    print(opt)  # [1, 2, 5, 5, 12, 13, 15]
    for node in nodes:
        print(node)
    """
    value: 1, prev: None, no_select: 0, select: 1
    value: 2, prev: None, no_select: 1, select: 2
    value: 4, prev: 0, no_select: 2, select: 5
    value: 1, prev: 1, no_select: 5, select: 3
    value: 7, prev: 2, no_select: 5, select: 12
    value: 8, prev: 3, no_select: 12, select: 13
    value: 3, prev: 4, no_select: 13, select: 15
    """

    # 回溯 nodes opt
    result = []
    index = len(nodes) - 1
    while index >= 0:
        if opt[index] == nodes[index].no_select:
            index = index - 1
        else:
            result.append(index)
            if nodes[index].prev is None:
                break
            index = nodes[index].prev
    print(result)  # [6, 4, 2, 0]
