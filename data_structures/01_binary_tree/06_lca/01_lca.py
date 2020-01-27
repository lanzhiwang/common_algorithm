#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
参考：
https://blog.csdn.net/pikachu_777/article/details/85222995
https://www.hrwhisper.me/algorithm-lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor of two given nodes in the tree. 给定一棵二叉树，求最近公共祖先。

对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。

二叉搜索树 BST

      6
   /    \
  2      8
 / \    / \
0   4  7   9
   / \
  3   5

LCA(2, 8) = 6
LCA(2, 4) = 2
LCA(0, 5) = 2

思路：
1、若 q 和 p 分别在 root 的左子树和右子树内，则 root 就是 LCA。
2、若 q 和 p 都在 root 左子树内，则 LCA 也在左子树内。
3、若 q 和 p 都在 root 右子树内，则 LCA 也在右子树内。

因此递归求解：

1、若当前 root 为 None，或 root 为 q 或 p，则返回 root。
2、否则分别遍历左右子树。
3、若左右子树分别找到 q 和 p，返回 root。
4、否则，说明 p 和 q 都在某一个子树内，返回这个子树的递归结果。

"""
