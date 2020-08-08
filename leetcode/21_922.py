#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
922. 按奇偶排序数组 II
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

你可以返回任何满足上述条件的数组作为答案。


示例：

输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。

[4, 2, 5, 7]

odd = 1
even = 0
[]

4
odd = 1
even = 2
[4]

2
odd = 1
even = 4
[4, None, 2]

5
odd = 3
even = 4
[4, 5, 2]

7
odd = 3
even = 4
[4, 5, 2, 7]

"""

def sort_array_by_parity(a):
    odd = 1
    even = 0
    result = []
    for v in a:
        if v % 2 == 0:
            result.insert(even, v)
            even += 2
        else:
            result.insert(odd, v)
            odd += 2
    return result

print(sort_array_by_parity([4, 2, 5, 7]))
