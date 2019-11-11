#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/7 上午11:21
# @Author  : zhaoyu
# @Site    : 
# @File    : test_py.py
# @Software: PyCharm

import pypinyin
import time

# with open('insert.txt', 'r') as f:
#     for line in f:
#         if line is None:
#             continue
#         start = time.time()
#         py = pypinyin.lazy_pinyin(line)
#         print('cost pinyin：{:.5f}s'.format((time.time() - start)))
#         print('{}\t{}'.format(line, py))

import emoji

str = ",彭彭演这个剧不仅仅是剧组的团宠，还是弹幕的团宠:relieved_face::relieved_face::face_blowing_a_kiss::face_blowing_a_kiss::face_blowing_a_kiss:"
e = emoji.emojize(str)
print(e)