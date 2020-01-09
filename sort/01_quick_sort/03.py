#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://github.com/lanzhiwang/Python-Algorithms/blob/master/sorts/quick_sort.py
"""
def quick_sort(collection):
    length = len(collection)
    if length <= 1:
        return collection
    else:
        # Use the last element as the first pivot
        pivot = collection.pop()
        # Put elements greater than pivot in greater list
        # Put elements lesser than pivot in lesser list
        greater, lesser = [], []
        for element in collection:
            if element > pivot:
                greater.append(element)
            else:
                lesser.append(element)
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    # unsorted = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
    # print( quick_sort(unsorted) )

    for arr in [
        [], [0], [2], [3, 5], [5, 3], [5, 5], [0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 3, 5],
        [2, 5, 3, 0, 2, 3, 0, 3], [0, 2, 2, 3, 5],
        [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5], [-45, -2, -5]
    ]:
        print(arr)
        print(quick_sort(arr))
        # print(arr)
