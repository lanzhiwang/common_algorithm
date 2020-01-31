#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
https://www.youtube.com/watch?v=Jakbj4vaIbE

arr = [3, 34, 4, 12, 5, 2]
       0  1   2  3   4  5
s = 9
1、是否有一组数之和为 9，返回 True 或 False
2、如果有一组数之和为 9，列出所有的组合方式


                                                                        sub(5, 9)
                                       /                                                                    \
                                sub(4, 7)                                                                 sub(4, 9)
                    /                              \                                          /                                     \
            sub(3, 2)                            sub(3, 7)                             sub(3, 4)                                  sub(3, 9)
             /     \                               /    \                               /      \                                  /       \
     sub(2, -10) sub(2, 2)                  sub(2, -5) sub(2, 7)                 sub(2, -8)    sub(2, 4)                  sub(2, -3)    sub(2, 9)
                 /     \                             /          \                          /              \                           /             \
        sub(1, -2)   sub(1, 2)             sub(1, 3)           sub(1, 7)           sub(1, 0)             sub(1, 4)             sub(1, 5)            sub(1, 9)
                     /      \               /     \              /   \              /      \              /     \              /      \              /     \
               sub(0, -32)sub(0, 2) sub(0, -31)sub(0, 3) sub(0, -27)sub(0, 7) sub(0, -34)sub(0, 0) sub(0, -30)sub(0, 4) sub(0, -29)sub(0, 5) sub(0, -25)sub(0, 9)

subset(5, 9)
 选 subset(4, 7)
    subset(4, 7)
     选 subset(3, 2)
        subset(3, 2)
         选 subset(2, -10) -> return
         不选 subset(2, 2)
            subset(2, 2)
             选 subset(1, -2) -> return
             不选 subset(1, 2)
                subset(1, 2)
                 选 subset(0, -32)
                 不选 subset(0, 2) -> return
     不选 subset(3, 7)
        subset(3, 7)
         选 subset(2, -5) -> return
         不选 subset(2, 7)
            subset(2, 7)
             选 subset(1, 3)
                subset(1, 3)
                 选 subset(0, -31) -> return
                 不选 subset(0, 3) -> return
             不选 subset(1, 7)
                subset(1, 7)
                 选 subset(0, -27) -> return
                 不选 subset(0, 7) -> return
 不选 subset(4, 9)
    subset(4, 9)
     选 subset(3, 4)
        subset(3, 4)
         选 subset(2, -8) -> return
         不选 subset(2, 4)
            subset(2, 4) -> return
     不选 subset(3, 9)

"""

arr = [3, 34, 4, 12, 5, 2]
s = 9

# 是否有一组数之和为 9，返回 True 或 False
def rec_sub(collentions, i, s):
    if collentions[i] == s:
        return True
    if s < 0:
        return False
    if i == 0:
        if collentions[0] == s:
            return True
        else:
            return False
    select = rec_sub(collentions, i-1, s-collentions[i])
    no_select = rec_sub(collentions, i-1, s)
    return select or no_select


print(rec_sub(arr, len(arr)-1, s))
