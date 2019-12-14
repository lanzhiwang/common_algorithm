"""

原始序列 99 5 36 7 22 17 46 12  -  从小到大升序排序

[99, 5, 36, 7, 22, 17, 46, 12]
[5, 99, 36, 7, 22, 17, 46, 12]
[5, 36, 99, 7, 22, 17, 46, 12]

1->0
2->0,1
3->0,1,2
4->0,1,2,3
5->0,1,2,3,4
6->0,1,2,3,4,5
7->0,1,2,3,4,5,6

"""


def insertion_sort(collection):
    for loop_index in range(1, len(collection)):
        print('collection: %s' % collection)
        print('loop_index: %s, collection[%s]: %s' % (loop_index, loop_index, collection[loop_index]))
        insertion_index = loop_index - 1

        while insertion_index >= 0:
            print('while')
            temp = collection[loop_index]
            print('temp: %s' % temp)

            if collection[insertion_index] > temp:
                print('break')
                print('insertion_index: %s, collection[%s]: %s' % (insertion_index, insertion_index, collection[insertion_index]))
                break
            insertion_index -= 1


if __name__ == '__main__':
    unsorted = [99, 5, 36, 7, 22, 17, 46, 12]
    insertion_sort(unsorted)
    print(unsorted)