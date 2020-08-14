#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
662. 二叉树最大宽度
给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。这个二叉树与满二叉树（full binary tree）结构相同，但一些节点为空。

每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度。

示例 1:

输入: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

输出: 4
解释: 最大值出现在树的第 3 层，宽度为 4 (5,3,null,9)。
示例 2:

输入: 

          1
         /  
        3    
       / \       
      5   3     

输出: 2
解释: 最大值出现在树的第 3 层，宽度为 2 (5,3)。
示例 3:

输入: 

          1
         / \
        3   2 
       /        
      5      

输出: 2
解释: 最大值出现在树的第 2 层，宽度为 2 (3,2)。
示例 4:

输入: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
输出: 8
解释: 最大值出现在树的第 4 层，宽度为 8 (6,null,null,null,null,null,null,7)。



               1-0
        /              \
       2-1              3-2
    /    \          /      \
   4-3    5-4      6-5     7-6
  / \    / \     /   \    /   \
 8   9 10  11  12   13  14   15
 7   8 9   10  11   12  13   14

i  l=2*i+1  r=2*i+2
0  1        2
1  3        4
2  5        6
3  7        8
4  9        10
5  11       12
6  13       14
7
8
9
10
11
12
13
14
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from queue import Queue

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        queue1 = Queue()
        queue2 = Queue()
        queue1.put((root, 0))
        max_width = 0
        while not queue1.empty() or not queue2.empty():
            min_max = []
            while not queue1.empty():
                node_tul = queue1.get()
                min_max.append(node_tul[1])

                if node_tul[0].left is not None:
                    queue2.put((node_tul[0].left, 2*node_tul[1]+1))

                if node_tul[0].right is not None:
                    queue2.put((node_tul[0].right, 2*node_tul[1]+2))
            if len(min_max) == 1:
                max_width = max(max_width, 1)
            else:
                max_width = max(max_width, min_max[-1] - min_max[0] + 1)

            min_max = []
            while not queue2.empty():
                node_tul = queue2.get()
                min_max.append(node_tul[1])

                if node_tul[0].left is not None:
                    queue1.put((node_tul[0].left, 2*node_tul[1]+1))

                if node_tul[0].right is not None:
                    queue1.put((node_tul[0].right, 2*node_tul[1]+2))
            if len(min_max) == 1:
                max_width = max(max_width, 1)
            else:
                max_width = max(max_width, min_max[-1] - min_max[0] + 1)
