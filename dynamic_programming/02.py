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
 选   3 + opt(4)
 不选 opt(5)

opt(5) -> 13
 选   8 + opt(3)
 不选 opt(4)

opt(4) -> 12
 选   7 + opt(2)
 不选 opt(3)

opt(3) -> 5
 选   1 + opt(1)
 不选 opt(2)

opt(2) -> 5
 选   4 + opt(0)
 不选 opt(1)

opt(1) -> 2
 选   2 + opt(None)
 不选 opt(0)

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
    def __init__(self, value, prev=None):
        self.value = value
        self.prev = prev

    def __str__(self):
        return 'value: %s, prev: %s' % (self.value, self.prev)


if __name__ == '__main__':
    nodes = []
    for t in [1, 2, 4, 1, 7, 8, 3]:
        nodes.append(Node(t))

    for i in range(len(nodes)):
        if i - 2 >= 0:
            nodes[i].prev = i - 2
        else:
            nodes[i].prev = None

    for node in nodes:
        print(node)

    opt = [None] * len(nodes)
    opt[0] = nodes[0].value
    for i in range(1, len(nodes)):
        if nodes[i].prev is None:
            select = nodes[i].value
        else:
            select = nodes[i].value + opt[nodes[i].prev]
        no_select = opt[i-1]
        opt[i] = max(select, no_select)

    print(opt)
