#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
基数排序(只考虑正整数)

https://mp.weixin.qq.com/s/WA3_h4IgIgNTNYeKs-j__Q

基数排序有两种方式进行，一种是LSD，从右边关键字开始排序，另一种是MSD，从左边关键字开始排序。

基数排序LSD

[103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5]

"""


"""找到一组数中最大的数，获取最大数的位数

[]
[0]
[2]
[0, 0, 0, 0]
[103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5]

"""
def get_max_n(collection):
    if len(collection) == 0:
        return None, None

    max_value = max(collection)
    if max_value == 0:
        return 0, 1

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
    return max_value, n


# 计数排序
def counting_sort(collection):
    if len(collection) <= 1:
        return collection

    result = [None] * len(collection)
    min_value = min(collection)
    max_value = max(collection)

    c = [0] * (max_value - min_value + 1)

    for number in collection:
        c[number - min_value] += 1

    for i in range(len(c)):
        if i > 0:
            c[i] = c[i] + c[i-1]

    for number in collection:
        result[c[number - min_value]-1] = number
        c[number - min_value] -= 1

    return result

# 基数排序LSD
def radix_sort(collection):
    print(collection)
    if len(collection) <= 1:
        return collection

    max_value, n = get_max_n(collection)
    print(max_value, n)

    if max_value == 0:  # collection = [0, 0, 0, 0, 0]
        return collection

    for i in range(n):  # 0, 1, 2
        exp = pow(10, i)  # 1, 10, 100
        print(exp)
        counting_sort(collection, exp)

    for number in collection:
        print(number)





if __name__ == '__main__':
    tests = [[], [0], [2], [0, 0, 0, 0], [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5]]
    for test in tests:
        print(test)
        print(get_max_n(test))
    print()
    print()



    unsorted = [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5]
    print(radix_sort(unsorted))
