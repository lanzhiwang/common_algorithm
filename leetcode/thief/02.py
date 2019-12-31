#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/house-robber-iii/

在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。
除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:
输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.

示例 2:
输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1


输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.

"""


# 先遍历出有多少种偷法

"""

        3-0
      /     \
    4-1    5-2
   /   \     \
 1-3   3-4   1-5

第一种情况
[]
[1]
[1, 0]
[1, 0, 0]
[1, 0, 0, 1]
[1, 0, 0, 1, 1]
[1, 0, 0, 1, 1, 1]

第二种情况
[]
[0]
[0, 0]
[0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]

第三种情况
[]
[0]
[0, 1]
[0, 1, 1]
[0, 1, 1, 0]
[0, 1, 1, 0, 0]
[0, 1, 1, 0, 0, 0]

第四种情况
[]

"""


class Node(object):
    def __init__(self, value, left, right, father):
        self.value = value
        self.left = left
        self.right = right
        self.father = father

    def __str__(self):
        return 'value=%s, left=%s, right=%s, father=%s' % (self.value, self.left, self.right, self.father)


node0 = Node(3, 1, 2, -1)
node1 = Node(4, 3, 4, 0)
node2 = Node(5, -1, 5, 0)
node3 = Node(1, -1, -1, 1)
node4 = Node(3, -1, -1, 1)
node5 = Node(1, -1, -1, 2)

nodes = [node0, node1, node2, node3, node4, node5]


def foo(nodes, last_result):
    if len(last_result) == len(nodes):
        print('%s' % last_result)
        return last_result

    i = len(last_result)
    if nodes[i].father == -1:
        foo(nodes, [0])
        foo(nodes, [1])
    else:
        """
        if last_result[nodes[i].father] == 1:
            foo(nodes, last_result[0:i] + [0])
        if last_result[nodes[i].father] == 0:
            foo(nodes, last_result[0:i] + [1])
            foo(nodes, last_result[0:i] + [0])
        """
        foo(nodes, last_result[0:i] + [0])
        if last_result[nodes[i].father] == 0:
            foo(nodes, last_result[0:i] + [1])


foo(nodes, [])
