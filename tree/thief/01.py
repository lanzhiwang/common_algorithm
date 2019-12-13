#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
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

node0
[1, None, None, None, None, None]
[0, None, None, None, None, None]

node1
[1, 0, None, None, None, None]
[0, 1, None, None, None, None]
[0, 0, None, None, None, None]

node2
[1, 0, 0, None, None, None]
[0, 1, 1, None, None, None]
[0, 1, 0, None, None, None]
[0, 0, 1, None, None, None]
[0, 0, 0, None, None, None]

node3
[1, 0, 0, 1, None, None]
[1, 0, 0, 0, None, None]
[0, 1, 1, 0, None, None]
[0, 1, 0, 0, None, None]
[0, 0, 1, 1, None, None]
[0, 0, 1, 0, None, None]
[0, 0, 0, 1, None, None]
[0, 0, 0, 0, None, None]

node4
[1, 0, 0, 1, 1, None]
[1, 0, 0, 1, 0, None]
[1, 0, 0, 0, 1, None]
[1, 0, 0, 0, 0, None]
[0, 1, 1, 0, 0, None]
[0, 1, 0, 0, 0, None]
[0, 0, 1, 1, 1, None]
[0, 0, 1, 1, 0, None]
[0, 0, 1, 0, 1, None]
[0, 0, 1, 0, 0, None]
[0, 0, 0, 1, 1, None]
[0, 0, 0, 1, 0, None]
[0, 0, 0, 0, 1, None]
[0, 0, 0, 0, 0, None]

node5
[1, 0, 0, 1, 1, 1]
[1, 0, 0, 1, 1, 0]
[1, 0, 0, 1, 0, 1]
[1, 0, 0, 1, 0, 0]
[1, 0, 0, 0, 1, 1]
[1, 0, 0, 0, 1, 0]
[1, 0, 0, 0, 0, 1]
[1, 0, 0, 0, 0, 0]
[0, 1, 1, 0, 0, 0]
[0, 1, 0, 0, 0, 1]
[0, 1, 0, 0, 0, 0]
[0, 0, 1, 1, 1, 0]
[0, 0, 1, 1, 0, 0]
[0, 0, 1, 0, 1, 0]
[0, 0, 1, 0, 0, 0]
[0, 0, 0, 1, 1, 1]
[0, 0, 0, 1, 1, 0]
[0, 0, 0, 1, 0, 1]
[0, 0, 0, 1, 0, 0]
[0, 0, 0, 0, 1, 1]
[0, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 0, 1]
[0, 0, 0, 0, 0, 0]


[3, 0, 0, 1, 3, 1] 8
[3, 0, 0, 1, 3, 0] 7
[3, 0, 0, 1, 0, 1] 5
[3, 0, 0, 1, 0, 0] 4
[3, 0, 0, 0, 3, 1] 7
[3, 0, 0, 0, 3, 0] 6
[3, 0, 0, 0, 0, 1] 4
[3, 0, 0, 0, 0, 0] 3
[0, 4, 5, 0, 0, 0] 9 **
[0, 4, 0, 0, 0, 1] 5
[0, 4, 0, 0, 0, 0] 4
[0, 0, 5, 1, 3, 0] 9 **
[0, 0, 5, 1, 0, 0] 6
[0, 0, 5, 0, 3, 0] 8
[0, 0, 5, 0, 0, 0] 5
[0, 0, 0, 1, 3, 1] 5
[0, 0, 0, 1, 3, 0] 4
[0, 0, 0, 1, 0, 1] 2
[0, 0, 0, 1, 0, 0] 1
[0, 0, 0, 0, 3, 1] 4
[0, 0, 0, 0, 3, 0] 3
[0, 0, 0, 0, 0, 1] 1
[0, 0, 0, 0, 0, 0] 0

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


def foo(index, node, last_result):
    result = []

    if node.father == -1:
        result.append([1] + last_result[index + 1:])
        result.append([0] + last_result[index + 1:])
        return result
    else:
        for temp in last_result:
            if temp[node.father] == 1:  # 父节点 偷
                result.append(temp[0:index] + [0] + temp[index + 1:])
            else:  # 父节点 不偷
                result.append(temp[0:index] + [1] + temp[index + 1:])
                result.append(temp[0:index] + [0] + temp[index + 1:])
        return result


temp = [None, None, None, None, None, None]
result0 = []
result1 = []
result2 = []
result3 = []
result4 = []
result5 = []
for i in range(len(nodes)):
    if i == 0:
        result0 = foo(i, nodes[i], temp)
        print('result0: %s' % result0)

    if i == 1:
        result1 = foo(i, nodes[i], result0)
        print('result1: %s' % result1)

    if i == 2:
        result2 = foo(i, nodes[i], result1)
        print('result2: %s' % result2)

    if i == 3:
        result3 = foo(i, nodes[i], result2)
        print('result3: %s' % result3)

    if i == 4:
        result4 = foo(i, nodes[i], result3)
        print('result4: %s' % result4)

    if i == 5:
        result5 = foo(i, nodes[i], result4)
        print('result5: %s' % result5)

sums = []
for re in result5:
    sum = 0
    for r in range(len(re)):
        if re[r] == 1:
            sum += nodes[r].value
    sums.append(sum)
print(sums)
