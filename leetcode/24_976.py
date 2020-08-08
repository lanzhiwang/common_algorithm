#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

r"""
976. 三角形的最大周长
给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。

如果不能形成任何面积不为零的三角形，返回 0。


示例 1：

输入：[2,1,2]
输出：5
示例 2：

输入：[1,2,1]
输出：0
示例 3：

输入：[3,2,3,4]
输出：10
示例 4：

输入：[3,6,2,3]
输出：8

[] [1, 2, 3, 4, 5, 6]
    [1] [2, 3, 4, 5, 6]  return [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 2, 6] ... ]
    [2] [1, 3, 4, 5, 6]
    [3] [1, 2, 4, 5, 6]
    [4] [1, 2, 3, 5, 6]
    [5] [1, 2, 3, 4, 6]
    [6] [1, 2, 3, 4, 5]
    return []

[1] [2, 3, 4, 5, 6]
    [1, 2] [3, 4, 5, 6]  return [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 2, 6]]
    [1, 3] [2, 4, 5, 6]
    [1, 4] [2, 3, 5, 6]
    [1, 5] [2, 3, 4, 6]
    [1, 6] [2, 3, 4, 5]
    return [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 2, 6] ... ]

[1, 2] [3, 4, 5, 6]
    [1, 2, 3] [4, 5, 6]  return [[1, 2, 3]]
    [1, 2, 4] [3, 5, 6]  return [[1, 2, 4]]
    [1, 2, 5] [3, 4, 6]  return [[1, 2, 5]]
    [1, 2, 6] [3, 4, 6]  return [[1, 2, 6]]
    return [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 2, 6]]

[1, 2, 3] [4, 5, 6]
    return [[1, 2, 3]]
"""

def get_combination(target, source, length):
    if len(target) == length:
        return [target]
    result = []
    for i in range(len(source)):
        temp = target[:]
        temp.append(source[i])
        for j in get_combination(temp, source[0:i] + source[i + 1:], length):
            result.append(j)
    return result

# print(get_combination([], [1, 2, 3, 4, 5, 6], 3))
# print(len(get_combination([], [1, 2, 3, 4, 5, 6], 3)))


def largest_perimeter(a):
    l_list = get_combination([], a, 3)
    max_perimeter = float('-inf')
    for l in l_list:
        l_sorted = sorted(l)
        if l_sorted[0] + l_sorted[1] > l_sorted[2]:
            max_perimeter = max(max_perimeter, sum(l_sorted))
    return max_perimeter

# print(largest_perimeter([2,1,2]))


def get_combination_by_yield(source, length):
    if length == 1:
        for i in source:
            yield [i]

    for i in range(len(source)):
        for j in get_combination_by_yield(source[0:i] + source[i + 1:], length - 1):
            j.append(source[i])
            yield j


def largest_perimeter_by_yield(a):
    l_list = get_combination_by_yield(a, 3)
    max_perimeter = float('-inf')
    for l in l_list:
        l_sorted = sorted(l)
        print(l_sorted)
        if l_sorted[0] + l_sorted[1] > l_sorted[2]:
            max_perimeter = max(max_perimeter, sum(l_sorted))
    return max_perimeter

# start_time = time.time()
# print(largest_perimeter_by_yield([26,46,88,38,22,2,31,11,36,18,123]))
# print(time.time() - start_time)



def largestPerimeter(A):
    a = sorted(A, reverse=True)
    for i in range(len(a)- 2):
        if a[i] < a[i + 1] + a[i + 2]:
            return a[i] + a[i + 1] + a[i + 2]
    return 0

print(largestPerimeter([26,46,88,38,22,2,31,11,36,18,123]))