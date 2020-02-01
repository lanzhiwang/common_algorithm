#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://mp.weixin.qq.com/s/zxGybmwITUMSuw-PqZ_nEA

给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:

[

  [1,3,1],

  [1,5,1],

  [4,2,1]

]

输出: 7

解释: 因为路径 1→3→1→1→1 的总和最小。

分析:
    0 1 2
    -----
0 | 1 3 1
1 | 1 5 1
2 | 4 2 1

opt(2, 2) -> 6+1 = 7
    opt(2, 1) -> 5+2 = 7
        opt(2, 0) -> 1+4 = 5
            opt(2, -1) -> None
            opt(1, 0) -> 1
                opt(1, -1) -> None
                opt(-1, 0) -> None
        opt(1, 1) -> 2+5 = 7
            opt(1, 0) -> 1+1 = 2
                opt(1, -1) -> None
                opt(0, 0) -> 1
                    opt(0, -1) -> None
                    opt(-1, 0) -> None
            opt(0, 1) -> 1+1 = 2
                opt(0, 0) -> 1
                    opt(0, -1) -> None
                    opt(-1, 0) -> None
                opt(-1, 1) -> None
    opt(1, 2) -> 5+1 = 6
        opt(1, 1) -> 2+5 = 7
            opt(1, 0) -> 1+1 = 2
                opt(1, -1) -> None
                opt(0, 0) -> 1
                    opt(0, -1) -> None
                    opt(-1, 0) -> None
            opt(0, 1) -> 1+3 = 4
                opt(0, 0) -> 1
                    opt(0, -1) -> None
                    opt(-1, 0) -> None
                opt(-1, 1) -> None
        opt(0, 2) -> 4+1 = 5
            opt(0, 1) -> 1+3 = 4
                opt(0, 0) -> 1
                    opt(0, -1) -> None
                    opt(-1, 0) -> None
                opt(-1, 1) -> None
            opt(-1, 2) -> None



opt(2, 1)
opt(2, 0)




"""
