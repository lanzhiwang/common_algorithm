#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
基数排序

https://mp.weixin.qq.com/s/WA3_h4IgIgNTNYeKs-j__Q

基数排序有两种方式进行，一种是LSD，从右边关键字开始排序，另一种是MSD，从左边关键字开始排序。
https://blog.csdn.net/xgf415/article/details/76595887

基数排序MSD

[103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5]
百位
0 9 1 7 11 15 25 5
1 103 107
2 201 209
3
4
5
6
7
8
9

9 1 7 11 15 25 5
十位
0 9 1 7 5
1 11 15
2 25
3
4
5
6
7
8
9

9 1 7 5
个位
0
1 1
2
3
4
5 5
6
7 7
8
9 9

1 5 7 9

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


def radix_sort_msd(collection, exp):
    # print('radix_sort_msd')
    # print(collection, exp)

    c = {i: [] for i in range(0, 10)}
    # print(c)
    for number in collection:
        c[number // exp % 10].append(number)
    # print(c)  # {0: [9, 1, 7, 11, 15, 25, 5], 1: [103, 107], 2: [201, 209], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

    result = []
    # if exp == 1:
    #     for value in c.values():
    #         result += value
    #     return result
    for value in c.values():
        if exp == 1:
            result += value
        else:
            result += radix_sort_msd(value, exp // 10)
    return result


# 基数排序SD(只考虑正整数)
def radix_sort_msd_help(collection):
    # print('radix_sort_msd_help')
    # print(collection)
    if len(collection) <= 1:
        return collection

    max_value, n = get_max_n(collection)
    # print(max_value, n)

    if max_value == 0:  # collection = [0, 0, 0, 0, 0]
        return collection

    exp = pow(10, n-1)
    return radix_sort_msd(collection, exp)

    # for i in range(n-1, -1, -1):  # 0, 1, 2
    #     exp = pow(10, i)  # 100, 10, 1
    #     counting_sort(collection, exp)


if __name__ == '__main__':
    tests = [[], [0], [2], [0, 0, 0, 0], [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5]]
    # tests = [[103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5]]
    for test in tests:
        print(test)
        print(radix_sort_msd_help(test))
        print()
