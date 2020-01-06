r"""
https://www.cnblogs.com/chenkeyu/p/7505637.html
https://blog.csdn.net/qq_41437694/article/details/89575503

在最小化堆插入一个新数据：

当插入一个新值时，首先将值放到树的最后的位置
然后调整该值

原始最小堆：[1, 6, 4, 8, 7, 6, 5, 13, 12, 11]

插入数据：5

                      1-0
                /           \
              6-1          4-2
          /        \      /   \
        8-3       7-4   6-5  5-6
      /    \    /    \
    13-7 12-8 11-9  5-10

i  p p = (i - 1) // 2
10 4 (10 - 1) // 2
9  4 (9 - 1) // 2
8  3 (8 - 1) // 2
7  3 (7 - 1) // 2
6  2 (6 - 1) // 2
5  2 (5 - 1) // 2
4  1 (4 - 1) // 2
3  1 (3 - 1) // 2
2  0 (2 - 1) // 2
1  0 (1 - 1) // 2
0  None

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

    r"""
             1
           /   \ 
          6     4
       /    \  / \
      8     7  6  5
     / \   / \
    13 12 11  5
    
    """
    i = (len(min_heap) - 1 - 1) // 2
    while i >= 0:
        # print(i)  # 4 1 0
        heapify(min_heap, i, len(min_heap))
        i = (i - 1) // 2
    # heapify(min_heap, 4, len(min_heap))
    # heapify(min_heap, 3, len(min_heap))
    # heapify(min_heap, 2, len(min_heap))
    # heapify(min_heap, 1, len(min_heap))
    # heapify(min_heap, 0, len(min_heap))
    print(min_heap)  # [1, 5, 4, 8, 6, 6, 5, 13, 12, 11, 7]
