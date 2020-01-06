"""
利用堆结构进行排序

从小到大升序 - 利用最大堆
从大到小降序 - 利用最小堆

原始序列：
99 5 36 7 22 17 46 12

1、最大堆化

"""


# 最大堆
def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index

    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index

    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        # heapify(unsorted, largest, heap_size)


if __name__ == '__main__':
    user_input = '99 5 36 7 22 17 46 12'
    unsorted = [int(item) for item in user_input.split(' ')]
    print('source unsorted: %s' % unsorted)  # [99, 5, 36, 7, 22, 17, 46, 12]

    # 最大堆化
    for i in range(len(unsorted) // 2 - 1, -1, -1):
        heapify(unsorted, i, len(unsorted))
    # print(unsorted)  # [99, 22, 46, 12, 5, 17, 36, 7]

    unsorted[0], unsorted[len(unsorted)-1] = unsorted[len(unsorted)-1], unsorted[0]
    # print(unsorted)  # [7, 22, 46, 12, 5, 17, 36, 99]

    heapify(unsorted, 0, len(unsorted)-1)
    # print(unsorted)  # [46, 22, 36, 12, 5, 17, 7, 99]

    unsorted[0], unsorted[len(unsorted) - 2] = unsorted[len(unsorted) - 2], unsorted[0]
    # print(unsorted)  # [7, 22, 36, 12, 5, 17, 46, 99]

    heapify(unsorted, 0, len(unsorted) - 2)
    # print(unsorted)  # [36, 22, 17, 12, 5, 7, 46, 99]
    unsorted[0], unsorted[len(unsorted) - 3] = unsorted[len(unsorted) - 3], unsorted[0]
    # print(unsorted)  # [7, 22, 17, 12, 5, 36, 46, 99]

    heapify(unsorted, 0, len(unsorted) - 3)
    # print(unsorted)  # [22, 12, 17, 7, 5, 36, 46, 99]
    unsorted[0], unsorted[len(unsorted) - 4] = unsorted[len(unsorted) - 4], unsorted[0]
    # print(unsorted)  # [5, 12, 17, 7, 22, 36, 46, 99]

    heapify(unsorted, 0, len(unsorted) - 4)
    # print(unsorted)  # [17, 12, 5, 7, 22, 36, 46, 99]
    unsorted[0], unsorted[len(unsorted) - 5] = unsorted[len(unsorted) - 5], unsorted[0]
    # print(unsorted)  # [7, 12, 5, 17, 22, 36, 46, 99]

    heapify(unsorted, 0, len(unsorted) - 5)
    # print(unsorted)  # [12, 7, 5, 17, 22, 36, 46, 99]
    unsorted[0], unsorted[len(unsorted) - 6] = unsorted[len(unsorted) - 6], unsorted[0]
    # print(unsorted)  # [5, 7, 12, 17, 22, 36, 46, 99]

    heapify(unsorted, 0, len(unsorted) - 6)
    print(unsorted)  # [7, 5, 12, 17, 22, 36, 46, 99]
    unsorted[0], unsorted[len(unsorted) - 7] = unsorted[len(unsorted) - 7], unsorted[0]
    print(unsorted)  # [5, 7, 12, 17, 22, 36, 46, 99]





