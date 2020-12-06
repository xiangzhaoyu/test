#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/1 下午7:22
# @Author  : zhaoyu
# @Site    : 工位计算
# @File    : gongwei.py
# @Software: PyCharm


import sys

s = input()
s_a = s.split(',')

# print('输入工位1-样本1数值')
# b1_1 = float(input())
b1_1 = float(s_a[0])
print('工位1-样本1 ' + str(b1_1))

# print('输入工位1-样本2数值')
# b1_2 = float(input())
b1_2 = float(s_a[1])
print('工位1-样本2 ' + str(b1_2))

# print('输入工位2-样本1数值')
# b2_1 = float(input())
b2_1 = float(s_a[2])
print('工位2-样本1 ' + str(b2_1))

# print('输入工位2-样本2数值')
# b2_2 = float(input())
b2_2 = float(s_a[3])
print('工位2-样本2 ' + str(b2_2))

# print('输入工位3-样本1数值')
# b3_1 = float(input())
b3_1 = float(s_a[4])
print('工位3-样本1 ' + str(b3_1))

# print('输入工位3-样本2数值')
# b3_2 = float(input())
b3_2 = float(s_a[5])
print('工位3-样本2 ' + str(b3_2))

# print('输入工位4-样本1数值')
# b4_1 = float(input())
b4_1 = float(s_a[6])
print('工位4-样本1 ' + str(b4_1))

# print('输入工位4-样本2数值')
# b4_2 = float(input())
b4_2 = float(s_a[7])
print('工位4-样本2 ' + str(b4_2))

# print('输入工位5-样本1数值')
# b5_1 = float(input())
b5_1 = float(s_a[8])
print('工位5-样本1 ' + str(b5_1))

# print('输入工位5-样本2数值')
# b5_2 = float(input())
b5_2 = float(s_a[9])
print('工位5-样本2 ' + str(b5_2))

g1_1 = abs(b1_1 - b1_2)
g2_1 = abs(b2_1 - b2_2)
g3_1 = abs(b3_1 - b3_2)
g4_1 = abs(b4_1 - b4_2)
g5_1 = abs(b5_1 - b5_2)

z1_2_1 = abs(b1_1 - b2_1)
z2_3_1 = abs(b2_1 - b3_1)
z3_4_1 = abs(b3_1 - b4_1)
z4_5_1 = abs(b4_1 - b5_1)

z1_2_2 = abs(b1_2 - b2_2)
z2_3_2 = abs(b2_2 - b3_2)
z3_4_2 = abs(b3_2 - b4_2)
z4_5_2 = abs(b4_2 - b5_2)


print('---------------------------------------------------------------')
print('---------{}---------{}---------{}---------{}---------'.format(str(z4_5_2), str(z3_4_2), str(z2_3_2), str(z1_2_2)))
print('----|----------|----------|----------|----------|----')
print('----{}---------{}---------{}---------{}---------{}---'.format(str(g5_1), str(g4_1), str(g3_1), str(g2_1), str(g1_1)))
print('----|----------|----------|----------|----------|----')
print('---------{}---------{}---------{}---------{}---------'.format(str(z4_5_1), str(z3_4_1), str(z2_3_1), str(z1_2_1)))
print('---------------------------------------------------------------')

print('{}  {}  {}  {}'.format(str((z4_5_2+z4_5_1)/2), str((z3_4_2+z3_4_1)/2), str((z2_3_2+z2_3_1)/2), str((z1_2_2+z1_2_1)/2)))
