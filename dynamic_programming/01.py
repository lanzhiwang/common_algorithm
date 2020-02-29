#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import operator

r"""
https://www.youtube.com/watch?v=1BAsAgdx7Ac

opt(i) i = 0 1 2 3 4 5 6 7

opt(7) -> 13
 选   4 + opt(4) -> 4+9
 不选 opt(6) -> 10

opt(6) -> 10
 选   2 + opt(2) -> 2+8
 不选 opt(5) -> 9

opt(5) -> 9
 选   3 + opt(1) -> 3+5
 不选 opt(4) -> 9

opt(4) -> 9
 选   6 + opt(None) -> 6+0
 不选 opt(3) -> 9

opt(3) -> 9
 选   4 + opt(0) -> 4+5
 不选 opt(2) -> 8

opt(2) -> 8
 选   8 + opt(None) -> 8+0
 不选 opt(1) -> 5

opt(1) -> 5
 选   1 + opt(None) -> 1+0
 不选 opt(0) -> 5

opt(0) -> 5
 选   5
 不选 None -> 0


opt(i)
 选   vi + opt(prev(i))
 不选 opt(i-1)

i prev(i) opt(i)
0 None    5
1 None    5
2 None    8
3 0       9
4 None    9
5 1       9
6 2       10
7 4       13


"""


class Task(object):
    def __init__(self, value, start, end, prev=None, no_select=0, select=0):
        self.value = value
        self.start = start
        self.end = end
        self.prev = prev
        self.no_select = no_select
        self.select = select

    def __str__(self):
        return 'value: %s, start: %s, end: %s, prev: %s, no_select: %s, select: %s' % (self.value, self.start, self.end, self.prev, self.no_select, self.select)


if __name__ == '__main__':
    tasks = []
    for t in [(5, 1, 4), (1, 3, 5), (8, 0, 6), (4, 4, 7), (6, 3, 8), (3, 5, 9), (2, 6, 10), (4, 8, 11)]:
        tasks.append(Task(*t))

    """
    1 -> 0
    2 -> 1 0
    3 -> 2 1 0
    4 -> 3 2 1 0
    5 -> 4 3 2 1 0
    6 -> 5 4 3 2 1 0
    7 -> 6 5 4 3 2 1 0
    """
    for i in range(1, len(tasks)):  # 1 2 3 4 5 6 7
        for j in range(i-1, -1, -1):
            if tasks[j].end <= tasks[i].start or tasks[j].start >= tasks[i].end:
                tasks[i].prev = j
                break

    for task in tasks:
        print(task)
    """
    value: 5, start: 1, end: 4, prev: None
    value: 1, start: 3, end: 5, prev: None
    value: 8, start: 0, end: 6, prev: None
    value: 4, start: 4, end: 7, prev: 0
    value: 6, start: 3, end: 8, prev: None
    value: 3, start: 5, end: 9, prev: 1
    value: 2, start: 6, end: 10, prev: 2
    value: 4, start: 8, end: 11, prev: 4
    """

    tasks[0].no_select = 0
    tasks[0].select = tasks[0].value
    opt = [None] * len(tasks)
    opt[0] = max(tasks[0].value, tasks[0].no_select)
    for i in range(1, len(tasks)):  # 1 2 3 4 5 6 7
        if tasks[i].prev is None:
            select = tasks[i].value
        else:
            select = tasks[i].value + opt[tasks[i].prev]
        no_select = opt[i-1]
        tasks[i].no_select = no_select
        tasks[i].select = select
        opt[i] = max(select, no_select)

    print(opt)  # [5, 5, 8, 9, 9, 9, 10, 13]

    for task in tasks:
        print(task)
    """
    value: 5, start: 1, end: 4, prev: None, no_select: 0, select: 5
    value: 1, start: 3, end: 5, prev: None, no_select: 5, select: 1
    value: 8, start: 0, end: 6, prev: None, no_select: 5, select: 8
    value: 4, start: 4, end: 7, prev: 0, no_select: 8, select: 9
    value: 6, start: 3, end: 8, prev: None, no_select: 9, select: 6
    value: 3, start: 5, end: 9, prev: 1, no_select: 9, select: 8
    value: 2, start: 6, end: 10, prev: 2, no_select: 9, select: 10
    value: 4, start: 8, end: 11, prev: 4, no_select: 10, select: 13
    """

    # 回溯 opt tasks
    result = []
    index = len(tasks) - 1
    while index >= 0:
        if opt[index] == tasks[index].no_select:
            index = index - 1
        else:
            result.append(index)
            if tasks[index].prev is None:
                break
            index = tasks[index].prev
    print(result)
