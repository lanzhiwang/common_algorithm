#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
696. 计数二进制子串
给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。

重复出现的子串要计算它们出现的次数。

示例 1 :

输入: "00110011"
输出: 6
解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。

请注意，一些重复出现的子串要计算它们出现的次数。

另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
示例 2 :

输入: "10101"
输出: 4
解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
注意：

s.length 在1到50,000之间。
s 只包含“0”或“1”字符。


00110011
0
0 curr = 2 prev = 2
1
1 curr = 2 prev = 2
0
0 curr = 2 prev = 2
1
1


"""

class Solution(object):
    def count_binary_substrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        prev = 0
        curr = 0
        for index , value in enumerate(s):
            if index == 0:
                curr += 1
            else:
                if value == s[index - 1]:
                    curr += 1
                else:
                    prev = curr
                    curr = 1
            if curr <= prev:
                count += 1
        return count

print(Solution().count_binary_substrings('00110011'))
