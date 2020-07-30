#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
606. 根据二叉树创建字符串
你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。

空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。

示例 1:

输入: 二叉树: [1,2,3,4]
       1
     /   \
    2     3
   /
  4

输出: "1(2(4))(3)"

解释: 原本将是“1(2(4)())(3())”，
在你省略所有不必要的空括号对之后，
它将是“1(2(4))(3)”。

示例 2:

输入: 二叉树: [1,2,3,null,4]
       1
     /   \
    2     3
     \
      4

输出: "1(2()(4))(3)"

解释: 和第一个示例相似，
除了我们不能省略第一个对括号来中断输入和输出之间的一对一映射关系。

       1
     /   \
    2     3
   /
  4

tree2str(1)
    tree2str(2) return 2(4)
    tree2str(3) return 3
    1(2(4))(3)

tree2str(2)
    tree2str(4) return 4
    tree2str(None) return ''
    return 2(4)

tree2str(3)
    tree2str(None) return ''
    tree2str(None) return ''
    return 3

tree2str(4)
    tree2str(None) return ''
    tree2str(None) return ''
    return 4

tree2str(None)
    return ''


       1
     /   \
    2     3
     \
      4

tree2str(1)
    tree2str(2) return 2()(4)
    tree2str(3) return 3
    return 1(2()(4))(3)

tree2str(2)
    tree2str(None) return ''
    tree2str(4) return 4
    return 2()(4)

tree2str(3)
    tree2str(None) return ''
    tree2str(None) return ''
    return 3

tree2str(4)
    tree2str(None) return ''
    tree2str(None) return ''
    return 4

tree2str(None)
    return ''


"""

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def list_to_tree(source_list, index=0):
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


def tree2str(node):
    if node is None:
        return ''
    left = tree2str(node.left)
    right =  tree2str(node.right)
    if left != '' and right != '':
        return '%s(%s)(%s)' % (node.value, left, right)
    elif left != '' and right == '':
        return '%s(%s)' % (node.value, left)
    elif left == '' and right != '':
        return '%s()(%s)' % (node.value, right)
    else:
        return '%s' % node.value

print tree2str(list_to_tree([1, 2, 3, None, 4]))
