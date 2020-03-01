#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
斐波那契数列 Fibonacci sequence
[1, 1, 2, 3, 5, 8, 13, 21, 34]

fab(5)
    fab(4)  return 5
    fab(3)  return 3
    return 8

fab(4)
    fab(3)  return 3
    fab(2)  return 2
    return 5

fab(3)
    fab(2)  return 2
    fab(1)  return 1
    return 3

fab(2)
    fab(1)  return 1
    fab(0)  return 1
    return 2

fab(1)
    return 1

fab(0)
    return 1

"""

def fab(n):
    result = -1
    # 忽略整数判断
    if n == 0 or n == 1:
        result = 1
        return result
    if n < 0:
        return result

    result = fab(n-1) + fab(n-2)
    return result


print(fab(0))
print(fab(1))
print(fab(2))
print(fab(3))
print(fab(4))
print(fab(5))
