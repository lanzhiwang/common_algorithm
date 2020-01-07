# -*- coding: utf-8 -*-

"""
https://www.jianshu.com/p/d1b1544ddcab
"""

import string

from stack import Stack

__author__ = 'Omkar Pathak'


def is_operand(char):
    return char in string.ascii_letters or char in string.digits


def precedence(char):
    """ Return integer value representing an operator's precedence, or
    order of operation.

    https://en.wikipedia.org/wiki/Order_of_operations
    """
    dictionary = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    return dictionary.get(char, -1)


def infix_to_postfix(expression):
    """ Convert infix notation to postfix notation using the Shunting-yard
    algorithm.

    https://en.wikipedia.org/wiki/Shunting-yard_algorithm
    https://en.wikipedia.org/wiki/Infix_notation
    https://en.wikipedia.org/wiki/Reverse_Polish_notation
    """
    stack = Stack(len(expression))
    postfix = []
    for char in expression:
        print('postfix: %s' % postfix)
        print('stack: %s' % stack)
        print('char: %s' % char)
        if is_operand(char):  # 字母或数字
            postfix.append(char)

        elif char not in {'(', ')'}:  # 运算符 + - * / ^
            print('stack.peek(): %s' % stack.peek())
            while not stack.is_empty() and precedence(char) <= precedence(stack.peek()):
                postfix.append(stack.pop())
            stack.push(char)

        elif char == '(':  # （
            stack.push(char)

        elif char == ')':  # ）
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            if stack.peek() != '(':
                raise ValueError('Mismatched parentheses')
            stack.pop()
        print('postfix: %s' % postfix)
        print('stack: %s' % stack)
        print()

    while not stack.is_empty():
        postfix.append(stack.pop())
    return ' '.join(postfix)


if __name__ == '__main__':
    expression = 'a+b*(c^d-e)^(f+g*h)-i'
    print('Infix to Postfix Notation demonstration:\n')
    print('Infix notation: ' + expression)
    print('Postfix notation: ' + infix_to_postfix(expression))
    print()

    expression = '3+3*(6-1*2)/4-1'
    print('Infix to Postfix Notation demonstration:\n')
    print('Infix notation: ' + expression)
    print('Postfix notation: ' + infix_to_postfix(expression))

