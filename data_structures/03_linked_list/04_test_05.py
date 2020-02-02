# -*- coding: utf-8 -*-

"""
https://www.youtube.com/watch?v=hvSqg02HBz4

交叉链表

1 -> 2 -> 3
            -> 4 -> 5 -> 6
     a -> b

len(list1) = 6
len(list2) = 5

list1 先移动 len(list1) - len(list2) 到 2 节点
然后 list1 和 list2 一起移动，第一次汇合的地方就是交叉点

"""
