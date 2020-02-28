#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
桶排序

处理负数
[-45, -5, -2]
min: -45
max: -2
bucket_len: -2 - (-45) + 1 = 44
[0, 0,  0,  0, ..., 0]
 0  1   2   3  ...  43 -> index + min
-45 -44 -43 -42     -2


[2, 2, 3, 5]
min: 2
max: 5
bucket_len: 5 - 2 + 1 = 4
[0, 0, 0, 0]
 0  1  2  3 -> index + min
 2  3  4  5

"""

def bucket_sort(my_list):
    result = []
    if len(my_list) <= 1:
        return my_list

    max_value = max(my_list)
    min_value = min(my_list)
    bucket_len = max_value - min_value + 1
    buckets = [0 for _ in range(bucket_len)]

    for i in my_list:
        buckets[i-min_value] += 1

    for index in range(bucket_len):
        result.extend( [index + min_value] * buckets[index] )

    return result


if __name__ == '__main__':
    for unsorted in [
        [], [0], [2], [3, 5], [5, 3], [5, 5], [0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 3, 5],
        [2, 5, 3, 0, 2, 3, 0, 3], [0, 2, 2, 3, 5],
        [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5],
        [6, 1, 2, 7, 9, 3, 4, 5, 10, 8], [0, 2, 2, -6, -1, 3, 5],
        [-45, -2, -5]
    ]:
        print(unsorted)
        print(bucket_sort(unsorted))
        print()
