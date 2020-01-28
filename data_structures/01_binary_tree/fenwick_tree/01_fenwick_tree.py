#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
树状数组或二叉索引树（Binary Indexed Tree, Fenwick Tree）

参考：
https://www.bilibili.com/video/av26371798/

定义：
原始数组：A = []
树状数组：C = []
C[1] = A[1]
C[2] = A[1] + A[2]
C[3] = A[3]
C[4] = A[1] + A[2] + A[3] + A[4]
C[5] = A[5]
C[6] = A[5] + A[6]
C[7] = A[7]
C[8] = A[1] + A[2] + A[3] + A[4] + A[5] + A[6] + A[7] + A[8]
...

                                                                    二进制低位 0 的个数
                                                                           |
                                                                           V
C[1] = C[0001] = A[1]                                                   2**0 = 1 <- low_bit(1)
C[2] = C[0010] = A[1] + A[2]                                            2**1 = 2 <- low_bit(2)
C[3] = C[0011] = A[3]                                                   2**0 = 1 <- low_bit(3)
C[4] = C[0100] = A[1] + A[2] + A[3] + A[4]                              2**2 = 4 <- low_bit(4)
C[5] = C[0101] = A[5]                                                   2**0 = 1 <- low_bit(5)
C[6] = C[0110] = A[5] + A[6]                                            2**1 = 2 <- low_bit(6)
C[7] = C[0111] = A[7]                                                   2**0 = 1 <- low_bit(7)
C[8] = C[1000] = A[1] + A[2] + A[3] + A[4] + A[5] + A[6] + A[7] + A[8]  2**3 = 8 <- low_bit(8)

     转为二进制 二进制低位1 转为十进制
1 -> 0001     -> 0001   -> 1
2 -> 0010     -> 0010   -> 2
3 -> 0011     -> 0001   -> 1
4 -> 0100     -> 0100   -> 4
5 -> 0101     -> 0001   -> 1
6 -> 0110     -> 0010   -> 2
7 -> 0111     -> 0001   -> 1
8 -> 1000     -> 1000   -> 8

low_bit 就是最低位上的 1 代表的数

C[i] = A[i - low_bit(i) + 1] + ... + A[i]

C[1] = A[1 - 1 + 1] + ... + A[i] [1, 1]
C[2] = A[2 - 2 + 1] + ... + A[i] [1, 2]
C[3] = A[3 - 1 + 1] + ... + A[i] [3, 3]
C[4] = A[4 - 4 + 1] + ... + A[i] [1, 4]
C[5] = A[5 - 1 + 1] + ... + A[i] [5, 5]
C[6] = A[6 - 2 + 1] + ... + A[i] [5, 6]
C[7] = A[7 - 1 + 1] + ... + A[i] [7, 7]
C[8] = A[8 - 8 + 1] + ... + A[i] [1, 8]



i p = i + low_bit(i)
1 2 = 1 + 1
2 4 = 2 + 2
3 4 = 3 + 1
4 8 = 4 + 4
5 6 = 5 + 1
6 8 = 6 + 2
7 8 = 7 + 1
8 16 = 8 + 8


         C[8]
     /     \     \
   C[4]    C[6] C[7]
   /  \     /
 C[2] C[3] C[5]
 /
C[1]

"""


def low_bit(n):
    return n & (-n)


def update(c, i, k):
    """
    A[i] = A[i] + k
    """
    while True:
        c[i] = c[i] + k
        i = i + low_bit(i)
        if i > len(c):
            break


def sum_range(c, i):
    """
    A[1] + A[2] + ... + A[i]
    """
    ans = 0
    while True:
        ans = c[i] + ans
        i = i - low_bit(i)
        if i < 0:
            break


if __name__ == '__main__':
    print(low_bit(1))  # 1
    print(low_bit(2))  # 2
    print(low_bit(3))  # 1
    print(low_bit(4))  # 4
    print(low_bit(5))  # 1
    print(low_bit(6))  # 2
    print(low_bit(7))  # 1
    print(low_bit(8))  # 8
