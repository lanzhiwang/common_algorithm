#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
155. 最小栈
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。

示例:

输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

提示：

pop、top 和 getMin 操作总是在 非空栈 上调用。


[6, 2, 7, 9, 3, 4, 1, 5, 10, 8]
self.stack = [6, 2, 7, 9, 3, 4, 1, 5, 10, 8]
self.min_value = [6, 2, 1]


"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_value = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not bool(self.min_value):
            self.min_value.append(x)
        else:
            now_min = self.min_value[-1]
            if now_min >= x:
                self.min_value.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            value = self.stack.pop()
            if self.min_value[-1] == value:
                self.min_value.pop()
            return value
        else:
            raise IndexError('pop from an empty stack')


    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        if self.min_value:
            return self.min_value[-1]

