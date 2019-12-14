"""
冒泡排序

原始序列 12 35 99 18 76 - 从小到大 升序

12 35 99 18 7
12 35 18 99 7
12 35 18 7 99

12 35 18 7
12 18 35 7
12 18 7 35

12 18 7
12 7 18

12 7
7 12

"""


def bubble_sort(collection):
    if len(collection) <= 1:
        return collection
    max_element = max(collection)
    i = collection.index(max_element)
    return collection[0:i] + collection[i+1:] + [max_element]


if __name__ == '__main__':
    unsorted = [12, 35, 99, 18, 76]
    print(bubble_sort(unsorted))
