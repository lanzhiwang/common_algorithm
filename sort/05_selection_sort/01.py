"""
简单选择排序
原始序列 99 5 36 7 22 17 46 12
N = 8

99 5 36 7 22 17 46 12
^
后续最小：5，交换 99 和 5


5 99 36 7 22 17 46 12
  ^
后续最小：7，交换 99 和 7


5 7 36 99 22 17 46 12
    ^
后续最小：12，交换 36 和 12


5 7 12 99 22 17 46 36
       ^
后续最小：17，交换 99 和 17


5 7 12 17 22 99 46 36
          ^
后续最小：22，不需要交换


5 7 12 17 22 99 46 36
             ^
后续最小：36，交换 99 和 36


5 7 12 17 22 36 46 99
                ^
后续最小：46，不需要交换


5 7 12 17 22 36 46 99

"""


def selection_sort(collection):
    for i in range(0, len(collection)-1):
        # print('i: %s' % i)
        # print('collection: %s' % collection)

        # temp = collection[i+1:]
        # min_element = min(temp)
        # min_element_index = temp.index(min_element) + i + 1
        # 或者
        min_element = min(collection[i+1:])
        min_element_index = collection.index(min_element, i)

        # print('min_element: %s' % min_element)
        # print('min_element_index: %s' % min_element_index)

        if min_element < collection[i]:
            collection[i], collection[min_element_index] = collection[min_element_index], collection[i]

        # print('collection: %s' % collection)


if __name__ == '__main__':
    unsorted = [2, 5, 3, 0, 2, 3, 0, 3]
    selection_sort(unsorted)
    print(unsorted)

    for unsorted in [
        [], [0], [2], [3, 5], [5, 3], [5, 5], [0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 3, 5],
        [2, 5, 3, 0, 2, 3, 0, 3], [0, 2, 2, 3, 5],
        [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5],
        [6, 1, 2, 7, 9, 3, 4, 5, 10, 8],
        [-45, -2, -5]
    ]:
        print(unsorted)
        selection_sort(unsorted)
        print(unsorted)
        print()
