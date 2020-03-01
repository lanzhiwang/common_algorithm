#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/trapping-rain-water/
https://mp.weixin.qq.com/s/sO3rokhr_xsjZ0wXf6j5GQ

0 3

[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
 0  1  2  3  4  5  6  7  8  9  10 11

0 []                           [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
1 [0]                             [1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
2 [0, 1]                             [0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
3 [0, 1, 0]                             [2, 1, 0, 1, 3, 2, 1, 2, 1]
4 [0, 1, 0, 2]                             [1, 0, 1, 3, 2, 1, 2, 1]
5 [0, 1, 0, 2, 1]                             [0, 1, 3, 2, 1, 2, 1]
6 [0, 1, 0, 2, 1, 0]                             [1, 3, 2, 1, 2, 1]
7 [0, 1, 0, 2, 1, 0, 1]                             [3, 2, 1, 2, 1]
8 [0, 1, 0, 2, 1, 0, 1, 3]                             [2, 1, 2, 1]
9 [0, 1, 0, 2, 1, 0, 1, 3, 2]                             [1, 2, 1]
10 [0, 1, 0, 2, 1, 0, 1, 3, 2, 1]                            [2, 1]
11 [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2]                            [1]

            [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
             0  1  2  3  4  5  6  7  8  9  10 11
min_height: [0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1]
                   1     1  2  1        1
"""


def trapping_rain_water_01(collection):
    ans = 0
    if len(collection) <= 2:
        return ans

    for i in range(1, len(collection)-1):
        l_max = max(collection[0:i])
        r_max = max(collection[i:])

        min_height = min(l_max, r_max)
        if min_height > collection[i]:
            ans += min_height-collection[i]

    return ans


def trapping_rain_water_02(collection):
    ans = 0
    if len(collection) <= 2:
        return ans

    l_max_height = 0
    r_max_height = max(collection)
    for i in range(1, len(collection)-1):
        l_max_height = max(collection[i-1], l_max_height)
        if collection[i-1] <= r_max_height:
            r_max_height = max(collection[i:])
        min_height = min(l_max_height, r_max_height)
        if collection[i] < min_height:
            ans += (min_height - collection[i])
    return ans


if __name__ == "__main__":
    contain = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trapping_rain_water_01(contain))
    print(trapping_rain_water_02(contain))
