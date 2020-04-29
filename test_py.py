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

# import emoji
#
# str = ",彭彭演这个剧不仅仅是剧组的团宠，还是弹幕的团宠:relieved_face::relieved_face::face_blowing_a_kiss::face_blowing_a_kiss::face_blowing_a_kiss:"
# e = emoji.emojize(str)
# print(e)

import json

with open('/Users/xiangzy/Desktop/ocr_match_tasks.json', 'r', encoding='utf-8') as f:
    load_dic = json.load(f)
    with open('/Users/xiangzy/Desktop/ocr_video.csv', 'a+', encoding='utf-8') as wf:
        try:
            wf.write('帧频\t合集ID\t任务ID\t视频名称\t视频ID\t视频地址\t数据\n')
            for vf in load_dic:
                wf.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(vf.get('framerate', ''), vf.get('extra', {}).get('cid', ''), vf.get('extra', {}).get('taskid', ''), vf.get('extra', {}).get('name', ''), vf.get('extra', {}).get('id', ''), vf.get('url', ''), vf.get('data', json.dumps(vf.get('data', {})))))
        except Exception as e:
            print(e)