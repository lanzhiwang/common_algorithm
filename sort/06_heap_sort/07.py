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

    for j in range(len(unsorted)-1, 0, -1):
        unsorted[0], unsorted[j] = unsorted[j], unsorted[0]
        heapify(unsorted, 0, j)
    print(unsorted)
