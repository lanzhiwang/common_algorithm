#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
计数排序

https://juejin.im/post/5cac107ee51d456e7079f1d5

原始序列
A = [2, 5, 3, 0, 2, 3, 0, 3]

{0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
{0: 2, 1: 0, 2: 2, 3: 3, 4: 0, 5: 1}
{0: 2, 1: 2, 2: 4, 3: 7, 4: 7, 5: 8}

"""


def counting_sort(collection):
    if len(collection) <= 1:
        return collection

    result = [None] * len(collection)
    min_value = min(collection)
    max_value = max(collection)

    c = {i: 0 for i in range(min_value, max_value+1)}
    for number in collection:
        c[number] += 1

    for i in c:
        if i-1 in c:
            c[i] = c[i] + c[i-1]

    for number in collection:
        result[c[number]-1] = number
        c[number] -= 1

    return result


if __name__ == '__main__':
    unsorted = [2, 2, 3, 5]
    print(counting_sort(unsorted))

    unsorted = [2, 5, 3, 0, 2, 3, 0, 3]
    print(counting_sort(unsorted))

    unsorted = [0, 2, 2, 3, 5]
    print(counting_sort(unsorted))

    unsorted = []
    print(counting_sort(unsorted))

    unsorted = [-45, -5, -2]
    print(counting_sort(unsorted))
