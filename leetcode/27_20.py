#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
20. 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
(

示例 2:

输入: "()[]{}"
输出: true
(
[
{

示例 3:

输入: "(]"
输出: false
(

示例 4:

输入: "([)]"
输出: false
(
([


示例 5:

输入: "{[]}"
输出: true
{
{[

"""


class Stack(object):
    def __init__(self):
        self.stack = []

    def __bool__(self):
        return bool(self.stack)

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('pop from an empty stack')

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        return not bool(self.stack)

    def size(self):
        return len(self.stack)


class Solution(object):
    def is_valid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Stack()
        for i in s:
            if i in ['(', '{', '[']:
                stack.push(i)
            else:
                test = stack.peek()
                if '%s%s' % (test, i) in ['()', '{}', '[]']:
                    stack.pop()
                else:
                    return False
        if stack.is_empty():
            return True
        else:
            return False

print(Solution().is_valid('()'))
