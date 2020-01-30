#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
https://www.youtube.com/watch?v=1BAsAgdx7Ac

https://www.youtube.com/watch?v=Jakbj4vaIbE




opt(i) i = 0 1 2 3 4 5 6 7

opt(7)
 选   4 + opt(4)
 不选 opt(6)

opt(6) -> 10
 选   2 + opt(2)
 不选 opt(5)

opt(5) -> 9
 选   3 + opt(1)
 不选 opt(4)

opt(4) -> 9
 选   6 + opt(None)
 不选 opt(3)

opt(3) -> 9
 选   4 + opt(0)
 不选 opt(2)

opt(2) -> 8
 选   8 + opt(None)
 不选 opt(1)

opt(1) -> 5
 选   1 + opt(None)
 不选 opt(0)

opt(0) -> 5
 选   5
 不选 None


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
    def __init__(self, value, start, end, prev=None):
        self.value = value
        self.start = start
        self.end = end
        self.prev = prev

    def __str__(self):
        return 'value: %s, start: %s, end: %s, prev: %s' % (self.value, self.start, self.end, self.prev)


if __name__ == '__main__':
    tasks = []
    for t in [(5, 1, 4), (1, 3, 5), (8, 0, 6), (4, 4, 7), (6, 3, 8), (3, 5, 9), (2, 6, 10), (4, 8, 11)]:
        tasks.append(Task(*t))
    for i in range(1, len(tasks)):
        for j in range(i-1, -1, -1):
            if tasks[j].end <= tasks[i].start or tasks[j].start >= tasks[i].end:
                tasks[i].prev = j
                break

    for task in tasks:
        print(task)

    opt = [None] * len(tasks)
    opt[0] = 5

    for i in range(1, len(tasks)):
        if tasks[i].prev is None:
            select = tasks[i].value
        else:
            select = tasks[i].value + opt[tasks[i].prev]
        no_select = opt[i-1]
        opt[i] = max(select, no_select)

    print(opt)

