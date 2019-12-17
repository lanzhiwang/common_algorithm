"""
原始序列: [10, 5, 7, 3, 2, 8, 6]

[10, 5, 7, 3, 2, 8, 6]
[10, 5, 7] [3, 2, 8, 6]

[10, 5, 7]
[10] [5, 7]

"""


def merge(left, right):
    result = []
    while left and right:
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
    return result + left + right


def merge_sort(collection):
    length = len(collection)
    if length <= 1:
        return collection
    mid = len(collection) // 2
    return merge(merge_sort(collection[0:mid]), merge_sort(collection[mid:]))


if __name__ == '__main__':
    unsorted = [10, 5, 7, 3, 2, 8, 6]
    print(*merge_sort(unsorted), sep=',')
