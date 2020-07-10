#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 下午3:33
# @Author  : zhaoyu
# @Site    : 
# @File    : panel_dot.py
# @Software: PyCharm


r = 10
rect_len = r * 2
per = 1

total_dots = 300
cur_dots = 0
cur_rect_len = rect_len
# while cur_rect_len - per > 0:
#     n = cur_rect_len * 4 / per - 1
#     if n > 0:
#         cur_dots += n
#     else:
#         break
#     cur_rect_len -= per * 2
#     print('current cur_rect_len:{} cur_dots:{}', cur_rect_len, cur_dots)


split = 9
while split > 0:
    dots = split * 2 * 4 - 4
    cur_dots += dots
    print('current dots:{} current split:{}'.format(cur_dots, split))
    split -= 1

