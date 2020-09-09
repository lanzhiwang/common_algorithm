#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
121. 买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。


示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

[7, 1, 5, 3, 6, 4]
 0  1  2  3  4  5

max_profit(5)
    4 - 1

max_profit(4)
    6 - 1

max_profit(3)
    3 - 1

max_profit(2)
    5 - 1

max_profit(1)
    1 - 7


"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) in [0, 1]:
            return 0
        prices = prices[::-1]
        print(prices)
        max_profit = float('-inf')
        for i, v in enumerate(prices):
            sub_prices = prices[i+1:]
            if len(sub_prices) > 0:
                min_buy_price = min(prices[i+1:])
                max_profit = max(v - min_buy_price, max_profit)
        max_profit = max(0, max_profit)
        return max_profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
