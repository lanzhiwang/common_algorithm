#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from queue import Queue


r"""
Segment Tree 线段树

参考
https://www.bilibili.com/video/av42192601/

求最大值线段树

原始数列: [2, 1, 5, 3, 4]
N = 5

1、build，求最大值

            0-4(2)
           /     \
       0-2(1)   3-4(3)
      /    \     / \
   0-1(0) 2-2  3-3 4-4
  /  \
0-0 1-1

       5
     /    \
    5      4
   / \    / \
  2   5  3   4
 / \
2   1

2、update index = 1 value = 5

找出区间 1-1
更新节点以及父节点

       5
     /    \
    5      4
   / \    / \
  2   5  3   4
 / \
2   5

       5
     /    \
    5      4
   / \    / \
  5   5  3   4
 / \
2   5

3、求区间最大值

            0-4(2)
           /     \
       0-2(1)   3-4(3)
      /    \     / \
   0-1(0) 2-2  3-3 4-4
  /  \
0-0 1-1

       5
     /    \
    5      4
   / \    / \
  5   5  3   4
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


class MaxArray:
    def __init__(self, nums):
        self.nums = nums
        if self.nums:
            self.root = self._build_tree(0, len(nums) - 1)

    def update(self, i, val):
        self._update_tree(self.root, i, val)

    def max_range(self, i, j):
        return self._max_range(self.root, i, j)

    def _build_tree(self, start, end):
        if start == end:
            return SegmentTreeNode(start, end, self.nums[start])
        mid = (start + end) // 2
        left = self._build_tree(start, mid)
        right = self._build_tree(mid + 1, end)
        return SegmentTreeNode(start, end, max([left.val, right.val]), left, right)

    def _update_tree(self, node, i, val):
        if node.start == i and node.end == i:
            node.val = val
            return
        if i <= node.mid:
            self._update_tree(node.left, i, val)
        else:
            self._update_tree(node.right, i, val)
        node.val = max(node.left.val, node.right.val)

    def _max_range(self, node, i, j):
        if node.start == i and node.end == j:
            return node.val

        if i <= node.mid:
            if j <= node.mid:
                return self._max_range(node.left, i, j)
            else:
                return max(self._max_range(node.left, i, node.mid), self._max_range(node.right, node.mid + 1, j))
        else:  # i > node.mid
            return self._max_range(node.right, i, j)

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
    max_arr = MaxArray([2, 1, 5, 3, 4])
    for node in max_arr.traverse():
        print(node)
    print()
    """
    val: 5, start: 0, end: 4
    val: 5, start: 0, end: 2
    val: 4, start: 3, end: 4
    val: 2, start: 0, end: 1
    val: 5, start: 2, end: 2
    val: 3, start: 3, end: 3
    val: 4, start: 4, end: 4
    val: 2, start: 0, end: 0
    val: 1, start: 1, end: 1
    """

    max_arr.update(1, 5)
    for node in max_arr.traverse():
        print(node)
    print()
    """
    val: 5, start: 0, end: 4
    val: 5, start: 0, end: 2
    val: 4, start: 3, end: 4
    val: 5, start: 0, end: 1
    val: 5, start: 2, end: 2
    val: 3, start: 3, end: 3
    val: 4, start: 4, end: 4
    val: 2, start: 0, end: 0
    val: 5, start: 1, end: 1
    """

    print(max_arr.max_range(3, 4))  # 4
    print(max_arr.max_range(2, 2))  # 5
    print(max_arr.max_range(1, 3))  # 5
