#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://mp.weixin.qq.com/s/GxQEoh9rHKBIhFwFYjmdVg

给定一个无序的整数数组，找到其中最长上升子序列的长度。


示例:

输入: [10, 9, 2, 5, 3, 7, 101, 18]

输出: 4

解释: 最长的上升子序列是 [2, 3, 7, 101]，它的长度是 4。

说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。

nums: [10, 9, 2, 5, 3, 7, 101, 18]
        0  1  2  3  4  5    6   7

opt[i] ：表示以nums[i]结尾的最长上升子序列的长度

opt(0) -> 1
opt(1) -> 1
opt(2) -> 1
opt(3) -> opt(2)+1 = 2
opt(4) -> opt(2)+1 = 2
opt(5) -> max(opt(4), opt(2)) + 1 = 3
opt(6) -> max(opt(5), opt(4), opt(3), opt(2), opt(1), opt(0)) + 1 = 4
opt(7) -> max(opt(5), opt(4), opt(3), opt(2), opt(1), opt(0)) + 1 = 4

"""
