#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
斐波那契数列 Fibonacci sequence
"""

fibonacci = [None, None, None, None, None, None]

fibonacci[0] = 1
fibonacci[1] = 1
fibonacci[2] = fibonacci[1] + fibonacci[0]
fibonacci[3] = fibonacci[2] + fibonacci[1]
fibonacci[4] = fibonacci[3] + fibonacci[2]
fibonacci[5] = fibonacci[4] + fibonacci[3]

print(fibonacci)  # [1, 1, 2, 3, 5, 8]


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