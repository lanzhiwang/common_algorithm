#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from queue import Queue


r"""
Segment Tree 线段树

参考
https://www.bilibili.com/video/av42192601/

求和线段树

原始数列: [2, 1, 5, 3, 4]
N = 5

1、build，求和

            0-4(2)
           /     \
       0-2(1)   3-4(3)
      /    \     / \
   0-1(0) 2-2  3-3 4-4
  /  \
0-0 1-1

       15
     /    \
    8      7
   / \    / \
  3   5  3   4
 / \
2   1

2、update index = 1 value = 5

找出区间 1-1
更新节点以及父节点

       15
     /    \
    8      7
   / \    / \
  3   5  3   4
 / \
2   5

       15
     /    \
    8      7
   / \    / \
  7   5  3   4
 / \
2   5

       15
     /    \
    12     7
   / \    / \
  7   5  3   4
 / \
2   5

       19
     /    \
    12     7
   / \    / \
  7   5  3   4
 / \
2   5

3、求区间和

            0-4(2)
           /     \
       0-2(1)   3-4(3)
      /    \     / \
   0-1(0) 2-2  3-3 4-4
  /  \
0-0 1-1

       19
     /    \
    12     7
   / \    / \
  7   5  3   4
 / \
2   5

[3, 4]
[2, 2]
[1, 3]


"""


class SegmentTreeNode(object):
    def __init__(self, start, end, val, left=None, right=None):
        self.start = start
        self.end = end
        self.val = val
        self.mid = (start + end) // 2
        self.left = left
        self.right = right

    def __str__(self):
        return 'val: %s, start: %s, end: %s' % (self.val, self.start, self.end)


class NumArray:
    def __init__(self, nums):
        self.nums = nums
        if self.nums:
            self.root = self._build_tree(0, len(nums) - 1)

    def update(self, i, val):
        self._update_tree(self.root, i, val)

    def sum_range(self, i, j):
        return self._sum_range(self.root, i, j)

    def _build_tree(self, start, end):
        if start == end:
            return SegmentTreeNode(start, end, self.nums[start])
        mid = (start + end) // 2
        left = self._build_tree(start, mid)
        right = self._build_tree(mid + 1, end)
        return SegmentTreeNode(start, end, left.val + right.val, left, right)

    def _update_tree(self, root, i, val):
        if root.start == i and root.end == i:
            root.val = val
            return
        if i <= root.mid:
            self._update_tree(root.left, i, val)
        else:
            self._update_tree(root.right, i, val)
        root.val = root.left.val + root.right.val

    def _sum_range(self, root, i, j):
        if root.start == i and root.end == j:
            return root.val
        """
         [i, j] [i, j] [i, j]
        [start mid] [mid+1 end]
        """
        if j <= root.mid:
            return self._sum_range(root.left, i, j)
        elif i > root.mid:
            return self._sum_range(root.right, i, j)
        else:
            return self._sum_range(root.left, i, root.mid) + self._sum_range(root.right, root.mid + 1, j)

    def traverse(self):
        result = []
        if self.root is not None:
            queue = Queue()
            queue.put(self.root)
            while not queue.empty():
                node = queue.get()
                result.append(node)

                if node.left is not None:
                    queue.put(node.left)

                if node.right is not None:
                    queue.put(node.right)
            return result


if __name__ == '__main__':
    num_arr = NumArray([2, 1, 5, 3, 4])
    for node in num_arr.traverse():
        print(node)
    print()
    """
    val: 15, start: 0, end: 4
    val: 8, start: 0, end: 2
    val: 7, start: 3, end: 4
    val: 3, start: 0, end: 1
    val: 5, start: 2, end: 2
    val: 3, start: 3, end: 3
    val: 4, start: 4, end: 4
    val: 2, start: 0, end: 0
    val: 1, start: 1, end: 1
    """
    num_arr.update(1, 5)
    for node in num_arr.traverse():
        print(node)
    print()
    """
    val: 19, start: 0, end: 4
    val: 12, start: 0, end: 2
    val: 7, start: 3, end: 4
    val: 7, start: 0, end: 1
    val: 5, start: 2, end: 2
    val: 3, start: 3, end: 3
    val: 4, start: 4, end: 4
    val: 2, start: 0, end: 0
    val: 5, start: 1, end: 1
    """

    print(num_arr.sum_range(3, 4))  # 7
    print(num_arr.sum_range(2, 2))  # 5
    print(num_arr.sum_range(1, 3))  # 13
