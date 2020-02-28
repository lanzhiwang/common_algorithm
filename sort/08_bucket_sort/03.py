#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
桶排序

处理负数

[-45, -5, -2]
min: -45
max: -2
bucket_len: -2 - (-45) + 1 = 44

{
-45: 0
-44: 0
-43: 0
...
-2: 0
}

[0, 0,  0,  0, ..., 0]
-45 -44 -43 -42     -2

"""

# 使用字典处理
def bucket_sort(my_list):
    result = []
    if len(my_list) <= 1:
        return my_list

    max_value = max(my_list)
    min_value = min(my_list)
    buckets = {i: 0 for i in range(min_value, max_value+1)}

    for i in my_list:
        buckets[i] += 1

    for index in buckets:
        result.extend([index] * buckets[index])

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
