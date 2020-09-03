#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
350. 两个数组的交集 II
给定两个数组，编写一个函数来计算它们的交集。

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]

示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]

nums1 = [1,2,2,1], nums2 = [2,2]

[1, 1, 2, 2] i = 0
[2, 2] j = 0
[]

[1, 1, 2, 2] i = 1
[2, 2] j = 0
[]

[1, 1, 2, 2] i = 2
[2, 2] j = 0
[2]

[1, 1, 2, 2] i = 3
[2, 2] j = 1
[2, 2]

"""

def intersect(nums1, nums2):
    num1 = sorted(nums1)
    num2 = sorted(nums2)
    result = []
    i = 0
    j = 0
    while True:
        try:
            if num1[i] == num2[j]:
                result.append(num1[i])
                i += 1
                j += 1
            elif num1[i] > num2[j]:
                j += 1
            else:
                i += 1
        except IndexError as e:
            break
    return result








