#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from queue import Queue


r"""
https://www.youtube.com/watch?v=Jakbj4vaIbE

arr = [3, 34, 4, 12, 5, 2]
       0  1   2  3   4  5
s = 9
1、是否有一组数之和为 9，返回 True 或 False
2、如果有一组数之和为 9，列出所有的组合方式

0 2 5

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

subset(5, 9)
 选 subset(4, 7)
    subset(4, 7)
     选 subset(3, 2)
        subset(3, 2)
         选 subset(2, -10) -> return
         不选 subset(2, 2)
            subset(2, 2)
             选 subset(1, -2) -> return
             不选 subset(1, 2)
                subset(1, 2)
                 选 subset(0, -32)
                 不选 subset(0, 2) -> return
     不选 subset(3, 7)
        subset(3, 7)
         选 subset(2, -5) -> return
         不选 subset(2, 7)
            subset(2, 7)
             选 subset(1, 3)
                subset(1, 3)
                 选 subset(0, -31) -> return
                 不选 subset(0, 3) -> return
             不选 subset(1, 7)
                subset(1, 7)
                 选 subset(0, -27) -> return
                 不选 subset(0, 7) -> return
 不选 subset(4, 9)
    subset(4, 9)
     选 subset(3, 4)
        subset(3, 4)
         选 subset(2, -8) -> return
         不选 subset(2, 4)
            subset(2, 4) -> return
     不选 subset(3, 9)



arr = [3, 34, 4, 12, 5, 2]
       0  1   2  3   4  5

[2, 0]
[7, 2, 5, 0]
[19, 7, 14, 2, 17, 5, 12, 0]
[23, 19, 11, 7, 18, 14, 6, 2, 21, 17, 9, 5, 16, 12, 4, 0]
[57, 23, 53, 19, 45, 11, 41, 7, 52, 18, 48, 14, 40, 6, 36, 2, 55, 21, 51, 17, 43, 9, 39, 5, 50, 16, 46, 12, 38, 4, 34, 0]
[60, 57, 26, 23, 56, 53, 22, 19, 48, 45, 14, 11, 44, 41, 10, 7, 55, 52, 21, 18, 51, 48, 17, 14, 43, 40, 9, 6, 39, 36, 5, 2, 58, 55, 24, 21, 54, 51, 20, 17, 46, 43, 12, 9, 42, 39, 8, 5, 53, 50, 19, 16, 49, 46, 15, 12, 41, 38, 7, 4, 37, 34, 3, 0]

                                                                                             0
                                                /                                                                                           \
                                               2                                                                                             0
                          /                                           \                                                /                                             \
                         7                                             2                                              5                                               0
              /                    \                         /                     \                        /                     \                          /                     \
            19                      7                       14                      2                      17                      5                       12                       0
      /           \           /          \             /         \            /         \             /          \            /         \             /          \            /          \
     23           19         11           7           18         14          6           2           21          17          9           5           16          12          4            0
   /    \      /    \      /    \      /   \       /    \      /    \      /   \       /   \       /   \       /    \      /   \       /   \       /    \      /   \       /   \       /    \
  57    23    53    19    45    11    41    7     52    18    48    14    40    6     36    2     55    21    51    17    43    9     39    5     50    16    46    12    38    4     34     0
 / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \    / \
60 57 26 23 56 53 22 19 48 45 14 11 44 41 10  7 55 52 21 18 51 48 17 14 43 40 9   6 39 36 5   2 58 55 24 21 54 51 20 17 46 43 12  9 42 39 8   5 53 50 19 16 49 46 15 12 41 38 7   4 37  34 3   0

"""

arr = [3, 34, 4, 12, 5, 2]
s = 9

# 是否有一组数之和为 9，返回 True 或 False
def rec_sub(collentions, i, s):
    if collentions[i] == s:
        return True
    if s < 0:
        return False
    if i == 0:
        if collentions[0] == s:
            return True
        else:
            return False
    select = rec_sub(collentions, i-1, s-collentions[i])
    no_select = rec_sub(collentions, i-1, s)
    return select or no_select


print(rec_sub(arr, len(arr)-1, s))

queue = Queue()
queue.put(0)
# 543210
for i in range(5, -1, -1):
    l = []
    while not queue.empty():
        val = queue.get()
        l.append(val+arr[i])
        l.append(val)
    print(l)
    for j in l:
        queue.put(j)


r"""

     2          0
   /   \      /   \
  7     2    5     0
 / \   / \  / \   / \
19  7 14 2 17  5 12  0

 0  1  2 3  4  5  6  7
   0    1    2      3
      0          1


temp i
26   0
13   1
6    2
3    3
1    4
0    5

43   0
21   1
10   2
5    3
2    4
1    5



"""

for j in [26, 43]:
    result = []
    temp = j
    for i in range(len(arr)):
        print('i: %s, temp: %s' % (i, temp))
        if temp % 2 == 0:  # select
            result.append(i)
        temp = temp // 2
    print(result)
