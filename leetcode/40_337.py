#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

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



     3
    / \
   2   4
    \   \
     5   1

None - 偷 or 不偷
1 - 偷 or 不偷
0 - 不偷
opt(3, None)
    3+opt(2, 0)+opt(4, 0) 3+5+1
    0+opt(2, None)+opt(4, None) 0+5+1
    return 9


opt(2, 0)
    0+opt(5, None) 0+return 5
    return 5

opt(4, 0)
    0+opt(1, None) 0+return 1
    return 1

opt(2, None)
    2+opt(5, 0) 2+return 0
    0+opt(5, None) 0+return 5
    return 5

opt(4, None)
    1+opt(1, 0) 1+return 0
    0+opt(1, None) 0+return 1
    return 1

opt(5, None)
    return 5

opt(1, None)
    return 1

opt(5, 0)
    return 0

opt(1, 0)
    return 0


"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    cache = {}
    def max_rob(self, node, action):
        key = '%s%s' % (hash(node), action)
        if key in self.__class__.cache:
            return self.__class__.cache[key]
        result = 0
        if action == 1:
            if node.left is None and node.right is None:
                result = node.val
            elif node.left is not None and node.right is None:
                result = max(
                    node.val + self.max_rob(node.left, 0),
                    0 + self.max_rob(node.left, 1)
                )
            elif node.left is None and node.right is not None:
                result = max(
                    node.val + self.max_rob(node.right, 0),
                    0 + self.max_rob(node.right, 1)
                )
            else:
                result = max(
                    node.val + self.max_rob(node.left, 0) + self.max_rob(node.right, 0),
                    0 + self.max_rob(node.left, 1) + self.max_rob(node.right, 1)
                )
        else:
            # action == 0
            if node.left is None and node.right is None:
                result = 0
            elif node.left is not None and node.right is None:
                result = 0 + self.max_rob(node.left, 1)
            elif node.left is None and node.right is not None:
                result = 0 + self.max_rob(node.right, 1)
            else:
                result = 0 + self.max_rob(node.left, 1) + self.max_rob(node.right, 1)
        self.__class__.cache[key] = result
        return result


    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.__class__.cache = {}
        return self.max_rob(root, 1)
