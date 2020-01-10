"""
冒泡排序

原始序列 12 35 99 18 76 - 从小到大 升序

"""


def bubble_sort(collection, index):
    if index == 0 or len(collection) <= 1:
        return
    max_element = None
    for i in range(0, index+1):
        if max_element is None:
            max_element = collection[i]
        else:
            if collection[i] > max_element:
                max_element = collection[i]

    i = collection.index(max_element)
    if i != index:
        collection[index], collection[i] = collection[i], collection[index]
    bubble_sort(collection, index-1)


if __name__ == '__main__':
    # unsorted = [12, 35, 99, 18, 76]
    # bubble_sort(unsorted, len(unsorted)-1)
    # print(unsorted)

    for unsorted in [
        [], [0], [2], [3, 5], [5, 3], [5, 5], [0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 3, 5],
        [2, 5, 3, 0, 2, 3, 0, 3], [0, 2, 2, 3, 5],
        [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5],
        [6, 1, 2, 7, 9, 3, 4, 5, 10, 8],
        [-45, -2, -5]
    ]:
        print(unsorted)
        bubble_sort(unsorted, len(unsorted) - 1)
        print(unsorted)
        print()
