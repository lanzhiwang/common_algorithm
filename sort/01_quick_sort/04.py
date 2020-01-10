#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://github.com/lanzhiwang/Python-Algorithms/blob/master/sorts/quick_sort_3_partition.py

快速排序 - 从小到大升序排序
array 6, 1, 2, 7, 9, 3, 4, 5, 10, 8

pivot = 6
a: 0, b: 9, i: 0
[6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
a: 0, b: 9, i: 1
[6, 1, 2, 7, 9, 3, 4, 5, 10, 8]

a: 0, b: 9, i: 1
[6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
a: 1, b: 9, i: 2
[1, 6, 2, 7, 9, 3, 4, 5, 10, 8]

a: 1, b: 9, i: 2
[1, 6, 2, 7, 9, 3, 4, 5, 10, 8]
a: 2, b: 9, i: 3
[1, 2, 6, 7, 9, 3, 4, 5, 10, 8]

a: 2, b: 9, i: 3
[1, 2, 6, 7, 9, 3, 4, 5, 10, 8]
a: 2, b: 8, i: 3
[1, 2, 6, 8, 9, 3, 4, 5, 10, 7]

a: 2, b: 8, i: 3
[1, 2, 6, 8, 9, 3, 4, 5, 10, 7]
a: 2, b: 7, i: 3
[1, 2, 6, 10, 9, 3, 4, 5, 8, 7]

a: 2, b: 7, i: 3
[1, 2, 6, 10, 9, 3, 4, 5, 8, 7]
a: 2, b: 6, i: 3
[1, 2, 6, 5, 9, 3, 4, 10, 8, 7]

a: 2, b: 6, i: 3
[1, 2, 6, 5, 9, 3, 4, 10, 8, 7]
a: 3, b: 6, i: 4
[1, 2, 5, 6, 9, 3, 4, 10, 8, 7]

a: 3, b: 6, i: 4
[1, 2, 5, 6, 9, 3, 4, 10, 8, 7]
a: 3, b: 5, i: 4
[1, 2, 5, 6, 4, 3, 9, 10, 8, 7]

a: 3, b: 5, i: 4
[1, 2, 5, 6, 4, 3, 9, 10, 8, 7]
a: 4, b: 5, i: 5
[1, 2, 5, 4, 6, 3, 9, 10, 8, 7]

a: 4, b: 5, i: 5
[1, 2, 5, 4, 6, 3, 9, 10, 8, 7]
a: 5, b: 5, i: 6
[1, 2, 5, 4, 3, 6, 9, 10, 8, 7]

[1, 2, 5, 4, 3, 6, 9, 10, 8, 7]

"""


def quick_sort_3partition(sorting, left, right):
    if right <= left:
        return
    a = i = left
    b = right
    pivot = sorting[left]
    while i <= b:
        # print('a: %s, b: %s, i: %s' % (a, b, i))
        # print(sorting)
        if sorting[i] < pivot:
            sorting[a], sorting[i] = sorting[i], sorting[a]
            a += 1
            i += 1
        elif sorting[i] > pivot:
            sorting[b], sorting[i] = sorting[i], sorting[b]
            b -= 1
        else:
            i += 1
        # print('a: %s, b: %s, i: %s' % (a, b, i))
        # print(sorting)
        # print()
    quick_sort_3partition(sorting, left, a - 1)
    quick_sort_3partition(sorting, b + 1, right)


if __name__ == '__main__':
    # unsorted = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
    # quick_sort_3partition(unsorted, 0, len(unsorted)-1)
    # print(unsorted)


    for unsorted in [
        [], [0], [2], [3, 5], [5, 3], [5, 5], [0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 3, 5],
        [2, 5, 3, 0, 2, 3, 0, 3], [0, 2, 2, 3, 5],
        [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5],
        [6, 1, 2, 7, 9, 3, 4, 5, 10, 8],
        [-45, -2, -5]
    ]:
        print(unsorted)
        quick_sort_3partition(unsorted, 0, len(unsorted) - 1)
        print(unsorted)
        print()
