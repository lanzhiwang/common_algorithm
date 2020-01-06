"""
https://www.cnblogs.com/chenkeyu/p/7505637.html

在最小化堆中取出最小值：

在最小堆中，拿出一个最小值，也就是拿出第一个数

然后把最后一个数放到头的位置，这样树的结构就不会改变，而且操作简单

最后调整最小堆

原始最小堆：[1, 6, 4, 8, 7, 6, 5, 13, 12, 11]


"""


# 最小堆
def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    if left_index < heap_size and unsorted[left_index] < unsorted[largest]:
        largest = left_index

    if right_index < heap_size and unsorted[right_index] < unsorted[largest]:
        largest = right_index

    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        # heapify(unsorted, largest, heap_size)


if __name__ == '__main__':
    # 1 6 4 8 7 6 5 13 12 11
    min_heap = [1, 6, 4, 8, 7, 6, 5, 13, 12, 11]

    min = min_heap[0]
    print(min)

    min_heap[0] = min_heap.pop(-1)
    print(min_heap)  # [11, 6, 4, 8, 7, 6, 5, 13, 12]

    heapify(min_heap, 0, len(min_heap))
    print(min_heap)  # [4, 6, 5, 8, 7, 6, 11, 13, 12]