"""
Infix to Postfix Notation demonstration:

Infix notation: a+b*(c^d-e)^(f+g*h)-i
postfix: []
stack: []
char: a
postfix: ['a']
stack: []

postfix: ['a']
stack: []
char: +
stack.peek(): None
postfix: ['a']
stack: ['+']

postfix: ['a']
stack: ['+']
char: b
postfix: ['a', 'b']
stack: ['+']

postfix: ['a', 'b']
stack: ['+']
char: *
stack.peek(): +
postfix: ['a', 'b']
stack: ['+', '*']

postfix: ['a', 'b']
stack: ['+', '*']
char: (
postfix: ['a', 'b']
stack: ['+', '*', '(']

postfix: ['a', 'b']
stack: ['+', '*', '(']
char: c
postfix: ['a', 'b', 'c']
stack: ['+', '*', '(']

postfix: ['a', 'b', 'c']
stack: ['+', '*', '(']
char: ^
stack.peek(): (
postfix: ['a', 'b', 'c']
stack: ['+', '*', '(', '^']

postfix: ['a', 'b', 'c']
stack: ['+', '*', '(', '^']
char: d
postfix: ['a', 'b', 'c', 'd']
stack: ['+', '*', '(', '^']

postfix: ['a', 'b', 'c', 'd']
stack: ['+', '*', '(', '^']
char: -
stack.peek(): ^
postfix: ['a', 'b', 'c', 'd', '^']
stack: ['+', '*', '(', '-']

postfix: ['a', 'b', 'c', 'd', '^']
stack: ['+', '*', '(', '-']
char: e
postfix: ['a', 'b', 'c', 'd', '^', 'e']
stack: ['+', '*', '(', '-']

postfix: ['a', 'b', 'c', 'd', '^', 'e']
stack: ['+', '*', '(', '-']
char: )
postfix: ['a', 'b', 'c', 'd', '^', 'e', '-']
stack: ['+', '*']

postfix: ['a', 'b', 'c', 'd', '^', 'e', '-']
stack: ['+', '*']
char: ^
stack.peek(): *
postfix: ['a', 'b', 'c', 'd', '^', 'e', '-']
stack: ['+', '*', '^']

postfix: ['a', 'b', 'c', 'd', '^', 'e', '-']
stack: ['+', '*', '^']
char: (
postfix: ['a', 'b', 'c', 'd', '^', 'e', '-']
stack: ['+', '*', '^', '(']

postfix: ['a', 'b', 'c', 'd', '^', 'e', '-']
stack: ['+', '*', '^', '(']
char: f
postfix: ['a', 'b', 'c', 'd', '^', 'e', '-', 'f']
stack: ['+', '*', '^', '(']

postfix: ['a', 'b', 'c', 'd', '^', 'e', '-', 'f']
stack: ['+', '*', '^', '(']
char: +
stack.peek(): (
postfix: ['a', 'b', 'c', 'd', '^', 'e', '-', 'f']
stack: ['+', '*', '^', '(', '+']

postfix: ['a', 'b', 'c', 'd', '^', 'e', '-', 'f']
stack: ['+', '*', '^', '(', '+']
char: g
postfix: ['a', 'b', 'c', 'd', '^', 'e', '-', 'f', 'g']
stack: ['+', '*', '^', '(', '+']

postfix: ['a', 'b', 'c', 'd', '^', 'e', '-', 'f', 'g']
stack: ['+', '*', '^', '(', '+']
char: *
stack.peek(): +
postfix: ['a', 'b', 'c', 'd', '^', 'e', '-', 'f', 'g']
stack: ['+', '*', '^', '(', '+', '*']

postfix: ['a', 'b', 'c', 'd', '^', 'e', '-', 'f', 'g']
stack: ['+', '*', '^', '(', '+', '*']
char: h
postfix: ['a', 'b', 'c', 'd', '^', 'e', '-', 'f', 'g', 'h']
stack: ['+', '*', '^', '(', '+', '*']

postfix: ['a', 'b', 'c', 'd', '^', 'e', '-', 'f', 'g', 'h']
stack: ['+', '*', '^', '(', '+', '*']
char: )
postfix: ['a', 'b', 'c', 'd', '^', 'e', '-', 'f', 'g', 'h', '*', '+']
stack: ['+', '*', '^']

postfix: ['a', 'b', 'c', 'd', '^', 'e', '-', 'f', 'g', 'h', '*', '+']
stack: ['+', '*', '^']
char: -
stack.peek(): ^
postfix: ['a', 'b', 'c', 'd', '^', 'e', '-', 'f', 'g', 'h', '*', '+', '^', '*', '+']
stack: ['-']

postfix: ['a', 'b', 'c', 'd', '^', 'e', '-', 'f', 'g', 'h', '*', '+', '^', '*', '+']
stack: ['-']
char: i
postfix: ['a', 'b', 'c', 'd', '^', 'e', '-', 'f', 'g', 'h', '*', '+', '^', '*', '+', 'i']
stack: ['-']

Postfix notation: a b c d ^ e - f g h * + ^ * + i -

Infix to Postfix Notation demonstration:

Infix notation: 3+3*(6-1*2)/4-1
postfix: []
stack: []
char: 3
postfix: ['3']
stack: []

postfix: ['3']
stack: []
char: +
stack.peek(): None
postfix: ['3']
stack: ['+']

postfix: ['3']
stack: ['+']
char: 3
postfix: ['3', '3']
stack: ['+']

postfix: ['3', '3']
stack: ['+']
char: *
stack.peek(): +
postfix: ['3', '3']
stack: ['+', '*']

postfix: ['3', '3']
stack: ['+', '*']
char: (
postfix: ['3', '3']
stack: ['+', '*', '(']

postfix: ['3', '3']
stack: ['+', '*', '(']
char: 6
postfix: ['3', '3', '6']
stack: ['+', '*', '(']

postfix: ['3', '3', '6']
stack: ['+', '*', '(']
char: -
stack.peek(): (
postfix: ['3', '3', '6']
stack: ['+', '*', '(', '-']

postfix: ['3', '3', '6']
stack: ['+', '*', '(', '-']
char: 1
postfix: ['3', '3', '6', '1']
stack: ['+', '*', '(', '-']

postfix: ['3', '3', '6', '1']
stack: ['+', '*', '(', '-']
char: *
stack.peek(): -
postfix: ['3', '3', '6', '1']
stack: ['+', '*', '(', '-', '*']

postfix: ['3', '3', '6', '1']
stack: ['+', '*', '(', '-', '*']
char: 2
postfix: ['3', '3', '6', '1', '2']
stack: ['+', '*', '(', '-', '*']

postfix: ['3', '3', '6', '1', '2']
stack: ['+', '*', '(', '-', '*']
char: )
postfix: ['3', '3', '6', '1', '2', '*', '-']
stack: ['+', '*']

postfix: ['3', '3', '6', '1', '2', '*', '-']
stack: ['+', '*']
char: /
stack.peek(): *
postfix: ['3', '3', '6', '1', '2', '*', '-', '*']
stack: ['+', '/']

postfix: ['3', '3', '6', '1', '2', '*', '-', '*']
stack: ['+', '/']
char: 4
postfix: ['3', '3', '6', '1', '2', '*', '-', '*', '4']
stack: ['+', '/']

postfix: ['3', '3', '6', '1', '2', '*', '-', '*', '4']
stack: ['+', '/']
char: -
stack.peek(): /
postfix: ['3', '3', '6', '1', '2', '*', '-', '*', '4', '/', '+']
stack: ['-']

postfix: ['3', '3', '6', '1', '2', '*', '-', '*', '4', '/', '+']
stack: ['-']
char: 1
postfix: ['3', '3', '6', '1', '2', '*', '-', '*', '4', '/', '+', '1']
stack: ['-']

Postfix notation: 3 3 6 1 2 * - * 4 / + 1 -

"""