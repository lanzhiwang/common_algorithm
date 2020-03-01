#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from queue import Queue


r"""
https://www.youtube.com/watch?v=Jakbj4vaIbE

假设 arr 列表中全部为正整数，s 也是正整数
arr = [3, 34, 4, 12, 5, 2]
       0  1   2  3   4  5
s = 9
1、是否有一组数之和为 9，返回 True 或 False
2、如果有一组数之和为 9，列出所有的组合方式
"""


r"""
如果有一组数之和为 9，列出所有的组合方式

方法一：

                                                                        sub(5, 9)
                                       /                                                                    \
                                sub(4, 7)                                                                 sub(4, 9)
                    /                              \                                          /                                     \
            sub(3, 2)                            sub(3, 7)                             sub(3, 4)                                  sub(3, 9)
             /     \                               /    \                               /      \                                  /       \
     sub(2, -10) sub(2, 2)                  sub(2, -5) sub(2, 7)                 sub(2, -8)    sub(2, 4)                  sub(2, -3)    sub(2, 9)
                 /     \                             /          \                          /              \                           /             \
        sub(1, -2)   sub(1, 2)             sub(1, 3)           sub(1, 7)           sub(1, 0)             sub(1, 4)             sub(1, 5)            sub(1, 9)
                     /      \               /     \              /   \              /      \              /     \              /      \              /     \
               sub(0, -32)sub(0, 2) sub(0, -31)sub(0, 3) sub(0, -27)sub(0, 7) sub(0, -34)sub(0, 0) sub(0, -30)sub(0, 4) sub(0, -29)sub(0, 5) sub(0, -25)sub(0, 9)

最后等于 0 或者 3

arr = [3, 34, 4, 12, 5, 2]
       3  3   7  7   7  9
       0  0   4  4   9  9

"""
arr = [3, 34, 4, 12, 5, 2]

# 5 -> 2, 9
result = [[9]]

# 4 -> 5, 9
result = [[9, 7], [9, 9]]

# 3 -> 12, 9
result = [[9, 7, 2], [9, 7, 7], [9, 9, 4], [9, 9, 9]]

# 2 -> 4, 9
result = [[9, 7, 2, -10], [9, 7, 2, 2], [9, 7, 7, -5], [9, 7, 7, 7], [9, 9, 4, -8], [9, 9, 4, 4], [9, 9, 9, -3], [9, 9, 9, 9]]

# 1 -> 34, 9
# 0 -> 3, 9

def get_all_list_1(collentions, i, sum_list):
    result = []
    if i <= 0:
        for l in sum_list:
            if l[-1]-arr[i+1] in (0, collentions[0]):
                temp1 = l[:]
                temp1.append(l[-1]-arr[i+1])
                result.append(temp1)

            if l[-1] in (0, collentions[0]):
                temp2 = l[:]
                temp2.append(l[-1])
                result.append(temp2)
        return result

    for l in sum_list:
        temp1 = l[:]
        temp1.append(l[-1]-arr[i+1])

        temp2 = l[:]
        temp2.append(l[-1])

        result.append(temp1)
        result.append(temp2)
    return get_all_list_1(collentions, i-1, result)

arr = [3, 34, 4, 12, 5, 2]
result = get_all_list_1(arr, len(arr)-2, [[9]])
print(result)

"""
[[9, 7, 7, 7, 3, 3], [9, 9, 4, 4, 0, 0]]
"""


r"""
如果有一组数之和为 9，列出所有的组合方式

方法二：

"""

arr = [3, 34, 4, 12, 5, 2]
s = 9

# 0 -> 3
result = [[3], [0]]

# 1 -> 34
result = [[3, 37], [3, 3], [0, 34], [0, 0]]
result = [[3, 3], [0, 0]]

# 2 -> 4
result = [[3, 3, 7], [3, 3, 3], [0, 0, 4], [0, 0, 0]]

