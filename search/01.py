#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
二分法查找

target: 4
array: 1 3 4 6 8 11 14
1 3 4 6 8 11 14
^               ^
middle: (0+7)/2 = 3
array[3]: 6 > 4

1 3 4 6 8 11 14
^     ^
middle: (0+3)/2 = 1
array[1]: 3 < 4

1 3 4 6 8 11 14
  ^   ^
middle: (1+3)/2 = 2
array[2]: 4

###############################

target: 8
array: 1 3 4 6 8 11 14
1 3 4 6 8 11 14
^               ^
middle: (0+7)/2 = 3
array[3]: 6 < 8

1 3 4 6 8 11 14
      ^         ^
middle: (3+7)/2 = 5
array[5]: 11 > 8

1 3 4 6 8 11 14
      ^   ^
middle: (3+5)/2 = 4
array[4]: 8

###############################

target: 7
array: 1 3 4 6 8 11 14
1 3 4 6 8 11 14
^               ^
middle: (0+7)/2 = 3
array[3]: 6 < 7

1 3 4 6 8 11 14
      ^        ^
middle: (3+7)/2 = 5
array[5]: 11 > 7

1 3 4 6 8 11 14
      ^   ^
middle: (3+5)/2 = 4
array[4]: 8 > 7

1 3 4 6 8 11 14
      ^ ^
middle: (3+4)/2 = 3
array[3]: 6 < 7

"""


def dichotomy_search(array, target):
    left = 0
    right = len(array)

    while right-left > 1:
        middle = (left + right) / 2
        if array[middle] > target:
            right = middle
        elif array[middle] < target:
            left = middle
        else:
            return middle
    else:
        return -1


print(dichotomy_search([1, 3, 4, 6, 8, 11, 14], 4))
print(dichotomy_search([1, 3, 4, 6, 8, 11, 14], 8))
print(dichotomy_search([1, 3, 4, 6, 8, 11, 14], 7))
