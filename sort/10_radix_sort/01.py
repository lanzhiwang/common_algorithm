#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
基数排序

https://mp.weixin.qq.com/s/WA3_h4IgIgNTNYeKs-j__Q



"""

# 从一个整数中分离个位，十位，百位，千位等
collection = [2, 15, 123, 1234]
for number in collection:
    print('number: %s' % number)
    # if number >= 0 and number < 10:
    #     print(number // 1 % 10)
    # elif number >= 10 and number < 100:
    #     print(number // 1 % 10)
    #     print(number // 10 % 10)
    # elif number >= 100 and number < 1000:
    #     print(number // 1 % 10)
    #     print(number // 10 % 10)
    #     print(number // 100 % 10)
    # elif number >= 1000 and number < 10000:
    #     print(number // 1 % 10)
    #     print(number // 10 % 10)
    #     print(number // 100 % 10)
    #     print(number // 1000 % 10)
    print(number // 1 % 10)
    print(number // 10 % 10)
    print(number // 100 % 10)
    print(number // 1000 % 10)
    print(number // 10000 % 10)
    print(number // 100000 % 10)

print()
print()

# 找到一组数中最大的数，获取最大数的位数
collection = [2, 15, 123, 1234]
print(collection)
max_value = max(collection)
print(max_value)
n = 1
exp = 10
while True:
    number1 = (max_value // exp) % 10
    number2 = (max_value // (exp * 10)) % 10
    if number1 == 0 and number2 == 0:
        break
    elif number1 != 0 and number2 == 0:
        n += 1
        break
    else:
        exp *= 100
        n += 2
print('n: %s' % n)
