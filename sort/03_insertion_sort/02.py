"""

原始序列 99 5 36 7 22 17 46 12  -  从小到大升序排序
     loop_index
[99, 5, 36, 7, 22, 17, 46, 12]

        loop_index
[5, 99, 36, 7, 22, 17, 46, 12]

            loop_index
[5, 36, 99, 7, 22, 17, 46, 12]

               loop_index
[5, 7, 36, 99, 22, 17, 46, 12]

                   loop_index
[5, 7, 22, 36, 99, 17, 46, 12]

                       loop_index
[5, 7, 17, 22, 36, 99, 46, 12]

                           loop_index
[5, 7, 17, 22, 36, 46, 99, 12]

[5, 7, 12, 17, 22, 36, 46, 99]

"""


def insertion_sort(collection):
    for loop_index in range(1, len(collection)):
        pivot = collection[loop_index]

        insertion_index = loop_index - 1
        while insertion_index >= 0:
            if collection[insertion_index] > pivot:
                collection[insertion_index+1] = collection[insertion_index]
                insertion_index -= 1
            else:
                collection[insertion_index + 1] = pivot
                break
        else:
            collection[insertion_index+1] = pivot


def insertion_sort_other(collection):
    for loop_index in range(1, len(collection)):
        pivot = collection[loop_index]

        insertion_index = loop_index - 1
        while insertion_index >= 0 and collection[insertion_index] > pivot:
            collection[insertion_index + 1] = collection[insertion_index]
            insertion_index -= 1
        else:
            collection[insertion_index+1] = pivot


if __name__ == '__main__':
    # unsorted = [99, 5, 36, 7, 22, 17, 46, 12]
    # insertion_sort_other(unsorted)
    # print(unsorted)

    for unsorted in [
        [], [0], [2], [3, 5], [5, 3], [5, 5], [0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 3, 5],
        [2, 5, 3, 0, 2, 3, 0, 3], [0, 2, 2, 3, 5],
        [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5],
        [6, 1, 2, 7, 9, 3, 4, 5, 10, 8],
        [-45, -2, -5], [99, 5, 36, 7, 22, 17, 46, 12]
    ]:
        print(unsorted)
        insertion_sort(unsorted)
        print(unsorted)
        print()
