#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
https://leetcode-cn.com/problems/house-robber-iii/

在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。
除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:
输入: [3, 2, 3, None, 3, None, 1]

     3
    / \
   2   3
    \   \
     3   1

输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.

分析:
[3, 2, 3, None, 3, None, 1]
 0  1  2  3     4  5     6

            3-0
        /         \
      2-1         3-2
     /   \       /   \
  None-3 3-4  None-5 1-6

计算父节点
i (i-1)//2
0 None
1 0
2 0
3 1
4 1
5 2
6 2

0 -> 3, []
    [1]
    [0]
    return 1 -> 2, [[1], [0]]


1 -> 2, [[1], [0]]
    [1, 0]
    [0, 1]
    [0, 0]
    return 2 -> 3, [[1, 0], [0, 1], [0, 0]]

2 -> 3, [[1, 0], [0, 1], [0, 0]]
    [1, 0, 0]
    [0, 1, 1]
    [0, 1, 0]
    [0, 0, 1]
    [0, 0, 0]
    return 3 -> None, [[1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 0, 1], [0, 0, 0]]

3 -> None, [[1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
    [1, 0, 0, None]
    [0, 1, 1, None]
    [0, 1, 0, None]
    [0, 0, 1, None]
    [0, 0, 0, None]
    return 4 -> 3, [[1, 0, 0, None], [0, 1, 1, None], [0, 1, 0, None], [0, 0, 1, None], [0, 0, 0, None]]

4 -> 3, [[1, 0, 0, None], [0, 1, 1, None], [0, 1, 0, None], [0, 0, 1, None], [0, 0, 0, None]]
    [1, 0, 0, None, 1]
    [1, 0, 0, None, 0]
    [0, 1, 1, None, 0]
    [0, 1, 0, None, 0]
    [0, 0, 1, None, 1]
    [0, 0, 1, None, 0]
    [0, 0, 0, None, 1]
    [0, 0, 0, None, 0]
    return 5 -> None, [[1, 0, 0, None, 1], [1, 0, 0, None, 0], [0, 1, 1, None, 0], [0, 1, 0, None, 0], [0, 0, 1, None, 1], [0, 0, 1, None, 0], [0, 0, 0, None, 1], [0, 0, 0, None, 0]]

5 -> None, [[1, 0, 0, None, 1], [1, 0, 0, None, 0], [0, 1, 1, None, 0], [0, 1, 0, None, 0], [0, 0, 1, None, 1], [0, 0, 1, None, 0], [0, 0, 0, None, 1], [0, 0, 0, None, 0]]
    [1, 0, 0, None, 1, None]
    [1, 0, 0, None, 0, None]
    [0, 1, 1, None, 0, None]
    [0, 1, 0, None, 0, None]
    [0, 0, 1, None, 1, None]
    [0, 0, 1, None, 0, None]
    [0, 0, 0, None, 1, None]
    [0, 0, 0, None, 0, None]
    return 6 -> 1, [[1, 0, 0, None, 1, None], [1, 0, 0, None, 0, None], [0, 1, 1, None, 0, None], [0, 1, 0, None, 0, None], [0, 0, 1, None, 1, None], [0, 0, 1, None, 0, None], [0, 0, 0, None, 1, None], [0, 0, 0, None, 0, None]]

6 -> 1, [[1, 0, 0, None, 1, None], [1, 0, 0, None, 0, None], [0, 1, 1, None, 0, None], [0, 1, 0, None, 0, None], [0, 0, 1, None, 1, None], [0, 0, 1, None, 0, None], [0, 0, 0, None, 1, None], [0, 0, 0, None, 0, None]]
    [1, 0, 0, None, 1, None, 1]
    [1, 0, 0, None, 1, None, 0]
    [1, 0, 0, None, 0, None, 1]
    [1, 0, 0, None, 0, None, 0]
    [0, 1, 1, None, 0, None, 0]
    [0, 1, 0, None, 0, None, 1]
    [0, 1, 0, None, 0, None, 0]
    [0, 0, 1, None, 1, None, 0]
    [0, 0, 1, None, 0, None, 0]
    [0, 0, 0, None, 1, None, 1]
    [0, 0, 0, None, 1, None, 0]
    [0, 0, 0, None, 0, None, 1]
    [0, 0, 0, None, 0, None, 0]
    return [[1, 0, 0, None, 1, None, 1], [1, 0, 0, None, 1, None, 0], [1, 0, 0, None, 0, None, 1], [1, 0, 0, None, 0, None, 0], [0, 1, 1, None, 0, None, 0], [0, 1, 0, None, 0, None, 1], [0, 1, 0, None, 0, None, 0], [0, 0, 1, None, 1, None, 0], [0, 0, 1, None, 0, None, 0], [0, 0, 0, None, 1, None, 1], [0, 0, 0, None, 1, None, 0], [0, 0, 0, None, 0, None, 1], [0, 0, 0, None, 0, None, 0]]


示例 2:
输入: [3, 4, 5, 1, 3, None, 1]

     3
    / \
   4   5
  / \   \
 1   3   1


输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.

"""

def get_all_method(collections, i, last_time):
    if i == 0:
        return get_all_method(collections, i+1, [[1], [0]])
    elif i >= 1 and i <= len(collections) - 1:
        temp = []
        for lt in last_time:
            if collections[i] is None:
                lt.append(None)
                temp.append(lt)
            elif lt[(i-1)//2] == 0:
                temp1 = lt[:]
                temp1.append(1)
                temp.append(temp1)

                temp2 = lt[:]
                temp2.append(0)
                temp.append(temp2)

            elif lt[(i-1)//2] == 1:
                lt.append(0)
                temp.append(lt)
        if i != len(collections) - 1:
            return get_all_method(collections, i+1, temp)
        else:
            return temp

test = [3, 2, 3, None, 3, None, 1]
result = get_all_method(test, 0, [])
print(result)
print('*' * 30)

nums = []
for r in result:
    num = 0
    for j in range(len(r)):
        if r[j] == 1:
            num += test[j]
    nums.append(num)
print(nums)  # [7, 6, 4, 3, 5, 3, 2, 6, 3, 4, 3, 1, 0]
