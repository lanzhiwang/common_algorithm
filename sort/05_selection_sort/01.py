"""
简单选择排序
原始序列 99 5 36 7 22 17 46 12
N = 8

99 5 36 7 22 17 46 12
^
后续最小：5，交换 99 和 5


5 99 36 7 22 17 46 12
  ^
后续最小：7，交换 99 和 7


5 7 36 99 22 17 46 12
    ^
后续最小：12，交换 36 和 12


5 7 12 99 22 17 46 36
       ^
后续最小：17，交换 99 和 17


5 7 12 17 22 99 46 36
          ^
后续最小：22，不需要交换


5 7 12 17 22 99 46 36
             ^
后续最小：36，交换 99 和 36


5 7 12 17 22 36 46 99
                ^
后续最小：46，不需要交换


5 7 12 17 22 36 46 99

"""


def selection_sort(collection):
    for i in range(0, len(collection)-1):
        min_element = min(collection[i:])
        min_element_index = collection.index(min_element)
        if min_element < collection[i]:
            collection[i], collection[min_element_index] = collection[min_element_index], collection[i]


if __name__ == '__main__':
    user_input = '99 5 36 7 22 17 46 12'
    unsorted = [int(item) for item in user_input.split(' ')]
    selection_sort(unsorted)
    print(unsorted)
