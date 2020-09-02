#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，
但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。

"""

import re



import re

pattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(pattern, text)





class Solution(object):
    def isNumber(self, text):
        """
        :type s: str
        :rtype: bool
        """
        text = text.strip()
        is_num = False
        is_dot = False
        is_e = False
        for i, s in enumerate(text):
            print(i, s)
            if s >= '0' and s <= '9':
                print(1)
                is_num = True
                print(is_num, is_dot, is_e)
            elif s == '.':
                print(2)
                if is_dot or is_e:
                    return False
                is_dot = True
                print(is_num, is_dot, is_e)
            elif s in ['e', 'E']:
                print(3)
                if not is_num or is_e:
                    return False
                is_e = True
                is_num = False
                print(is_num, is_dot, is_e)
            elif s in ['+', '-']:
                print(4)
                # if (i != 0) or (i > 0 and text[i-1] not in ['e', 'E']):
                #     return False
                if i != 0:
                    if text[i-1] not in ['e', 'E']:
                        return False
                # else:
                #     pass
                print(is_num, is_dot, is_e)
            else:
                print(5)
                return False
        return is_num





for s in ["+100", "5e2", "-123", "3.1416", "-1E-16", "0123", "12e", "1a3.14", "1.2.3", "+-5", "12e+5.4", "1 "]:
    print(s)
    print(Solution().isNumber(s))
    print('===============================')
