#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy

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


def quick_sort(array):
    len_array = len(array)

    if len_array <= 1:
        return array

    i = 0
    j = len_array - 1
    while i < j:
        # print('while')
        # print("i=%s, j=%s" % (i, j))
        for k in range(len_array-1, -1, -1):
            if array[k] < array[0]:
                j = k
                break
            else:
                continue
        # print("i=%s, array[%s]=%s, j=%s, array[%s]=%s" % (i, i, array[i], j, j, array[j]))

        for k in range(len_array):
            if array[k] > array[0]:
                i = k
                break
            else:
                continue
        # print("i=%s, array[%s]=%s, j=%s, array[%s]=%s" % (i, i, array[i], j, j, array[j]))

        if i < j:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

        # print(array)

    else:
        # print('else while')
        temp = array[0]
        array[0] = array[j]
        array[j] = temp
        # print(array)

    left_array = array[0:j]
    right_array = array[j+1:]
    print('left_array: %s' % left_array)
    print('right_array: %s' % right_array)

    # quick_sort(left_array)
    # quick_sort(right_array)

    return quick_sort(left_array) + [array[j]] + quick_sort(right_array)



array = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
print(array)
print(quick_sort(array))
print(array)
