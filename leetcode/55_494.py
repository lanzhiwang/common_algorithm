#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
494. 目标和
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。
对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

示例：

输入：nums: [1, 1, 1, 1, 1], S: 3
输出：5
解释：

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。

提示：

数组非空，且长度不会超过 20 。
初始的数组的和不会超过 1000 。
保证返回的最终结果能被 32 位整数存下。

[1, 1, 1, 1, 1], S: 3
 0  1  2  3  4

fun(4, 3)
    +1 f(3, 2)  return [[-1, +1, +1, +1], [+1, -1, +1, +1], [+1, +1, -1, +1], [+1, +1, +1, -1]]
    -1 f(3, 4)  return [[+1, +1, +1, +1]]
    return [[-1, +1, +1, +1, +1], [+1, -1, +1, +1, +1], [+1, +1, -1, +1, +1], [+1, +1, +1, -1, +1], [+1, +1, +1, +1, -1]]

f(3, 2)
    +1 f(2, 1)  return [[-1, +1, +1], [+1, -1, +1], [+1, +1, -1]]
    -1 f(2, 3)  return [[+1, +1, +1]]
    return [[-1, +1, +1, +1], [+1, -1, +1, +1], [+1, +1, -1, +1], [+1, +1, +1, -1]]

f(3, 4)
    +1 f(2, 3)  return [[+1, +1, +1]]
    -1 f(2, 5)
    return [[+1, +1, +1, +1]]


f(2, 1)
    +1 f(1, 0)  return [[-1, +1], [+1, -1]]
    -1 f(1, 2)  return [[+1, +1]]
    return [[-1, +1, +1], [+1, -1, +1], [+1, +1, -1]]

f(2, 3)
    +1 f(1, 2)  return [[+1, +1]]
    -1 f(1, 4)
    return [[+1, +1, +1]]

f(2, 3)
    +1 f(1, 2)  return [[+1, +1]]
    -1 f(1, 4)
    return [[+1, +1, +1]]

f(2, 5)
    +1 f(1, 4)
    -1 f(1, 6)


f(1, 0)
    +1 f(0, -1)  return [[-1]]
    -1 f(0, 1)  return [[+1]]
    return [[-1, +1], [+1, -1]]

f(1, 2)
    +1 f(0, 1)  return [[+1]]
    -1 f(0, 3)
    return [[+1, +1]]

f(1, 2)
    +1 f(0, 1)  return [[+1]]
    -1 f(0, 3)
    return [[+1, +1]]

f(1, 4)
    +1 f(0, 3)
    -1 f(0, 5)

f(1, 2)
    +1 f(0, 1)  return [[+1]]
    -1 f(0, 3)
    return [[+1, +1]]

f(1, 4)
    +1 f(0, 3)
    -1 f(0, 5)

f(1, 4)
    +1 f(0, 3)
    -1 f(0, 5)

f(1, 6)
    +1 f(0, 5)
    -1 f(0, 7)




f(0, -1)
    return [[-1]]

f(0, 1)
    return [[+1]]

f(0, 1)
    return [[+1]]

f(0, 3)
    return []
f(0, 1)
    return [[+1]]

f(0, 3)
f(0, 3)
f(0, 5)
f(0, 1)
    return [[+1]]

f(0, 3)
f(0, 3)
f(0, 5)
f(0, 3)
f(0, 5)
f(0, 5)
f(0, 7)

"""


class Solution(object):
    def fid_tar_sum(self, index, nums, sum):
        value = nums[index]
        print(index, value, sum)
        if index == 0 and value == 0 and sum == 0:
            return [['+0'], ['-0']]
        elif index == 0 and sum == value:
            return [['+%s' % value]]
        elif index == 0 and sum == 0 - value:
            return [['-%s' % value]]
        elif index == 0:
            return []

        result = []
        # + value
        print(self.fid_tar_sum(index-1, nums, sum-value))
        for l in self.fid_tar_sum(index-1, nums, sum-value):
            l.append('+%s' % value)
            result.append(l)
        # - value
        print(self.fid_tar_sum(index-1, nums, sum+value))
        for l in self.fid_tar_sum(index-1, nums, sum+value):
            l.append('-%s' % value)
            result.append(l)
        return result


    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        return self.fid_tar_sum(len(nums)-1, nums ,S)

print(Solution().findTargetSumWays([10,34,28,5,10,26,9,17,28,10,9,6,10,15,0,28,42,39,25,19], 26))

"""
[0, 1] 1
 0  1

f(1, 1)
    +1 f(0, 0)
    -1 f(0, 2)

f(0, 0)
    return [[+0], [-0]]
f(0, 2)

############

[0, 0, 1] 1
 0  1  2

f(2, 1)
    +1 f(1, 0)  return [[+0, +0], [-0, +0], [+0, -0], [-0, -0]]
    -1 f(1, 2)

f(1, 0)
    +0 f(0, 0)  return [[+0], [-0]]
    -0 f(0, 0)  return [[+0], [-0]]
    return [[+0, +0], [-0, +0], [+0, -0], [-0, -0]]

f(1, 2)
    +0 f(0, 2)  return []
    -0 f(0, 2)  return []
    return []


f(0, 0)
    return [[+0], [-0]]
f(0, 0)
    return [[+0], [-0]]

f(0, 2)
    return []
f(0, 2)
    return []



"""