"""
冒泡排序

原始序列 12 35 99 18 76 - 从小到大 升序

12 35 99 18 76
12 35 18 99 76
12 35 18 76 99

12 35 18 76
12 18 35 76
12 18 7 35

12 18 76
12 76 18

12 76
76 12

"""


def bubble_sort(collection):
    length = len(collection)
    if length <= 1:
        return collection

    max_element = max(collection)
    i = collection.index(max_element)
    collection[i], collection[length-1] = collection[length-1], collection[i]
    bubble_sort(collection[0:length-2])


if __name__ == '__main__':
    unsorted = [12, 35, 99, 18, 76]
    bubble_sort(unsorted)
    print(unsorted)
