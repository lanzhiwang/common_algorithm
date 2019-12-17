"""
归并排序 原理说明
原始序列 10 5 7 3 2 8
N = 6

初始分组：[10] [5] [7] [3] [2] [8]
使用队列第 1 次归并后的分组：[5 10] [3 7] [2 8]
使用队列第 2 次归并后的分组：[3 5 7 10] [2 8]
使用队列第 3 次归并后的分组：[2 3 5 7 8 10]

[3 5 7 10]
[2 8]
=> []

[3 5 7 10]
[8]
=> [2]

[5 7 10]
[8]
=> [2 3]

[7 10]
[8]
=> [2 3 5]

[10]
[8]
=> [2 3 5 7]

[10]
[]
=> [2 3 5 7 8]

[]
[]
=> [2 3 5 7 8 10]

"""