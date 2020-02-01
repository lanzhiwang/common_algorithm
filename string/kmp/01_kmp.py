#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""

KMP 是字符串匹配算法

在 T 中找到 P 字符串，假设 P 字符串较短
T: a b a a c a b a b c a c
P: a b a b c

方法一：暴力搜索
a b a a c a b a b c a c
a b a b c
  a b a b c
    a b a b c
      a b a b c
        a b a b c
          a b a b c

方法二: KMP

prefix table

a -> 0
a b -> 0
a b a -> 1
a b a b -> 2
a b a b c -> 0

0  1 2 3 4
a  b a b c
-1 0 0 1 2

      V
a b a a c a b a b c a c
0 1 2 3 4
a b a b c
- 0 0 1 2

      V
a b a a c a b a b c a c
    0 1 2 3 4
    a b a b c
    - 0 0 1 2

        V
a b a a c a b a b c a c
      0 1 2 3 4
      a b a b c
      - 0 0 1 2

        V
a b a a c a b a b c a c
        0 1 2 3 4
        a b a b c
        - 0 0 1 2

          V
a b a a c a b a b c a c
          0 1 2 3 4
          a b a b c
          - 0 0 1 2




T: a a a a a a a a a a b
P: a a a a b

prefix table

a -> 0
a a -> 1
a a a -> 2
a a a a -> 3
a a a a b

0  1 2 3 4
a  a a a b
-1 0 1 2 3

        V
a a a a a a a a a a b
0 1 2 3 4
a a a a b
1 0 1 2 3

          V
a a a a a a a a a a b
  0 1 2 3 4
  a a a a b
  1 0 1 2 3

            V
a a a a a a a a a a b
    0 1 2 3 4
    a a a a b
    1 0 1 2 3

              V
a a a a a a a a a a b
      0 1 2 3 4
      a a a a b
      1 0 1 2 3
...
                    V
a a a a a a a a a a b
            0 1 2 3 4
            a a a a b
            1 0 1 2 3

"""