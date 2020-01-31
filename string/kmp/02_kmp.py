#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
计算前缀表

a b a b c
a a a a b

5

 0  1  2  3  4
 a  b  a  b  c
-5 -4 -3 -2 -1

4
s[0:4] ['a', 'b', 'a', 'b']
s[5-4:] ['b', 'a', 'b', 'c']

3
s[0:3] ['a', 'b', 'a']
s[5-3:] ['a', 'b', 'c']

2
s[0:2] ['a', 'b']
s[5-2:] ['b', 'c']

1
s[0:1] ['a']
s[5-1:] ['c']

"""


def get_prefix_table(collection):
    if len(collection) <= 1:
        return None
    result = [0] * len(collection)
    result[0] = -1
    result[1] = 0

    for i in range(2, len(collection)):
        c = collection[0:i]
        for j in range(len(c)-1, 0, -1):
            if c[0:j] == c[len(c) - j:]:
                result[i] = j
                break

    return result


if __name__ == '__main__':
    print(get_prefix_table(['a', 'b', 'a', 'b', 'c']))  # [-1, 0, 0, 1, 2]
    print(get_prefix_table(['a', 'a', 'a', 'a', 'b']))  # [-1, 0, 1, 2, 3]