# 3 -> 12
result = [[3, 3, 7, 19], [3, 3, 7, 7], [3, 3, 3, 15], [3, 3, 3, 3], [0, 0, 4, 16], [0, 0, 4, 4], [0, 0, 0, 12], [0, 0, 0, 0]]

# 4 -> 5

# 5 -> 2

def get_all_list_2(collentions, i, s, sum_list):
    result = []
    if i == 0:  # 0
        result = [[collentions[0]], [0]]
        return get_all_list_2(collentions, i+1, s, result)

    elif i >= 1 and i <= len(collentions) - 2:  # 1 2 3 4
        for l in sum_list:
            if l[-1] + arr[i] <= s:
                temp1 = l[:]
                temp1.append(l[-1] + arr[i])
                result.append(temp1)
            temp2 = l[:]
            temp2.append(l[-1])
            result.append(temp2)
        return get_all_list_2(collentions, i+1, s, result)
    elif i == len(collentions) - 1:  # 5
        for l in sum_list:
            if l[-1] + arr[i] == s:
                temp1 = l[:]
                temp1.append(l[-1] + arr[i])
                result.append(temp1)
            if l[-1] == s:
                temp2 = l[:]
                temp2.append(l[-1])
                result.append(temp2)
        return result

result = []
result = get_all_list_2(arr, 0, 9, [])
print(result)
"""
[[3, 3, 7, 7, 7, 9], [0, 0, 4, 4, 9, 9]]
"""


r"""
如果有一组数之和为 9，列出所有的组合方式

方法二：

"""

arr = [3, 34, 4, 12, 5, 2]
s = 9

# 0 -> 3, []
[3]
[0]

# 1 -> 34, [3]
[3, 37]
[3, 3]
[0, 34]
[0, 0]

# 2 -> 4, [3, 37]
[3, 37, 41]
[3, 37, 37]
...

# 3 -> 12, [3, 37, 41]
[3, 37, 41, 53]
[3, 37, 41, 41]

# 4 -> 5, [3, 37, 41, 53]
[3, 37, 41, 53, 58]  # return [[3, 37, 41, 53, 58, 60], [3, 37, 41, 53, 58, 58]]
[3, 37, 41, 53, 53]  # return [[3, 37, 41, 53, 53, 55], [3, 37, 41, 53, 53, 53]]

# return [[3, 37, 41, 53, 58, 60], [3, 37, 41, 53, 58, 58], [3, 37, 41, 53, 53, 55], [3, 37, 41, 53, 53, 53]]

# 5 -> 2, [3, 37, 41, 53, 58]
[3, 37, 41, 53, 58, 60]
[3, 37, 41, 53, 58, 58]

# return [[3, 37, 41, 53, 58, 60], [3, 37, 41, 53, 58, 58]]



def get_all_list_3(collentions, i, s, sum_list):
    result = []
    if i == 0 and (not len(sum_list)):
        temp1 = get_all_list_3(collentions, i+1, s, [collentions[i]])
        temp2 = get_all_list_3(collentions, i+1, s, [0])
        temp1.extend(temp2)
        for temp in temp1:
            if temp[-1] == s:
                result.append(temp)
        return result
    elif i >= 1 and i <= len(collentions) - 2 and len(sum_list):
        temp1 = sum_list[:]
        temp1.append(sum_list[-1]+collentions[i])
        temp1 = get_all_list_3(collentions, i+1, s, temp1)
        temp2 = sum_list[:]
        temp2.append(sum_list[-1])
        temp2 = get_all_list_3(collentions, i+1, s, temp2)
        temp1.extend(temp2)
        return temp1
    elif i == len(collentions) - 1:
        temp1 = sum_list[:]
        temp1.append(sum_list[-1]+collentions[i])
        temp2 = sum_list[:]
        temp2.append(sum_list[-1])
        return [temp1, temp2]

result = get_all_list_3(arr, 0, 9, [])
print(result)
