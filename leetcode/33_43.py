#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
43. 字符串相乘
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
"""

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        len1 = len(num1)
        len2 = len(num2)
        result_num = [0] * (len1 + len2)
        for i in range(len1 - 1, -1, -1):
            n1 = int(num1[i])
            for j in range(len2 - 1, -1, -1):
                n2 = int(num2[j])
                temp = result_num[i + j + 1] + (n1 * n2)
                result_num[i + j + 1] = temp % 10
                result_num[i + j] += temp / 10
        result = ''.join(map(str, result_num))
        if result[0] == '0':
            result = result[1:]
        return result



print(Solution().multiply('123', '45'))

