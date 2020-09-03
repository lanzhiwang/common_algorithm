#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A-12C3 -> -12
A-12 -> -12
A-C -> ''
A12C -> 12
A+-1C -> -1
0 -> 0
AC2 -> 2

"""

def fin_str(str, first):
    print(str)
    result = ''
    if first:
        for index, s in enumerate(str):
            if s in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                print(index, s)
                try:
                    temp = fin_str(str[index+1:], first=False)
                except:
                    temp = None
                if temp is None:
                    result = '%s' % s
                else:
                    result = '%s%s' % (s, temp)
                try:
                    if str[index-1] == '-':
                        result = 0 - int(result)
                    return result
                except:
                    return int(result)
        return result
    else:
        if str[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            try:
                temp = fin_str(str[1:], first=False)
            except:
                temp = None
            if temp is None:
                return '%s' % str[0]
            else:
                return '%s%s' % (str[0], temp)
        else:
            return None


# for str in ['A-12C3', 'A-12', 'A-C', 'A12C', 'A+-1C', '', '0', 'AC2']:
#     print(fin_str(str, first=True))
#     print('=====')


def fin_str1(str):
    print(str)
    if str == '0':
        return 0
    start = None
    end = None
    for index, s in enumerate(str):
        if start is None:
            if s in '123456789':
                start = index
                continue
        if start is not None and end is None:
            if s not in '1234567890':
                end = index
                break
    print(start, end)
    if start is not None:
        if end is not None:
            result = str[start:end]
        else:
            result = str[start:]
        if start-1 >= 0 and str[start-1] == '-':
            return 0 - int(result)
        else:
            return int(result)
    else:
        return None

for str in ['A-12C3', 'A-12', 'A-C', 'A12C', 'A+-1C', '', '0', 'AC2', '123', '123-']:
    print(fin_str1(str))
    print('=====')
