#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
543. 二叉树的直径
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。


示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

思路：
https://www.cnblogs.com/ariel-dreamland/p/9166216.html


注意：两结点之间的路径长度是以它们之间边的数目表示。

###############################

          1
         / \
        2   3
       / \
      4   5

diameter_of_binary_tree(1)
    diameter_of_binary_tree(2) return 2
    diameter_of_binary_tree(3) return 1
    max = 3
    return 3

diameter_of_binary_tree(2)
    diameter_of_binary_tree(4) return 1
    diameter_of_binary_tree(5) return 1
    max = 2
    return 2

diameter_of_binary_tree(3)
    diameter_of_binary_tree(None) return 0
    diameter_of_binary_tree(None) return 0
    max = 0
    return 1

diameter_of_binary_tree(4)
    diameter_of_binary_tree(None) return 0
    diameter_of_binary_tree(None) return 0
    max = 0
    return 1

diameter_of_binary_tree(5)
    diameter_of_binary_tree(None) return 0
    diameter_of_binary_tree(None) return 0
    max = 0
    return 1

diameter_of_binary_tree(None)
    return 0

###############################
空树
return 0

###############################

[1]

diameter_of_binary_tree(1)
    diameter_of_binary_tree(None) return 0
    diameter_of_binary_tree(None) return 0
    max

           1
        /     \
       2       3
          /         \
         4           5
      /     \       /
     6       7     8
    /      /   \
   9      10   11
  / \     /    /
12   13  14   15
 \   /        /
 16 17       18

直径最长路径之一：[16, 12, 9, 6, 4, 7, 11, 15, 18]

diameter_of_binary_tree(1)
    diameter_of_binary_tree(2) return 1
    diameter_of_binary_tree(3) return 6
    max = 7  max = diameter_of_binary_tree(2) + diameter_of_binary_tree(3))
    return 7  return max(diameter_of_binary_tree(2) + diameter_of_binary_tree(3)) + 1


diameter_of_binary_tree(2)
    diameter_of_binary_tree(None) return 0
    diameter_of_binary_tree(None) return 0
    max = 0
    return 1


diameter_of_binary_tree(3)
    diameter_of_binary_tree(4) return 5
    diameter_of_binary_tree(5) return 2
    max = 7
    return 6

diameter_of_binary_tree(4)
    diameter_of_binary_tree(6) return 4
    diameter_of_binary_tree(7) return 4
    max = 8
    return 5

diameter_of_binary_tree(5)
    diameter_of_binary_tree(8) return 1
    diameter_of_binary_tree(None) return 0
    max = 1
    return 2


diameter_of_binary_tree(6)
    diameter_of_binary_tree(9) return 3
    diameter_of_binary_tree(None) return 0
    max = 3
    return 4


diameter_of_binary_tree(7)
    diameter_of_binary_tree(10) return 2
    diameter_of_binary_tree(11) return 3
    max = 5
    return 4


diameter_of_binary_tree(8)
    diameter_of_binary_tree(None) return 0
    diameter_of_binary_tree(None) return 0
    max = 0
    return 1

diameter_of_binary_tree(9)
    diameter_of_binary_tree(12) return 2
    diameter_of_binary_tree(13) return 2
    max = 4
    return 3


diameter_of_binary_tree(10)
    diameter_of_binary_tree(14) return 1
    diameter_of_binary_tree(None) return 0
    max = 1
    return 2


diameter_of_binary_tree(11)
    diameter_of_binary_tree(15) return 2
    diameter_of_binary_tree(None) return 0
    max = 2
    return 3


diameter_of_binary_tree(12)
    diameter_of_binary_tree(None) return 0
    diameter_of_binary_tree(16) return 1
    max = 1
    return 2

diameter_of_binary_tree(13)
    diameter_of_binary_tree(17) return 1
    diameter_of_binary_tree(None) return 0
    max = 1
    return 2

diameter_of_binary_tree(14)
    diameter_of_binary_tree(None) return 0
    diameter_of_binary_tree(None) return 0
    max = 0
    return 1

diameter_of_binary_tree(15)
    diameter_of_binary_tree(18) return 1
    diameter_of_binary_tree(None) return 0
    max = 1
    return 2

diameter_of_binary_tree(16)
    diameter_of_binary_tree(None) return 0
    diameter_of_binary_tree(None) return 0
    max = 0
    return 1

diameter_of_binary_tree(17)
    diameter_of_binary_tree(None) return 0
    diameter_of_binary_tree(None) return 0
    max = 0
    return 1

diameter_of_binary_tree(18)
    diameter_of_binary_tree(None) return 0
    diameter_of_binary_tree(None) return 0
    max = 0
    return 1

diameter_of_binary_tree(None)
    return 0

空树
return 0

一个节点的树
 1

diameter_of_binary_tree(1)
    diameter_of_binary_tree(None) return 0
    diameter_of_binary_tree(None) return 0
    max = 0
    return 1
"""

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def list_to_tree(source_list, index):
    if not source_list:
        return None
    try:
        value = source_list[index]
        if value is None:
            return None
    except IndexError:
        return None

    root = Node(value)
    root.left = list_to_tree(source_list, 2 * index + 1)
    root.right = list_to_tree(source_list, 2 * index + 2)
    return root

result = 0
def diameter_of_binary_tree(node):
    global result
    if node is None:
        return 0
    left = diameter_of_binary_tree(node.left)
    right = diameter_of_binary_tree(node.right)
    result = max(result, left + right)
    return max(left, right) + 1

diameter_of_binary_tree(list_to_tree([1, 2], 0))
print result

