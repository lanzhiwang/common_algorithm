#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
计数排序

https://juejin.im/post/5cac107ee51d456e7079f1d5


[2, 5, 3, 0, 2, 3, 0, 3]
result: [None, None, None, None, None, None, None, None]
min_value: 0
max_value: 5
c: {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
c: {0: 2, 1: 0, 2: 2, 3: 3, 4: 0, 5: 1}
c: {0: 2, 1: 2, 2: 4, 3: 7, 4: 7, 5: 8}

number: 2
result: [None, None, None, None, None, None, None, None]
c: {0: 2, 1: 2, 2: 4, 3: 7, 4: 7, 5: 8}
result: [None, None, None, 2, None, None, None, None]
c: {0: 2, 1: 2, 2: 3, 3: 7, 4: 7, 5: 8}

number: 5
result: [None, None, None, 2, None, None, None, None]
c: {0: 2, 1: 2, 2: 3, 3: 7, 4: 7, 5: 8}
result: [None, None, None, 2, None, None, None, 5]
c: {0: 2, 1: 2, 2: 3, 3: 7, 4: 7, 5: 7}

number: 3
result: [None, None, None, 2, None, None, None, 5]
c: {0: 2, 1: 2, 2: 3, 3: 7, 4: 7, 5: 7}
result: [None, None, None, 2, None, None, 3, 5]
c: {0: 2, 1: 2, 2: 3, 3: 6, 4: 7, 5: 7}

number: 0
result: [None, None, None, 2, None, None, 3, 5]
c: {0: 2, 1: 2, 2: 3, 3: 6, 4: 7, 5: 7}
result: [None, 0, None, 2, None, None, 3, 5]
c: {0: 1, 1: 2, 2: 3, 3: 6, 4: 7, 5: 7}

number: 2
result: [None, 0, None, 2, None, None, 3, 5]
c: {0: 1, 1: 2, 2: 3, 3: 6, 4: 7, 5: 7}
result: [None, 0, 2, 2, None, None, 3, 5]
c: {0: 1, 1: 2, 2: 2, 3: 6, 4: 7, 5: 7}

number: 3
result: [None, 0, 2, 2, None, None, 3, 5]
c: {0: 1, 1: 2, 2: 2, 3: 6, 4: 7, 5: 7}
result: [None, 0, 2, 2, None, 3, 3, 5]
c: {0: 1, 1: 2, 2: 2, 3: 5, 4: 7, 5: 7}

number: 0
result: [None, 0, 2, 2, None, 3, 3, 5]
c: {0: 1, 1: 2, 2: 2, 3: 5, 4: 7, 5: 7}
result: [0, 0, 2, 2, None, 3, 3, 5]
c: {0: 0, 1: 2, 2: 2, 3: 5, 4: 7, 5: 7}

number: 3
result: [0, 0, 2, 2, None, 3, 3, 5]
c: {0: 0, 1: 2, 2: 2, 3: 5, 4: 7, 5: 7}
result: [0, 0, 2, 2, 3, 3, 3, 5]
c: {0: 0, 1: 2, 2: 2, 3: 4, 4: 7, 5: 7}

"""


def counting_sort(collection):
    # print(collection)
    if len(collection) <= 1:
        return collection

    result = [None] * len(collection)
    min_value = min(collection)
    max_value = max(collection)
    # print('result: %s' % result)
    # print('min_value: %s' % min_value)
    # print('max_value: %s' % max_value)

    c = {i: 0 for i in range(min_value, max_value+1)}
    # print('c: %s' % c)

    for number in collection:
        c[number] += 1
    # print('c: %s' % c)

    for i in c:
        if i-1 in c:
            c[i] = c[i] + c[i-1]
    # print('c: %s' % c)

    for number in collection:
        # print('number: %s' % number)
        # print('result: %s' % result)
        # print('c: %s' % c)
        result[c[number]-1] = number
        c[number] -= 1
        # print('result: %s' % result)
        # print('c: %s' % c)
        # print()

    return result


if __name__ == '__main__':
    for unsorted in [
        [], [0], [2], [3, 5], [5, 3], [5, 5], [0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 3, 5],
        [2, 5, 3, 0, 2, 3, 0, 3], [0, 2, 2, 3, 5],
        [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5],
        [6, 1, 2, 7, 9, 3, 4, 5, 10, 8], [0, 2, 2, -6, -1, 3, 5],
        [-45, -2, -5]
    ]:
        print(unsorted)
        print(counting_sort(unsorted))
        print()
