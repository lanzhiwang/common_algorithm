#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
77. 组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

combine([1, 2, 3, 4], count=2)
    1
    combine([2, 3, 4], count=1)  return [[2], [3], [4]]
    [[1, 2], [1, 3], [1, 4]]

    2
    combine([3, 4], count=1)  return [[3], [4]]
    [[2, 3], [2, 4]]

    3
    combine([4], count=1)  return [[4]]
    [[3, 4]]

    4
    combine([], count=1)  return []


combine([2, 3, 4], count=1)
    2
    3
    4
    return [[2], [3], [4]]

combine([3, 4], count=1)
    return [[3], [4]]

combine([4], count=1)
    return [[4]]

combine([], count=1)
    return []


#########################################

[123]
[124]
[134]
[234]
combine([1, 2, 3, 4], count=3)
    1
    combine([2, 3, 4], count=2)  return [[2, 3], [2, 4], [3, 4]]

    2
    combine([3, 4], count=2)  return [[3, 4]]

    3
    combine([4], count=2)  return []

    4
    combine([], count=2)  return []


combine([2, 3, 4], count=2)
    2
    combine([3, 4], count=1)  return [[3], [4]]
    [[2, 3], [2, 4]]

    3
    combine([4], count=1)  return [[4]]
    [[3, 4]]

    4
    return [[2, 3], [2, 4], [3, 4]]

combine([3, 4], count=2)
    return [[3, 4]]

combine([4], count=2)
    return []


combine([3, 4], count=1)
    return [[3], [4]]

combine([4], count=1)
    return [[4]]



"""

class Solution(object):
    def com_bine(self, source, count):
        if len(source) < count:
            return []
        else:
            if count == 1:
                result = []
                for data in source:
                    result.append([data])
                return result

        result = []
        for i, v in enumerate(source):
            for l in self.com_bine(source[i+1:], count-1):
                l.insert(0, v)
                result.append(l)
        return result

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.com_bine(range(1, n+1), k)

