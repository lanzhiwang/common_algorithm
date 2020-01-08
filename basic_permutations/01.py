#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
通过排列组合学习递归代码的写法

['红', '黄', '蓝', '绿']
"""

s1 = ['红', '黄', '蓝', '绿']
print('s1 = %s' % s1)

solution = []
print('solution = %s' % solution)

print('level 1')
for i1 in range(len(s1)):
	print('i1 = %s' % i1)
	print('s1[i1] = %s' % s1[i1])

	newSolution1 = solution + [s1[i1]]
	print('newSolution1 = %s' % newSolution1)

	s2 = s1[:i1] + s1[i1+1:]
	print('s2 = %s' % s2)

	print('level 2')
	for i2 in range(len(s2)):
		print('i2 = %s' % i2)
		print('s2[i2] = %s' % s2[i2])

		newSolution2 = newSolution1 + [s2[i2]]
		print('newSolution2 = %s' % newSolution2)

		s3 = s2[:i2] + s2[i2+1:]
		print('s3 = %s' % s3)
		print('level 3')
		for i3 in range(len(s3)):
			print('i3 = %s' % i3)
			print('s3[i3] = %s' % s3[i3])

			newSolution3 = newSolution2 + [s3[i3]]
			print('newSolution3 = %s' % newSolution3)

			s4 = s3[:i3] + s3[i3+1:]
			print('s4 = %s' % s4)

			print('level 4')
			for i4 in range(len(s4)):
				print('i4 = %s' % i4)
				print('s4[i4] = %s' % s4[i4])

				newSolution4 = newSolution3 + [s4[i4]]
				print('newSolution4 = %s' % newSolution4)

				s5 = s4[:i4] + s4[i4+1:]
				print('s5 = %s' % s5)

				if len(s5) == 0:
					print('排列: %s' % newSolution4)

"""
s1 = ['红', '黄', '蓝', '绿']
solution = []
level 1
i1 = 0
s1[i1] = 红
newSolution1 = ['红']
s2 = ['黄', '蓝', '绿']
level 2
i2 = 0
s2[i2] = 黄
newSolution2 = ['红', '黄']
s3 = ['蓝', '绿']
level 3
i3 = 0
s3[i3] = 蓝
newSolution3 = ['红', '黄', '蓝']
s4 = ['绿']
level 4
i4 = 0
s4[i4] = 绿
newSolution4 = ['红', '黄', '蓝', '绿']
s5 = []
排列: ['红', '黄', '蓝', '绿']
i3 = 1
s3[i3] = 绿
newSolution3 = ['红', '黄', '绿']
s4 = ['蓝']
level 4
i4 = 0
s4[i4] = 蓝
newSolution4 = ['红', '黄', '绿', '蓝']
s5 = []
排列: ['红', '黄', '绿', '蓝']
i2 = 1
s2[i2] = 蓝
newSolution2 = ['红', '蓝']
s3 = ['黄', '绿']
level 3
i3 = 0
s3[i3] = 黄
newSolution3 = ['红', '蓝', '黄']
s4 = ['绿']
level 4
i4 = 0
s4[i4] = 绿
newSolution4 = ['红', '蓝', '黄', '绿']
s5 = []
排列: ['红', '蓝', '黄', '绿']
i3 = 1
s3[i3] = 绿
newSolution3 = ['红', '蓝', '绿']
s4 = ['黄']
level 4
i4 = 0
s4[i4] = 黄
newSolution4 = ['红', '蓝', '绿', '黄']
s5 = []
排列: ['红', '蓝', '绿', '黄']
i2 = 2
s2[i2] = 绿
newSolution2 = ['红', '绿']
s3 = ['黄', '蓝']
level 3
i3 = 0
s3[i3] = 黄
newSolution3 = ['红', '绿', '黄']
s4 = ['蓝']
level 4
i4 = 0
s4[i4] = 蓝
newSolution4 = ['红', '绿', '黄', '蓝']
s5 = []
排列: ['红', '绿', '黄', '蓝']
i3 = 1
s3[i3] = 蓝
newSolution3 = ['红', '绿', '蓝']
s4 = ['黄']
level 4
i4 = 0
s4[i4] = 黄
newSolution4 = ['红', '绿', '蓝', '黄']
s5 = []
排列: ['红', '绿', '蓝', '黄']
i1 = 1
s1[i1] = 黄
newSolution1 = ['黄']
s2 = ['红', '蓝', '绿']
level 2
i2 = 0
s2[i2] = 红
newSolution2 = ['黄', '红']
s3 = ['蓝', '绿']
level 3
i3 = 0
s3[i3] = 蓝
newSolution3 = ['黄', '红', '蓝']
s4 = ['绿']
level 4
i4 = 0
s4[i4] = 绿
newSolution4 = ['黄', '红', '蓝', '绿']
s5 = []
排列: ['黄', '红', '蓝', '绿']
i3 = 1
s3[i3] = 绿
newSolution3 = ['黄', '红', '绿']
s4 = ['蓝']
level 4
i4 = 0
s4[i4] = 蓝
newSolution4 = ['黄', '红', '绿', '蓝']
s5 = []
排列: ['黄', '红', '绿', '蓝']
i2 = 1
s2[i2] = 蓝
newSolution2 = ['黄', '蓝']
s3 = ['红', '绿']
level 3
i3 = 0
s3[i3] = 红
newSolution3 = ['黄', '蓝', '红']
s4 = ['绿']
level 4
i4 = 0
s4[i4] = 绿
newSolution4 = ['黄', '蓝', '红', '绿']
s5 = []
排列: ['黄', '蓝', '红', '绿']
i3 = 1
s3[i3] = 绿
newSolution3 = ['黄', '蓝', '绿']
s4 = ['红']
level 4
i4 = 0
s4[i4] = 红
newSolution4 = ['黄', '蓝', '绿', '红']
s5 = []
排列: ['黄', '蓝', '绿', '红']
i2 = 2
s2[i2] = 绿
newSolution2 = ['黄', '绿']
s3 = ['红', '蓝']
level 3
i3 = 0
s3[i3] = 红
newSolution3 = ['黄', '绿', '红']
s4 = ['蓝']
level 4
i4 = 0
s4[i4] = 蓝
newSolution4 = ['黄', '绿', '红', '蓝']
s5 = []
排列: ['黄', '绿', '红', '蓝']
i3 = 1
s3[i3] = 蓝
newSolution3 = ['黄', '绿', '蓝']
s4 = ['红']
level 4
i4 = 0
s4[i4] = 红
newSolution4 = ['黄', '绿', '蓝', '红']
s5 = []
排列: ['黄', '绿', '蓝', '红']
i1 = 2
s1[i1] = 蓝
newSolution1 = ['蓝']
s2 = ['红', '黄', '绿']
level 2
i2 = 0
s2[i2] = 红
newSolution2 = ['蓝', '红']
s3 = ['黄', '绿']
level 3
i3 = 0
s3[i3] = 黄
newSolution3 = ['蓝', '红', '黄']
s4 = ['绿']
level 4
i4 = 0
s4[i4] = 绿
newSolution4 = ['蓝', '红', '黄', '绿']
s5 = []
排列: ['蓝', '红', '黄', '绿']
i3 = 1
s3[i3] = 绿
newSolution3 = ['蓝', '红', '绿']
s4 = ['黄']
level 4
i4 = 0
s4[i4] = 黄
newSolution4 = ['蓝', '红', '绿', '黄']
s5 = []
排列: ['蓝', '红', '绿', '黄']
i2 = 1
s2[i2] = 黄
newSolution2 = ['蓝', '黄']
s3 = ['红', '绿']
level 3
i3 = 0
s3[i3] = 红
newSolution3 = ['蓝', '黄', '红']
s4 = ['绿']
level 4
i4 = 0
s4[i4] = 绿
newSolution4 = ['蓝', '黄', '红', '绿']
s5 = []
排列: ['蓝', '黄', '红', '绿']
i3 = 1
s3[i3] = 绿
newSolution3 = ['蓝', '黄', '绿']
s4 = ['红']
level 4
i4 = 0
s4[i4] = 红
newSolution4 = ['蓝', '黄', '绿', '红']
s5 = []
排列: ['蓝', '黄', '绿', '红']
i2 = 2
s2[i2] = 绿
newSolution2 = ['蓝', '绿']
s3 = ['红', '黄']
level 3
i3 = 0
s3[i3] = 红
newSolution3 = ['蓝', '绿', '红']
s4 = ['黄']
level 4
i4 = 0
s4[i4] = 黄
newSolution4 = ['蓝', '绿', '红', '黄']
s5 = []
排列: ['蓝', '绿', '红', '黄']
i3 = 1
s3[i3] = 黄
newSolution3 = ['蓝', '绿', '黄']
s4 = ['红']
level 4
i4 = 0
s4[i4] = 红
newSolution4 = ['蓝', '绿', '黄', '红']
s5 = []
排列: ['蓝', '绿', '黄', '红']
i1 = 3
s1[i1] = 绿
newSolution1 = ['绿']
s2 = ['红', '黄', '蓝']
level 2
i2 = 0
s2[i2] = 红
newSolution2 = ['绿', '红']
s3 = ['黄', '蓝']
level 3
i3 = 0
s3[i3] = 黄
newSolution3 = ['绿', '红', '黄']
s4 = ['蓝']
level 4
i4 = 0
s4[i4] = 蓝
newSolution4 = ['绿', '红', '黄', '蓝']
s5 = []
排列: ['绿', '红', '黄', '蓝']
i3 = 1
s3[i3] = 蓝
newSolution3 = ['绿', '红', '蓝']
s4 = ['黄']
level 4
i4 = 0
s4[i4] = 黄
newSolution4 = ['绿', '红', '蓝', '黄']
s5 = []
排列: ['绿', '红', '蓝', '黄']
i2 = 1
s2[i2] = 黄
newSolution2 = ['绿', '黄']
s3 = ['红', '蓝']
level 3
i3 = 0
s3[i3] = 红
newSolution3 = ['绿', '黄', '红']
s4 = ['蓝']
level 4
i4 = 0
s4[i4] = 蓝
newSolution4 = ['绿', '黄', '红', '蓝']
s5 = []
排列: ['绿', '黄', '红', '蓝']
i3 = 1
s3[i3] = 蓝
newSolution3 = ['绿', '黄', '蓝']
s4 = ['红']
level 4
i4 = 0
s4[i4] = 红
newSolution4 = ['绿', '黄', '蓝', '红']
s5 = []
排列: ['绿', '黄', '蓝', '红']
i2 = 2
s2[i2] = 蓝
newSolution2 = ['绿', '蓝']
s3 = ['红', '黄']
level 3
i3 = 0
s3[i3] = 红
newSolution3 = ['绿', '蓝', '红']
s4 = ['黄']
level 4
i4 = 0
s4[i4] = 黄
newSolution4 = ['绿', '蓝', '红', '黄']
s5 = []
排列: ['绿', '蓝', '红', '黄']
i3 = 1
s3[i3] = 黄
newSolution3 = ['绿', '蓝', '黄']
s4 = ['红']
level 4
i4 = 0
s4[i4] = 红
newSolution4 = ['绿', '蓝', '黄', '红']
s5 = []
排列: ['绿', '蓝', '黄', '红']
"""