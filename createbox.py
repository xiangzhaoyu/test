#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 下午5:59
# @Author  : zhaoyu
# @Site    : 复制xml，用于台标，因为box位置不变
# @File    : createbox.py
# @Software: PyCharm

import os, shutil

def create():
    fname = '4230682'
    xml = '4230682_0.mp4_25.0_15.96_399.xml'
    xmldir = '/Users/xiangzy/Desktop/hnws1/xml'
    for root, dirs, files in os.walk('/Users/xiangzy/Desktop/hnws1/img'):
        for file in files:
            if fname in file:
                print('copy {} to {}'.format('/Users/xiangzy/Desktop/4230682_0.mp4_25.0_15.96_399.xml',
                                             os.path.join(xmldir, os.path.splitext(file)[0] + '.xml')))
                shutil.copy('/Users/xiangzy/Desktop/4230682_0.mp4_25.0_15.96_399.xml', os.path.join(xmldir, os.path.splitext(file)[0]+'.xml'))

def create1():
    fname = '4230711'
    xml = '4230711_1.mp4_25.0_152.96_3824.xml'
    xmldir = '/Users/xiangzy/Desktop/hnws1/xml'
    for root, dirs, files in os.walk('/Users/xiangzy/Desktop/hnws1/img'):
        for file in files:
            if fname in file:
                print('copy {} to {}'.format('/Users/xiangzy/Desktop/'+xml,
                                             os.path.join(xmldir, os.path.splitext(file)[0] + '.xml')))
                shutil.copy('/Users/xiangzy/Desktop/'+xml, os.path.join(xmldir, os.path.splitext(file)[0]+'.xml'))

create1()