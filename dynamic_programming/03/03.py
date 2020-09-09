#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from queue import Queue


r"""
https://www.youtube.com/watch?v=Jakbj4vaIbE

假设 arr 列表中全部为正整数，s 也是正整数
arr = [3, 34, 4, 12, 5, 2]
       0  1   2  3   4  5
s = 9
1、是否有一组数之和为 9，返回 True 或 False
2、如果有一组数之和为 9，列出所有的组合方式


subset(5, 9)
    subset(4, 7)  return True  [5]
    subset(4, 9)  return True  []
    return True


subset(4, 7)
    subset(3, 2)
    subset(3, 7)  return True [5]
    return True

subset(4, 9)
    subset(3, 4)  return True [4]
    subset(3, 9)
    return True


subset(3, 2)
    subset(2, -10)
    subset(2, 2)

subset(3, 7)
    subset(2, -5)
    subset(2, 7)  return True [5]
    return True

subset(3, 4)
    subset(2, -8)
    subset(2, 4)  return True [4]
    return True

subset(3, 9)
    subset(2, -3)
    subset(2, 9)



subset(2, -10)
    subset(1, -14)
    subset(1, -10)

subset(2, 2)
    subset(1, -2)
    subset(1, 2)

subset(2, -5)
    subset(1, -9)
    subset(1, -5)

subset(2, 7)
    subset(1, 3)  return True [5, 2]
    subset(1, 7)
    return True

subset(2, -8)
    subset(1, -12)
    subset(1, -8)

subset(2, 4)
    subset(1, 0)  return True [4, 2]
    subset(1, 4)
    return True

subset(2, -3)
    subset(1, -7)
    subset(1, -3)

subset(2, 9)
    subset(1, 5)
    subset(1, 9)


subset(1, -14)
    subset(0, -48)
    subset(0, -14)

subset(1, -10)
    subset(0, -44)
    subset(0, -10)

subset(1, -2)
    subset(0, -36)
    subset(0, -2)

subset(1, 2)
    subset(0, -32)
    subset(0, 2)

subset(1, -9)
    subset(0, -43)
    subset(0, -9)

subset(1, -5)
    subset(0, -39)
    subset(0, -5)

subset(1, 3)
    subset(0, -31)
    subset(0, 3)  return True [5, 2]
    return True

subset(1, 7)
    subset(0, -27)
    subset(0, 7)

subset(1, -12)
    subset(0, -46)
    subset(0, -12)

subset(1, -8)
    subset(0, -42)
    subset(0, -8)

subset(1, 0)
    subset(0, -34)
    subset(0, 0)  return True [4, 2]
    return True

subset(1, 4)
    subset(0, -30)
    subset(0, 4)

subset(1, -7)
    subset(0, -41)
    subset(0, -7)

subset(1, -3)
    subset(0, -37)
    subset(0, -3)

subset(1, 5)
    subset(0, -29)
    subset(0, 5)

subset(1, 9)
    subset(0, -25)
    subset(0, 9)


subset(0, -48)
subset(0, -14)
subset(0, -44)
subset(0, -10)
subset(0, -36)
subset(0, -2)
subset(0, -32)
subset(0, 2)
subset(0, -43)
subset(0, -9)
subset(0, -39)
subset(0, -5)
subset(0, -31)
subset(0, 3)  [5, 2, 0]
    return True
subset(0, -27)
subset(0, 7)
subset(0, -46)
subset(0, -12)
subset(0, -42)
subset(0, -8)
subset(0, -34)
subset(0, 0)  [4, 2]
    return True
subset(0, -30)
subset(0, 4)
subset(0, -41)
subset(0, -7)
subset(0, -37)
subset(0, -3)
subset(0, -29)
subset(0, 5)
subset(0, -25)
subset(0, 9)







是否有一组数之和为 9，返回 True 或 False
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
