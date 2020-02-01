#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://mp.weixin.qq.com/s/BwL0Av7Zim5Fr6TOg-bfSA

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2, 1, -3, 4, -1, 2, 1, -5, 4]

输出: 6

解释: 连续子数组 [4, -1, 2, 1] 的和最大，为 6。


分析:
opt[i]：表示以 nums[i] 结尾的连续子数组的最大和

nums: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
opt:  [-2, 1, -2, 4,  3, 5, 6,  1, 5]

opt[i] = nums[i] + opt(i-1)  opt(i-1) >= 0
opt[i] = nums[i]             opt(i-1) < 0
opt(0) = nums[i]
"""
