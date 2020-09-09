#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
303. 区域和检索 - 数组不可变
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：

给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
说明:

你可以假设数组不可变。
会多次调用 sumRange 方法。

[-2, 0, 3, -5, 2, -1]
[-2, -2, 1, -4, -2, -3]
  0   1  2   3   4   5
sumRange(0, 2) -> [0, 1, 2]
sumRange(2, 5) -> [0, 1, 2, 3, 4, 5] - [0, 1]
"""

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.accumulate = []
        for index, num in enumerate(nums):
            if index > 0:
                self.accumulate.append(self.accumulate[index-1] + num)
            else:
                self.accumulate.append(num)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.accumulate[j]
        return self.accumulate[j] - self.accumulate[i-1]


