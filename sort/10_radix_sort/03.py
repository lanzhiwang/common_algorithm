#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
基数排序

https://mp.weixin.qq.com/s/WA3_h4IgIgNTNYeKs-j__Q

基数排序有两种方式进行，一种是LSD，从右边关键字开始排序，另一种是MSD，从左边关键字开始排序。

基数排序SD

[103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5]

"""


# 基数排序SD(只考虑正整数)
def radix_sort_msd(collection):
    pass


if __name__ == '__main__':
    tests = [[], [0], [2], [0, 0, 0, 0], [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5]]
    for test in tests:
        print(test)
        print(radix_sort_msd(test))
        print()


