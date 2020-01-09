#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import copy

"""
快速排序 - 从小到大升序排序
array 6 1 2 7 9 3 4 5 10 8

第 1 趟（j找到比6小的位置，i找到比6大的位置，j 先移动）
i                  j
6 1 2 7 9 3 4 5 10 8
^

      i       j
6 1 2 7 9 3 4 5 10 8
6 1 2 5 9 3 4 7 10 8
^
        i   j
6 1 2 5 9 3 4 7 10 8
6 1 2 5 4 3 9 7 10 8
^

          j i
6 1 2 5 4 3 9 7 10 8
3 1 2 5 4 6 9 7 10 8
          ^
循环条件：i < j

递归两个子序列
3 1 2 5 4
9 7 10 8

第 1 趟（j找到比3小的位置，i找到比3大的位置，j 先移动）
i       j
3 1 2 5 4
^

    j i
3 1 2 5 4
^

2 1 3 5 4

循环条件：i < j

递归两个子序列
2 1
5 4

i j
2 1
^

  ij
2 1
^

1 2
循环条件：i < j
"""


def quick_sort_01(array, left, right):
    # print('*****', array, left, right)

    if right <= left:
        return

    i = left
    j = right
    while i < j:
        # print('while')
        # print("i=%s, j=%s" % (i, j))
        for k in range(right, left-1, -1):
            j = k
            if array[k] < array[left]:
                break
        # print("i=%s, array[%s]=%s, j=%s, array[%s]=%s" % (i, i, array[i], j, j, array[j]))

        for k in range(left, right+1):
            i = k
            if array[k] > array[left]:
                break
        # print("i=%s, array[%s]=%s, j=%s, array[%s]=%s" % (i, i, array[i], j, j, array[j]))

        if i < j:
            array[i], array[j] = array[j], array[i]
            # print(array)

    else:
        # print('else while')
        array[left], array[j] = array[j], array[left]
        # print(array)

    # left_array = array[0:j]
    # right_array = array[j+1:]
    # print('left_array: %s' % left_array)
    # print('right_array: %s' % right_array)
    # print(array)

    quick_sort_01(array, left, j-1)
    quick_sort_01(array, j+1, right)

    # print(left_array + [array[j]] + right_array)
    # return left_array + [array[j]] + right_array


def quick_sort_02(array, left, right):
    if right <= left:
        return
    i = left
    j = right
    while i < j:
        for k in range(right, left-1, -1):
            j = k
            if array[k] < array[left]:
                break

        for k in range(left, right+1):
            i = k
            if array[k] > array[left]:
                break

        if i < j:
            array[i], array[j] = array[j], array[i]

    else:
        array[left], array[j] = array[j], array[left]

    quick_sort_02(array, left, j-1)
    quick_sort_02(array, j+1, right)


for unsorted in [
    [], [0], [2], [3, 5], [5, 3], [5, 5], [0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 3, 5],
    [2, 5, 3, 0, 2, 3, 0, 3], [0, 2, 2, 3, 5],
    [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5],
    [6, 1, 2, 7, 9, 3, 4, 5, 10, 8],
    [-45, -2, -5]
]:
    print(unsorted)
    quick_sort_02(unsorted, 0, len(unsorted)-1)
    print(unsorted)
