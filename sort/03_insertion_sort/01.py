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

"""


def insertion_sort(collection):
    result = []
    for i in collection:
        if not result:
            result.append(i)
            continue
        for position in range(len(result)):
            if i < result[position]:
                result.insert(position, i)
            else:
                continue
    return result


if __name__ == '__main__':
    unsorted = [99, 5, 36, 7, 22, 17, 46, 12]
    print( insertion_sort(unsorted) )