"""
希尔排序
原始序列 8 9 1 7 2 3 5 4 6 0 -- 从小到大升序排序

N = 10 增量序列 [5 2 1]  # N = 9 增量序列 [4 2 1]

增量为5，分为5组，每组2个元素
下标：0 1 2 3 4 5 6 7 8 9
序列：8 9 1 7 2 3 5 4 6 0
分组：[8 3] [9 5] [1 4] [7 6] [2 0]
排序：[3 8] [5 9] [1 4] [6 7] [0 2]
合并：3 5 1 6 0 8 9 4 7 2

增量为2，分为2组，每组5个元素
下标：0 1 2 3 4 5 6 7 8 9
序列：3 5 1 6 0 8 9 4 7 2
分组：[3 1 0 9 7] [5 6 8 4 2]
排序：[0 1 3 7 9] [2 4 5 6 8]
合并：0 2 1 4 3 5 7 6 9 8

增量为1，分为1组，每组10个元素
下标：0 1 2 3 4 5 6 7 8 9
序列：0 2 1 4 3 5 7 6 9 8



"""


def quick_sort_3partition(sorting, left, right):
    if right <= left:
        return
    a = i = left
    b = right
    pivot = sorting[left]
    while i <= b:
        if sorting[i] < pivot:
            sorting[a], sorting[i] = sorting[i], sorting[a]
            a += 1
            i += 1
        elif sorting[i] > pivot:
            sorting[b], sorting[i] = sorting[i], sorting[b]
            b -= 1
        else:
            i += 1
    quick_sort_3partition(sorting, left, a - 1)
    quick_sort_3partition(sorting, b + 1, right)


def shell_sort(collection):
    result = []
    length = len(collection)
    if length <= 1:
        return collection
    increment = [length // 2]
    while (increment[-1] // 2) >= 1:
        increment.append(increment[-1] // 2)
    for step in increment:  # [5, 2, 1]
        temp = []
        for i in range(step):
            temp.append(collection[i::step])
        print(temp)
        for l in temp:
            quick_sort_3partition(l, 0, len(l)-1)
        print(temp)



if __name__ == '__main__':
    unsorted = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
    # unsorted = [6, 1, 2, 7, 9, 3, 4, 5, 10]
    shell_sort(unsorted)
    print(unsorted)
