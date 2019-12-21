#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
计数排序

https://juejin.im/post/5cac107ee51d456e7079f1d5

[2, 2, 3, 5]
min: 2
max 5
c: [0, 0, 0, 0]
    2  3  4  5
c: [2, 1, 0, 1]
c: [2, 3, 3, 4]
"""


def counting_sort(collection):
    if len(collection) <= 1:
        return collection

    result = [None] * len(collection)
    min_value = min(collection)
    max_value = max(collection)

    c = [0] * (max_value - min_value + 1)

    for number in collection:
        c[number - min_value] += 1

    for i in range(len(c)):
        if i > 0:
            c[i] = c[i] + c[i-1]

    for number in collection:
        result[c[number - min_value]-1] = number
        c[number - min_value] -= 1

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
