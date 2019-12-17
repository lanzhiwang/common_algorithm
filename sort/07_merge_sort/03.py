"""
合并两个有序序列

方法一：增加新序列
[5, 7, 10]
[2, 3, 6, 8]
[]

[5, 7, 10]
[3, 6, 8]
[2]

[5, 7, 10]
[6, 8]
[2, 3]

[7, 10]
[6, 8]
[2, 3, 5]

[7, 10]
[8]
[2, 3, 5, 6]

[10]
[8]
[2, 3, 5, 6, 7]

[10]
[]
[2, 3, 5, 6, 7, 8]

[2, 3, 5, 6, 7, 8] + [10] + []

方法二：原地修改

"""


# 增加新序列
def merge1(left, right):
    result = []
    while left and right:
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
    return result + left + right


# 原地修改
def merge2(left, right):
    for right_index in range(len(right)):
        for left_index in range(len(left)):
            if left[left_index] > right[right_index]:
                left.insert(left_index, right[right_index])
                break
        else:
            left.append(right[right_index])
    return left


# 原地修改
def merge3(left, right):
    last_index = 0
    for right_index in range(len(right)):
        for left_index in range(last_index, len(left)+1):
            if left_index == len(left):
                left.append(right[right_index])
                last_index = left_index
                break

            if left[left_index] >= right[right_index]:
                left.insert(left_index, right[right_index])
                last_index = left_index + 1
                break
            elif left[left_index] < right[right_index]:
                continue
    return left


if __name__ == '__main__':
    for p in (([5], [7]), ([10], [5, 7]), ([2, 3], [6, 8]), ([2, 3], [2, 8]), ([5, 7, 10], [2, 3, 6, 8])):
        print(merge1(*p))
    print()

    for left, right in (([5], [7]), ([10], [5, 7]), ([2, 3], [6, 8]), ([2, 3], [2, 8]), ([5, 7, 10], [2, 3, 6, 8])):
        merge2(left, right)
        print(left)
    print()

    for left, right in (([5], [7]), ([10], [5, 7]), ([2, 3], [6, 8]), ([2, 3], [2, 8]), ([5, 7, 10], [2, 3, 6, 8])):
        merge3(left, right)
        print(left)
    print()
