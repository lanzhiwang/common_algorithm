#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://github.com/lanzhiwang/Python-Algorithms/blob/master/sorts/quick_sort_3_partition.py
"""
def quick_sort_3partition(sorting, left, right):
    if right <= left:
        return
    a = i = left
    b = right
    pivot = sorting[left]
    while i <= b:
        if sorting[i] < pivot:
            sorting[a], sorting[i] = sorting[i], sorting[a]
            a += 1
            i += 1
        elif sorting[i] > pivot:
            sorting[b], sorting[i] = sorting[i], sorting[b]
            b -= 1
        else:
            i += 1
    quick_sort_3partition(sorting, left, a - 1)
    quick_sort_3partition(sorting, b + 1, right)


if __name__ == '__main__':
    unsorted = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
    quick_sort_3partition(unsorted, 0, len(unsorted)-1)
    print(unsorted)