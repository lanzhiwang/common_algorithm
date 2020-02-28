#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
桶排序

原始序列 8 3 2 5 5

大概确定原始序列的最大值：8
  0    0    0    0    0    0    0    0    0
a[0] a[1] a[2] a[3] a[4] a[5] a[6] a[7] a[8]

  0    0    1    1    0    2    0    0    1
a[0] a[1] a[2] a[3] a[4] a[5] a[6] a[7] a[8]

排序后的结果：
2 3 5 5 8


"""

# 无法处理负数，只能处理列表中全部是正整数的情况
def bucket_sort(my_list):
    result = []
    if len(my_list) <= 1:
        return my_list

    max_value = max(my_list)
    buckets = [0 for _ in range(int(max_value)+1)]

    for i in my_list:
        buckets[i] += 1

    for index in range(len(buckets)):
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
