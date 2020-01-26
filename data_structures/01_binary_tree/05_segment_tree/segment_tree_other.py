#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from queue import Queue
from collections.abc import Sequence


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


class SegmentTree(object):
    def __init__(self, collection: Sequence, function):
        self.collection = collection
        self.fn = function
        if self.collection:
            self.root = self._build_tree(0, len(collection) - 1)

    def update(self, i, val):
        self._update_tree(self.root, i, val)

    def query_range(self, i, j):
        return self._query_range(self.root, i, j)

    def _build_tree(self, start, end):
        if start == end:
            return SegmentTreeNode(start, end, self.collection[start])
        mid = (start + end) // 2
        left = self._build_tree(start, mid)
        right = self._build_tree(mid + 1, end)
        return SegmentTreeNode(start, end, self.fn(left.val, right.val), left, right)

    def _update_tree(self, root, i, val):
        if root.start == i and root.end == i:
            root.val = val
            return
        if i <= root.mid:
            self._update_tree(root.left, i, val)
        else:
            self._update_tree(root.right, i, val)
        root.val = self.fn(root.left.val, root.right.val)

    def _query_range(self, root, i, j):
        if root.start == i and root.end == j:
            return root.val
        """
         [i, j] [i, j] [i, j]
        [start mid] [mid+1 end]
        """
        if j <= root.mid:
            return self._query_range(root.left, i, j)
        elif i > root.mid:
            return self._query_range(root.right, i, j)
        else:
            return self.fn(self._query_range(root.left, i, root.mid), self._query_range(root.right, root.mid + 1, j))

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
    print('求和线段树')
    import operator
    num_arr = SegmentTree([2, 1, 5, 3, 4], operator.add)
    for node in num_arr.traverse():
        print(node)
    print()

    num_arr.update(1, 5)
    for node in num_arr.traverse():
        print(node)
    print()

    print(num_arr.query_range(3, 4))  # 7
    print(num_arr.query_range(2, 2))  # 5
    print(num_arr.query_range(1, 3))  # 13

    print()
    print('求最大值线段树')
    max_arr = SegmentTree([2, 1, 5, 3, 4], max)
    for node in max_arr.traverse():
        print(node)
    print()

    max_arr.update(1, 5)
    for node in max_arr.traverse():
        print(node)
    print()

    print(max_arr.query_range(3, 4))  # 4
    print(max_arr.query_range(2, 2))  # 5
    print(max_arr.query_range(1, 3))  # 5

    print()
    print('求最小值线段树')
    min_arr = SegmentTree([2, 1, 5, 3, 4], min)
    for node in min_arr.traverse():
        print(node)
    print()

    min_arr.update(1, 5)
    for node in min_arr.traverse():
        print(node)
    print()

    print(min_arr.query_range(3, 4))  # 3
    print(min_arr.query_range(2, 2))  # 5
    print(min_arr.query_range(1, 3))  # 3
