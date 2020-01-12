#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
基数排序(只考虑正整数)

https://mp.weixin.qq.com/s/WA3_h4IgIgNTNYeKs-j__Q
https://blog.csdn.net/xgf415/article/details/76595887

基数排序有两种方式进行，一种是LSD，从右边关键字开始排序，另一种是MSD，从左边关键字开始排序。

基数排序LSD

[103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5]

个位
0
1 1 11 201
2
3 103
4
5 15 25 5
6
7 7 107
8
9 9 209

1 11 201 103 15 25 5 7 107 9 209
十位
0 1 201 103 5 7 107 9 209
1 11 15
2 25
3
4
5
6
7
8
9

1 201 103 5 7 107 9 209 11 15 25
百位
0 1 5 7 9 11 15 25
1 103 107
2 201 209
3
4
5
6
7
8
9

1 5 7 9 11 15 25 103 107 201 209


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
    while max_value // exp:
        n += 1
        exp *= 10

    return max_value, n


# [{0: 3}, {1: 9}, {2: 1}, {3: 7}, {4: 1}, {5: 5}, {6: 5}, {7: 1}, {8: 9}, {9: 7}, {10: 5}]
def get_max_min(collection):
    print(collection)
    min_value = None
    max_value = None
    for key, value in collection:
        if max_value is None and min_value is None:
            min_value = value
            max_value = value
            break
        if value < min_value:
            min_value = value
        if max_value < value:
            max_value = value
    return min_value, max_value


# 计数排序
def counting_sort(collection, exp):
    # print('计数排序')
    # print(collection, exp)
    length = len(collection)
    if length <= 1:
        return collection

    numbers = []
    for i in collection:
        numbers.append(i // exp % 10)

    result = [None] * length
    min_value = min(numbers)
    max_value = max(numbers)

    c = [0] * (max_value - min_value + 1)

    for number in numbers:
        c[number - min_value] += 1

    for i in range(len(c)):
        if i > 0:
            c[i] = c[i] + c[i-1]

    for number in collection[::-1]:
        temp = number // exp % 10
        result[c[temp - min_value] -1] = number
        c[temp - min_value] -= 1

    return result


# 基数排序LSD(只考虑正整数)
def radix_sort_lsd(collection):
    # print(collection)
    if len(collection) <= 1:
        return collection

    max_value, n = get_max_n(collection)
    # print(max_value, n)

    if max_value == 0:  # collection = [0, 0, 0, 0, 0]
        return collection

    for i in range(n):  # 0, 1, 2
        exp = pow(10, i)  # 1, 10, 100
        # print(exp)
        collection = counting_sort(collection, exp)
        # print(collection)
    return collection


if __name__ == '__main__':
    for unsorted in [
        [], [0], [2], [3, 5], [5, 3], [5, 5], [0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 3, 5],
        [2, 5, 3, 0, 2, 3, 0, 3], [0, 2, 2, 3, 5],
        [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5],
        [6, 1, 2, 7, 9, 3, 4, 5, 10, 8],
    ]:
        print(unsorted)
        print(radix_sort_lsd(unsorted))
        print()
