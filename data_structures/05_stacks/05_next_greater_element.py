# -*- coding: utf-8 -*-

"""
获取第一个比自己大的数

[11, 13, 21, 3]
N = 4

i=0 j=1, 2, 3
i=1 j=2, 3
i=2 j=3
i=3 j=4

"""


def printNGE(arr):
    print(arr)
    for i in range(0, len(arr)):
        next = -1
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                next = arr[j]
                break

        print(str(arr[i]) + " -- " + str(next))


# Driver program to test above function
arr = [11, 13, 21, 3]
printNGE(arr)
"""
[11, 13, 21, 3]
11 -- 13
13 -- 21
21 -- -1
3 -- -1
"""