#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 上午10:24
# @Author  : zhaoyu
# @Site    : 
# @File    : test_pic.py
# @Software: PyCharm

import os
import shutil

def get_imgpath(dir):
    """获取目录下所有图片的绝对地址"""
    paths = []
    try:
        if os.path.exists(dir):
            for file in os.listdir(dir):
                path = os.path.join(dir, file)
                if os.path.isfile(path) and os.path.splitext(file)[-1] == '.jpeg' or os.path.splitext(file)[
                        -1] == '.jpg' or os.path.splitext(file)[-1] == '.png':
                    paths.append(path)
                elif os.path.isdir(path):
                    paths.extend(get_imgpath(path))
    except Exception as e:
        print(repr(e))
    return paths

def p1(framedir, headdir):
    """
    :param framedir:
    :param headdir:
    :return:
    """
    yesdir = '/Users/xiangzy/Desktop/yes'
    nodir = '/Users/xiangzy/Desktop/no'
    framedir = get_imgpath(framedir)
    headdir = get_imgpath(headdir)
    i = 0
    for frame in framedir:
        name = os.path.split(frame)[-1]
        name = os.path.splitext(name)[0]
        nohead = True
        for head in headdir:
            if name in head:
                print('{}{}在{}中'.format(str(i), head, frame))
                shutil.copy(frame, os.path.join(yesdir, os.path.split(frame)[-1]))
                nohead = False
                break
        if nohead:
            print('{}{}没有获取到头像'.format(str(i), frame))
            shutil.copy(frame, os.path.join(nodir, os.path.split(frame)[-1]))
        i = i + 1


p1('/Users/xiangzy/Desktop/吴昕', '/Users/xiangzy/Desktop/wuxin1')