#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
415. 字符串相加
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。


提示：

num1 和num2 的长度都小于 5100
num1 和num2 都只包含数字 0-9
num1 和num2 都不包含任何前导零
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式
"""

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0':
            return num2
        if num2 == '0':
            return num1
        len1 = len(num1)
        len2 = len(num2)
        length = max(len1, len2)
        if len1 > len2:
            num2 = '%s%s' % ('0' * (len1 - len2), num2)
        else:
            num1 = '%s%s' % ('0' * (len2 - len1), num1)
        result_num = [0] * (length + 1)
        for i in range(length-1, -1, -1):
            try:
                n1 = int(num1[i])
            except IndexError as e:
                n1 = 0
            try:
                n2 = int(num2[i])
            except IndexError as e:
                n2 = 0
            temp = n1 + n2 + result_num[i+1]
            result_num[i+1] = temp % 10
            result_num[i] = temp / 10
        result = ''.join(map(str, result_num))
        return result.lstrip('0')



print(Solution().addStrings('999', '099'))


