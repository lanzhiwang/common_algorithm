#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
排列组合

['红', '黄', '蓝', '绿']
"""

s1 = ['红', '黄', '蓝', '绿']

solution1 = []

"""
for i1 in range(len(s1)):
    newSolution1 = solution + [s1[i1]]
    s2 = s1[:i1] + s1[i1+1:]

    for i2 in range(len(s2)):
        newSolution2 = newSolution1 + [s2[i2]]
        s3 = s2[:i2] + s2[i2+1:]

        for i3 in range(len(s3)):
            newSolution3 = newSolution2 + [s3[i3]]
            s4 = s3[:i3] + s3[i3+1:]

            for i4 in range(len(s4)):
                newSolution4 = newSolution3 + [s4[i4]]
                s5 = s4[:i4] + s4[i4+1:]

                if len(s5) == 0:
                    print('排列: %s' % (newSolution4))
"""

def foo(array, solution):
    if len(array) == 0:
        print('排列: %s' % solution)

    for i in range(len(array)):
        newSolution = solution + [array[i]]
        newArray = array[:i] + array[i+1:]

        foo(newArray, newSolution)

foo(s1, solution1)

"""
排列: ['红', '黄', '蓝', '绿']
排列: ['红', '黄', '绿', '蓝']
排列: ['红', '蓝', '黄', '绿']
排列: ['红', '蓝', '绿', '黄']
排列: ['红', '绿', '黄', '蓝']
排列: ['红', '绿', '蓝', '黄']
排列: ['黄', '红', '蓝', '绿']
排列: ['黄', '红', '绿', '蓝']
排列: ['黄', '蓝', '红', '绿']
排列: ['黄', '蓝', '绿', '红']
排列: ['黄', '绿', '红', '蓝']
排列: ['黄', '绿', '蓝', '红']
排列: ['蓝', '红', '黄', '绿']
排列: ['蓝', '红', '绿', '黄']
排列: ['蓝', '黄', '红', '绿']
排列: ['蓝', '黄', '绿', '红']
排列: ['蓝', '绿', '红', '黄']
排列: ['蓝', '绿', '黄', '红']
排列: ['绿', '红', '黄', '蓝']
排列: ['绿', '红', '蓝', '黄']
排列: ['绿', '黄', '红', '蓝']
排列: ['绿', '黄', '蓝', '红']
排列: ['绿', '蓝', '红', '黄']
排列: ['绿', '蓝', '黄', '红']

"""