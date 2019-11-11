#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 上午10:21
# @Author  : zhaoyu
# @Site    : 
# @File    : nlp_label_tool.py
# @Software: PyCharm

import os


def wirte_content(nlp_label, content):
    """
    标记文本内容
    :param nlp_label:
    :param content:
    :return:
    """
    with open('{}.txt'.format(nlp_label), 'a') as f:
        content = content.strip()
        f.write('{}\n'.format(content))


print('请输入待标注文件地址')
file_path = input()
print('待标注文件地址为 {}'.format(file_path))

if not os.path.exists(file_path):
    print('文件不存在 {}'.format(file_path))
    exit(1)

with open(file_path, 'r') as f:
    for line in f:
        try:
            line = line.strip()
            if line is None or len(line) < 1:
                continue
            print('选择文本类别：1 正常、2 负面、3 辱骂、4 灌水')
            nlp_label = input()
            wirte_content(nlp_label, line)
        except Exception as e:
            print('文本 {} 标记出现异常 {}'.format(line, str(repr(e))))
