#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
基数排序

https://mp.weixin.qq.com/s/WA3_h4IgIgNTNYeKs-j__Q
https://blog.csdn.net/xgf415/article/details/76595887


"""

# 从一个整数中分离个位，十位，百位，千位等
collection = [2, 15, 123, 1234, 0]
for number in collection:
    print('number: %s' % number)
    print(number // 1 % 10)  # 个位
    print(number // 10 % 10)  # 十位
    print(number // 100 % 10)  # 百位
    print(number // 1000 % 10)  # 千位
    print(number // 10000 % 10)  # 万位

"""
number: 2
2
0
0
0
0
number: 15
5
1
0
0
0
number: 123
3
2
1
0
0
number: 1234
4
3
2
1
0
number: 0
0
0
0
0
0
"""
print()
print()

# 找到一组数中最大的数，获取最大数的位数
collection = [2, 15, 123, 1234]
print(collection)
max_value = max(collection)
print(max_value)
"""
[2, 15, 123, 1234]
1234
n: 4
"""

print(max_value // 1)  # 1234
print(max_value // 10)  # 123
print(max_value // 100)  # 12
print(max_value // 1000)  # 1
print(max_value // 10000)  # 0

n = 1
exp = 10
while max_value // exp:
    n += 1
    exp *= 10
print('n: %s' % n)
"""
n: 4
"""