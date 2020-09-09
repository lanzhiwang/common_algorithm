#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
746. 使用最小花费爬楼梯
数组的每个索引作为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。

每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

示例 1:

输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。

 示例 2:

输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。

注意：

cost 的长度将会在 [2, 1000]。
每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。


[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
 0  1    2  3  4  5    6  7  8    9

opt(9)
    opt(8)
    1 + opt(7)

opt(8)
    opt(7)
    opt(6)

opt(7)
    opt(6)  return 2
    opt(5)  return 2
    return 2

opt(6)
    opt(5)  return 2
    opt(4)  return 2 1+2
    return 2

opt(5)
    opt(4)  return 2
    opt(3)  return 2 100+2
    return 2

opt(4)
    opt(3)  return 2
    opt(2)  return 2 1+2
    return 2

opt(3)
    [2, 3]
    [1, 3]
    opt(2)  return 2
    opt(1)  return 100 1+100
    return 2

opt(2)
    [0, 2]
    [1, 2]
    opt(1)  return 100
    opt(0)  return 1   1+1
    return 2

opt(1)
    return 100

opt(0)
    return 1

[0011]
[0, 0, 0, 1]
"""

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if not cost:
            return 0
        pre_first = cost[0]
        pre_second = cost[1]
        for i in range(2, len(cost)):
            temp = min(cost[i], cost[i] + pre_first)
            pre_first = pre_second
            pre_second = temp
        return pre_second

print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))




