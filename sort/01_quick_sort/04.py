#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://github.com/lanzhiwang/Python-Algorithms/blob/master/sorts/quick_sort_3_partition.py

快速排序 - 从小到大升序排序
array 6 1 6 2 7 9 3 4 5 10 8

pivot = 6
i = 0
6 1 6 2 7 9 3 4 5 10 8
a                    b

i = 1
6 1 6 2 7 9 3 4 5 10 8
a                    b

i = 2
1 6 6 2 7 9 3 4 5 10 8
  a                  b

i = 3
1 6 6 2 7 9 3 4 5 10 8
  a                  b

i = 4
1 2 6 6 7 9 3 4 5 10 8
      a              b

i = 4
1 2 6 6 8 9 3 4 5 10 7
      a           b

i = 4
1 2 6 6 10 9 3 4 5 8 7
      a          b

i = 4
1 2 6 6 5 9 3 4 10 8 7
      a       b

i = 5
1 2 6 5 6 9 3 4 10 8 7
        a     b

i = 5
1 2 6 5 6 4 3 9 10 8 7
        a   b

i = 5
1 2 6 5 4 6 3 9 10 8 7
          a b

i = 6
1 2 6 5 4 3 6 9 10 8 7
            ab
[1, 2, 5, 4, 3, 6, 9, 10, 8, 7]
"""
def quick_sort_3partition(sorting, left, right):
    if right <= left:
        return
    a = i = left
    b = right
    pivot = sorting[left]
    while i <= b:
        if sorting[i] < pivot:
            sorting[a], sorting[i] = sorting[i], sorting[a]
            a += 1
            i += 1
        elif sorting[i] > pivot:
            sorting[b], sorting[i] = sorting[i], sorting[b]
            b -= 1
        else:
            i += 1
    quick_sort_3partition(sorting, left, a - 1)
    quick_sort_3partition(sorting, b + 1, right)


if __name__ == '__main__':
    unsorted = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
    quick_sort_3partition(unsorted, 0, len(unsorted)-1)
    print(unsorted)