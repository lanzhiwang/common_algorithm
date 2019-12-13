#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
排列组合

['红', '黄', '蓝', '绿']
"""

s1 = ['红', '黄', '蓝', '绿']
print('s1 = %s' % (s1))

solution = []
print('solution = %s' % (solution))

print('level 1')
for i1 in range(len(s1)):
	print('i1 = %s' % (i1))
	print('s1[i1] = %s' % (s1[i1]))

	newSolution1 = solution + [s1[i1]]
	print('newSolution1 = %s' % (newSolution1))

	s2 = s1[:i1] + s1[i1+1:]
	print('s2 = %s' % (s2))

	print('level 2')
	for i2 in range(len(s2)):
		print('i2 = %s' % (i2))
		print('s2[i2] = %s' % (s2[i2]))

		newSolution2 = newSolution1 + [s2[i2]]
		print('newSolution2 = %s' % (newSolution2))

		s3 = s2[:i2] + s2[i2+1:]
		print('s3 = %s' % (s3))
		print('level 3')
		for i3 in range(len(s3)):
			print('i3 = %s' % (i3))
			print('s3[i3] = %s' % (s3[i3]))

			newSolution3 = newSolution2 + [s3[i3]]
			print('newSolution3 = %s' % (newSolution3))

			s4 = s3[:i3] + s3[i3+1:]
			print('s4 = %s' % (s4))

			print('level 4')
			for i4 in range(len(s4)):
				print('i4 = %s' % (i4))
				print('s4[i4] = %s' % (s4[i4]))

				newSolution4 = newSolution3 + [s4[i4]]
				print('newSolution4 = %s' % (newSolution4))

				s5 = s4[:i4] + s4[i4+1:]
				print('s5 = %s' % (s5))

				if len(s5) == 0:
					print('排列: %s' % (newSolution4))