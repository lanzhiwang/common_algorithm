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
        return 'val: %s, start: %s, end: %s, mid: %s' % (self.val, self.start, self.end, self.mid)


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

    def _update_tree(self, node, i, val):
        if node.start == i and node.end == i:
            node.val = val
            return
        if i <= node.mid:
            self._update_tree(node.left, i, val)
        else:
            self._update_tree(node.right, i, val)
        node.val = node.left.val + node.right.val

    def _sum_range(self, node, i, j):
        if node.start == i and node.end == j:
            return node.val
        if i <= node.mid:
            if j <= node.mid:
                return self._sum_range(node.left, i, j)
            else:
                return self._sum_range(node.left, i, node.mid) + self._sum_range(node.right, node.mid + 1, j)
        else:  # i > node.mid
            return self._sum_range(node.right, i, j)

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


"""
构建求和线段树
#####################################
build_tree(start=0, end=4)
    left = build_tree(start=0, end=2)  # return SegmentTreeNode()
    right = build_tree(start=3, end=4)  # return SegmentTreeNode()
    return SegmentTreeNode(start, end, left.val + right.val, left, right)

#####################################
build_tree(start=0, end=2)
    left = build_tree(start=0, end=1)  # return SegmentTreeNode()
    right = build_tree(start=2, end=2)  # return SegmentTreeNode()
    return SegmentTreeNode(start, end, left.val + right.val, left, right)

build_tree(start=3, end=4)
    left = build_tree(start=3, end=3)  # return SegmentTreeNode()
    right = build_tree(start=4, end=4)  # return SegmentTreeNode()
    return SegmentTreeNode(start, end, left.val + right.val, left, right)

#####################################
build_tree(start=0, end=1)
    left = build_tree(start=0, end=0)  # reutrn SegmentTreeNode(start, end, self.nums[start])
    right = build_tree(start=1, end=1)  # reutrn SegmentTreeNode(start, end, self.nums[start])
    return SegmentTreeNode(start, end, left.val + right.val, left, right)

build_tree(start=2, end=2)
    reutrn SegmentTreeNode(start, end, self.nums[start])

build_tree(start=3, end=3)
    reutrn SegmentTreeNode(start, end, self.nums[start])

build_tree(start=4, end=4)
    reutrn SegmentTreeNode(start, end, self.nums[start])

#####################################
build_tree(start=0, end=0)
    reutrn SegmentTreeNode(start, end, self.nums[start])
build_tree(start=1, end=1)
    return SegmentTreeNode(start, end, self.nums[start])

"""

r"""
更新求和线段树
            0-4(2)
           /     \
       0-2(1)   3-4(3)
      /    \     / \
   0-1(0) 2-2  3-3 4-4
  /  \
0-0 1-1
#####################################
update_tree(node=root, 1, 5)
    # start: 0, end: 4
    update_tree(node=root.left, 1, 5)
    node.val = node.left.val + node.right.val
    return

    update_tree(node=root.right, 1, 5)

#####################################
update_tree(node=root.left, 1, 5)
    # start: 0, end: 2
    update_tree(node=root.left.left, 1, 5)
    node.val = node.left.val + node.right.val
    return

    update_tree(node=root.left.right, 1, 5)

update_tree(node=root.right, 1, 5)
    # start: 3, end: 4
    update_tree(node=root.right.left, 1, 5)
    update_tree(node=root.right.right, 1, 5)

#####################################
update_tree(node=root.left.left, 1, 5)
    # start: 0, end: 1
    update_tree(node=root.left.left.left, 1, 5)
    update_tree(node=root.left.left.right, 1, 5)
    node.val = node.left.val + node.right.val
    return

update_tree(node=root.left.right, 1, 5)
    # start: 2, end: 2
    update_tree(node=root.left.right.left, 1, 5)
    update_tree(node=root.left.right.right, 1, 5)

update_tree(node=root.right.left, 1, 5)
    # start: 3, end: 3
    update_tree(node=root.right.left.left, 1, 5)
    update_tree(node=root.right.left.right, 1, 5)

update_tree(node=root.right.right, 1, 5)
    # start: 4, end: 4
    update_tree(node=root.right.right.left, 1, 5)
    update_tree(node=root.right.right.right, 1, 5)

#####################################
update_tree(node=root.left.left.right, 1, 5)
    # start: 1, end: 1
    node.val = val
    return

"""

r"""
求区间和

            0-4(2)
           /     \
       0-2(1)   3-4(3)
      /    \     / \
   0-1(0) 2-2  3-3 4-4
  /  \
0-0 1-1

0 1 2 3 4
mid=2
 i  j
[0, 0] left [0, 0]
[0, 1] left [0, 1]
[0, 2] left [0, 2]
[0, 3] left [0, 2] right [3, 3]
[0, 4]

[1, 1] left [1, 1]
[1, 2] left [1, 2]
[1, 3] left [1, 2] right [3, 3]
[1, 4] left [1, 2] right [3, 4]

[2, 2] left [2, 2]
[2, 3] left [2, 2] right [3, 3]
[2, 4] left [2, 2] right [3, 4]

i > mid
[3, 3] right [3, 3]
[3, 4] right [3, 4]

[4, 4] right [4, 4]


#####################################
sum_range(node=root, 1, 3)
    # start: 0, end: 4, mid: 2
    sum_range(node=root.left, 1, 3)
    sum_range(node=root.right, 1, 3)
    temp1 = sum_range(node=root.left, 1, 2)
    temp2 = sum_range(node=root.right, 3, 3)
    return temp1 + temp2

#####################################
sum_range(node=root.left, 1, 3)
sum_range(node=root.right, 1, 3)

sum_range(node=root.left, 1, 2)
    # start: 0, end: 2, mid: 1
    temp1 = sum_range(node=root.left.left, 1, 1)
    temp2 = sum_range(node=root.left.right, 2, 2)
    return temp1 + temp2

sum_range(node=root.right, 3, 3)
    return node.val

#####################################
sum_range(node=root.left.left, 1, 1)
    return node.val
sum_range(node=root.left.right, 2, 2)
    return node.val

"""

if __name__ == '__main__':
    num_arr = NumArray([2, 1, 5, 3, 4])
    for node in num_arr.traverse():
        print(node)
    print()
    """
    val: 15, start: 0, end: 4, mid: 2
    val: 8, start: 0, end: 2, mid: 1
    val: 7, start: 3, end: 4, mid: 3
    val: 3, start: 0, end: 1, mid: 0
    val: 5, start: 2, end: 2, mid: 2
    val: 3, start: 3, end: 3, mid: 3
    val: 4, start: 4, end: 4, mid: 4
    val: 2, start: 0, end: 0, mid: 0
    val: 1, start: 1, end: 1, mid: 1
    """
    num_arr.update(1, 5)
    for node in num_arr.traverse():
        print(node)
    print()
    """
    val: 19, start: 0, end: 4, mid: 2
    val: 12, start: 0, end: 2, mid: 1
    val: 7, start: 3, end: 4, mid: 3
    val: 7, start: 0, end: 1, mid: 0
    val: 5, start: 2, end: 2, mid: 2
    val: 3, start: 3, end: 3, mid: 3
    val: 4, start: 4, end: 4, mid: 4
    val: 2, start: 0, end: 0, mid: 0
    val: 5, start: 1, end: 1, mid: 1
    """

    print(num_arr.sum_range(3, 4))  # 7
    print(num_arr.sum_range(2, 2))  # 5
    print(num_arr.sum_range(1, 3))  # 13
