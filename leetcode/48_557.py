#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
557. 反转字符串中的单词 III
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例：

输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split()
        result_list = []
        for i in s_list:
            result_list.append(i[::-1])
        return ' '.join(result_list)

