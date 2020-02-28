"""
https://www.cnblogs.com/chenkeyu/p/7505637.html

在最小化堆插入一个新数据：

当插入一个新值时，首先将值放到树的最后的位置
然后调整该值，也就是向上调整所有的父节点

原始最小堆：[1, 6, 4, 8, 7, 6, 5, 13, 12, 11]

插入数据：5

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
        heapify(unsorted, largest, heap_size)


if __name__ == '__main__':
    # 1 6 4 8 7 6 5 13 12 11
    min_heap = [1, 6, 4, 8, 7, 6, 5, 13, 12, 11]
    min_heap.append(5)
    print(min_heap)  # [1, 6, 4, 8, 7, 6, 5, 13, 12, 11, 5]

    r"""
             1
           /   \
          6     4
       /    \  / \
      8     7  6 5
     / \   / \
    13 12 11  5

             1
           /   \
          6     4
       /    \  / \
      8     5  6 5
     / \   / \
    13 12 11  7

             1
           /   \
          5     4
       /    \  / \
      8     6  6 5
     / \   / \
    13 12 11  7


    """
    i = 4
    while i >= 0:
        print(i)  # 4 1 0
        heapify(min_heap, i, len(min_heap))
        i = (i-1) // 2

    # heapify(min_heap, 4, len(min_heap))
    # heapify(min_heap, 1, len(min_heap))
    # heapify(min_heap, 0, len(min_heap))
    print(min_heap)  # [1, 5, 4, 8, 6, 6, 5, 13, 12, 11, 7]
