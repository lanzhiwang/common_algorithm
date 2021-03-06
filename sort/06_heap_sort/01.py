r"""
最大堆化

source unsorte：
99 5 36 7 22 17 46 12
N = 8

                 99-0
             /         \
           5-1        36-2
         /    \      /   \
       7-3  22-4   17-5 46-6
        /
     12-7

找到最后一个叶子节点 12-7
找到最后一个叶子节点的父节点 7-3
3 = 8 // 2 - 1

根据节点位置确定左右子节点位置
i -> 2i+1 2i+2
0 -> 1 2
1 -> 3 4
2 -> 5 6
3 -> 7 -1
4 -> -1 -1
5 -> -1 -1
6 -> -1 -1
7 -> -1 -1


根据节点位置确定父节点
i -> (i-1)//2
0 -> -1
1 -> 0
2 -> 0
3 -> 1
4 -> 1
5 -> 2
6 -> 2
7 -> 3


heapify(unsorted, 3, 8)
[99, 5, 36, 12, 22, 17, 46, 7]


            99
          /    \
         5      36
        / \     / \
       12  22   17 46
      /
      7


heapify(unsorted, 2, 8)
[99, 5, 46, 12, 22, 17, 36, 7]


            99
          /    \
         5      46
        / \     / \
       12  22   17 36
      /
      7


heapify(unsorted, 1, 8)
[99, 22, 46, 12, 5, 17, 36, 7]


            99
          /    \
         22      46
        / \     / \
       12  5   17 36
      /
      7


heapify(unsorted, 0, 8)
[99, 22, 46, 12, 5, 17, 36, 7]


            99
          /    \
         22      46
        / \     / \
       12  5   17 36
      /
      7

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
        heapify(unsorted, largest, heap_size)


if __name__ == '__main__':
    user_input = '99 5 36 7 22 17 46 12'
    unsorted = [int(item) for item in user_input.split(' ')]
    print('source unsorted: %s' % unsorted)  # [99, 5, 36, 7, 22, 17, 46, 12]

    heapify(unsorted, 3, 8)
    print(unsorted)  # [99, 5, 36, 12, 22, 17, 46, 7]

    heapify(unsorted, 2, 8)
    print(unsorted)  # [99, 5, 46, 12, 22, 17, 36, 7]

    heapify(unsorted, 1, 8)
    print(unsorted)  # [99, 22, 46, 12, 5, 17, 36, 7]

    heapify(unsorted, 0, 8)
    print(unsorted)  # [99, 22, 46, 12, 5, 17, 36, 7]
