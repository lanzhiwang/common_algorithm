"""

原始序列 99 5 36 7 22 17 46 12  -  从小到大升序排序

[99]
[5, 99]
[5, 36, 99]
[5, 7, 36, 99]
[5, 7, 22, 36, 99]
[5, 7, 17, 22, 36, 99]
[5, 7, 17, 22, 36, 46, 99]
[5, 7, 12, 17, 22, 36, 46, 99]


[99, 5, 36, 7, 22, 17, 46, 12]
 ^
[99, 5, 36, 7, 22, 17, 46, 12]

[99, 5, 36, 7, 22, 17, 46, 12]
     ^
[5, 99, 36, 7, 22, 17, 46, 12]

[5, 99, 36, 7, 22, 17, 46, 12]
        ^
[5, 36, 99, 7, 22, 17, 46, 12]

[5, 36, 99, 7, 22, 17, 46, 12]
            ^
[5, 7, 36, 99, 22, 17, 46, 12]

[5, 7, 36, 99, 22, 17, 46, 12]
               ^
[5, 7, 22, 36, 99, 17, 46, 12]

[5, 7, 22, 36, 99, 17, 46, 12]
                   ^
[5, 7, 17, 22, 36, 99, 46, 12]

[5, 7, 17, 22, 36, 99, 46, 12]
                       ^
[5, 7, 17, 22, 46, 36, 99, 12]

[5, 7, 17, 22, 46, 36, 99, 12]
                           ^
[5, 7, 12, 17, 22, 46, 36, 99]

"""


def insertion_sort(collection):
    length = len(collection)
    if length <= 1:
        return collection
    result = [collection[0]]
    for i in range(1, length):
        # print('i: %s, collection[%s]: %s' % (i, i, collection[i]))
        # print('result: %s' % result)
        for position in range(len(result)):
            if collection[i] < result[position]:
                result.insert(position, collection[i])
                break
        else:
            result.append(collection[i])
        # print('result: %s' % result)
    return result


if __name__ == '__main__':
    # unsorted = [99, 5, 36, 7, 22, 17, 46, 12]
    # print(insertion_sort(unsorted))

    for unsorted in [
        [], [0], [2], [3, 5], [5, 3], [5, 5], [0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 3, 5],
        [2, 5, 3, 0, 2, 3, 0, 3], [0, 2, 2, 3, 5],
        [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5],
        [6, 1, 2, 7, 9, 3, 4, 5, 10, 8],
        [-45, -2, -5], [99, 5, 36, 7, 22, 17, 46, 12]
    ]:
        print(unsorted)
        print(insertion_sort(unsorted))
        print()
