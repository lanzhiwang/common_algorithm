#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
96. 不同的二叉搜索树
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


generate_trees([1, 2, 3, 4, 5])
    generate_trees([]) root = 1 generate_trees([2, 3, 4, 5])
        return []
        return 14
        14

    generate_trees([1]) root = 2 generate_trees([3, 4, 5])
        return [root(1)]
        return 5
        5

    generate_trees([1, 2]) root = 3 generate_trees([4, 5])
        return [root(1), root(2)]
        return [root(4), root(5)]
        4

    generate_trees([1, 2, 3]) root = 4 generate_trees([5])
        return 5
        return [root(5)]
        5

    generate_trees([1, 2, 3, 4]) root = 5 generate_trees([])
        return 14
        return []
        14
    return 14+5+4+5+14

generate_trees([2, 3, 4, 5])
    generate_trees([]) root = 2 generate_trees([3, 4, 5])
    generate_trees([2]) root = 3 generate_trees([4, 5])
    generate_trees([2, 3]) root = 4 generate_trees([5])
    generate_trees([2, 3, 4]) root = 5 generate_trees([])
    return 14

generate_trees([1, 2, 3, 4])
    generate_trees([]) root = 1 generate_trees([2, 3, 4])
        return []
        return 5
        0+5
    generate_trees([1]) root = 2 generate_trees([3, 4])
        return [root(1)]
        return [root(3), root(4)]
        2
    generate_trees([1, 2]) root = 3 generate_trees([4])
        return [root(1), root(2)]
        return [root(4)]
        2
    generate_trees([1, 2, 3]) root = 4 generate_trees([])
        return 5
        return []
        5
    return 5+2+2+5 = 14

generate_trees([3, 4, 5])
    generate_trees([]) root = 3 generate_trees([4, 5])
    generate_trees([3]) root = 4 generate_trees([5])
    generate_trees([3, 4]) root = 5 generate_trees([])
    return 5

generate_trees([1, 2, 3])
    generate_trees([]) root = 1 generate_trees([2, 3])
    generate_trees([1]) root = 2 generate_trees([3])
    generate_trees([1, 2]) root = 3 generate_trees([])
    return 5

generate_trees([2, 3, 4])
    generate_trees([]) root = 2 generate_trees([3, 4])
        return []
        return [root(3), root(4)]
        2
    generate_trees([2]) root = 3 generate_trees([4])
        return [root(2)]
        return [root(4)]
        1

    generate_trees([2, 3]) root = 4 generate_trees([])
        return [root(2), root(3)]
        return []
        2

    return 2+2+2 = 5

generate_trees([1, 2])
    return [root(1), root(2)]

generate_trees([2, 3])
    return [root(2), root(3)]

generate_trees([4, 5])
    return [root(4), root(5)]

generate_trees([3, 4])
    return [root(3), root(4)]

generate_trees([1])
    return [root(1)]

generate_trees([5])
    return [root(5)]

generate_trees([2])
    return [root(2)]

generate_trees([4])
    return [root(4)]

generate_trees([3])
    return [root(3)]

generate_trees([])
    return []

"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        """
        5
        0+1+4
        1+1+3
        2+1+2
        3+1+1
        4+1+0
        """
        result_dict = {0: 0, 1: 1, 2: 2}
        result = 0
        for i in range(n):
            if i in result_dict:
                left_num = result_dict[i]
            else:
                left_num = self.numTrees(i)
                result_dict[i] = left_num

            if (n - i - 1) in result_dict:
                right_num = result_dict[n - i - 1]
            else:
                right_num = self.numTrees(n - i - 1)
                result_dict[n - i - 1] = right_num

            if left_num != 0 and right_num != 0:
                result += (left_num * right_num)
            elif left_num == 0 and right_num != 0:
                result += right_num
            elif left_num != 0 and right_num == 0:
                result += left_num
            else:
                pass
        return result

print(Solution().numTrees(3))
