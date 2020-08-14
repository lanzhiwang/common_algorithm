#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
655. 输出二叉树
在一个 m*n 的二维字符串数组中输出二叉树，并遵守以下规则：

行数 m 应当等于给定二叉树的高度。
列数 n 应当总是奇数。
根节点的值（以字符串格式给出）应当放在可放置的第一行正中间。根节点所在的行与列会将剩余空间划分为两部分（左下部分和右下部分）。你应该将左子树输出在左下部分，右子树输出在右下部分。左下和右下部分应当有相同的大小。即使一个子树为空而另一个非空，你不需要为空的子树输出任何东西，但仍需要为另一个子树留出足够的空间。然而，如果两个子树都为空则不需要为它们留出任何空间。
每个未使用的空间应包含一个空的字符串""。
使用相同的规则输出子树。
示例 1:

输入:
     1
    /
   2
输出:
[["", "1", ""],
 ["2", "", ""]]

1+1+1
1

2
1 3  1

示例 2:

输入:
     1
    / \
   2   3
    \
     4
输出:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["4", "", "4", "", "4", "", "4"]]

3+1+3
1+1+1
1

4
2 6       2
1 3 5 7   1

示例 3:

输入:
               1
        /              \
       2                3
    /    \          /      \
   4      5        6        7
  / \    / \     /   \    /   \
 8   9  10  11  12   13  14   15
输出:
[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "3", "", "",  "",  "3",  "",  "",  "", "3", ""]
 ["4", "",  "4", "",  "4", "", "4", "",  "4",  "",  "4",  "",  "4", "", "4"]]
注意: 二叉树的高度在范围 [1, 10] 中。

7+1+7
3+1+3
1+1+1
1

              8
      4              12             4
  2      6      10       14         2
1   3  5   7  9   11  13   15       1


print_tree(1, -8, 16)
    8
    print_tree(2, -4, 8)
    print_tree(3, +4, 8)

print_tree(2, -4, 8)
    4
    print_tree(4, -2, 4)
    print_tree(5, +2, 4)

print_tree(3, +4, 8)
    12
    print_tree(6, -2, 12)
    print_tree(7, +2, 12)

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    row_column = []
    def depth_of_tree(self, tree):
        if tree is None:
            return 0
        else:
            depth_l_tree = self.depth_of_tree(tree.left)
            depth_r_tree = self.depth_of_tree(tree.right)
            if depth_l_tree > depth_r_tree:
                return 1 + depth_l_tree
            else:
                return 1 + depth_r_tree

    def get_column(self, row):
        result = []
        for i in range(row):
            if result:
                result.append(result[-1]+1+result[-1])
            else:
                result.append(1)
        return result[-1]

    def print_tree(self, node, step, position, row):
        index = position + step
        self.__class__.row_column[row][index-1] = '%s' % node.val
        if node.left is not None:
            self.print_tree(node.left, abs(step) / (-2), index, row + 1)
        if node.right is not None:
            self.print_tree(node.right, abs(step) / (2), index, row + 1)

    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if root is None:
            return []
        row = self.depth_of_tree(root)
        column = self.get_column(row)
        self.__class__.row_column = []
        for _ in range(row):
            self.__class__.row_column.append([''] * column)
        self.print_tree(root, (column + 1) / (-2), column + 1, 0)
        return self.__class__.row_column


"""
