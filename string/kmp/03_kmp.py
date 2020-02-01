#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""

初始化:
i
0 1 2 3 4 5 6 7 8 9 10 11
a b a a c a b a b c a  c
j
0 1 2 3 4
a b a b c
- 0 0 1 2

i = 0
j = 0

#############################################################
      i
0 1 2 3 4 5 6 7 8 9 10 11
a b a a c a b a b c a  c
      j
0 1 2 3 4
a b a b c
- 0 0 1 2

i = 3
j = 3

      i
0 1 2 3 4 5 6 7 8 9 10 11
a b a a c a b a b c a  c
      j
    0 1 2 3 4
    a b a b c
    - 0 0 1 2

i = 3
j = 1
#############################################################
      i
0 1 2 3 4 5 6 7 8 9 10 11
a b a a c a b a b c a  c
      j
    0 1 2 3 4
    a b a b c
    - 0 0 1 2

i = 3
j = 1

      i
0 1 2 3 4 5 6 7 8 9 10 11
a b a a c a b a b c a  c
      j
      0 1 2 3 4
      a b a b c
      - 0 0 1 2

i = 3
j = 0

#############################################################
        i
0 1 2 3 4 5 6 7 8 9 10 11
a b a a c a b a b c a  c
        j
      0 1 2 3 4
      a b a b c
      - 0 0 1 2

i = 4
j = 1

        i
0 1 2 3 4 5 6 7 8 9 10 11
a b a a c a b a b c a  c
        j
        0 1 2 3 4
        a b a b c
        - 0 0 1 2

i = 4
j = 0
#############################################################
        i
0 1 2 3 4 5 6 7 8 9 10 11
a b a a c a b a b c a  c
        j
        0 1 2 3 4
        a b a b c
        - 0 0 1 2

i = 4
j = 0

          i
0 1 2 3 4 5 6 7 8 9 10 11
a b a a c a b a b c a  c
          j
          0 1 2 3 4
          a b a b c
          - 0 0 1 2

i = 5
j = 0

#############################################################
                    i
0 1 2 3 4 5 6 7 8 9 10 11
a b a a c a b a b c a  c
                    j
          0 1 2 3 4
          a b a b c
          - 0 0 1 2

i = 10
j = 5
#############################################################

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


def kmp(target, pattern):
    if len(target) < len(pattern):
        return False
    prefix_table = get_prefix_table(pattern)
    i = 0
    j = 0
    while (i >= 0 and i < len(target)) and (j >= 0 and j < len(pattern)):
        if target[i] == pattern[j]:
            i += 1
            j += 1
            if j >= len(pattern):
                return True
        else:
            j = prefix_table[j]
            if j == -1:
                j = 0
                i += 1
    return False


if __name__ == '__main__':
    print(kmp('abaacababcac', 'ababc'))
    print(kmp('aaaaaaaaaab', 'aaaab'))
    print(kmp('aaaaaaaaaab', 'aaaac'))
