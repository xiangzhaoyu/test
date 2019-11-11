#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/18 下午8:57
# @Author  : zhaoyu
# @Site    : 
# @File    : test1.py
# @Software: PyCharm

import sys, os
from PIL import Image
from functools import reduce
import numpy as np


def compose(*func):
    return reduce(lambda f, g: lambda *a, **b: g(f(*a, **b)), func)


def comp1(a, b):
    c = a + b
    print(c)
    return c


def comp2(a):
    c = a * a
    print(c)
    return c


def comp3(a):
    c = a / (a + a)
    print(c)
    return c


def comp4(a):
    c = a * (a + a)
    print(c)
    return c


def comp5(a, b):
    c = a * a * b * b
    print(c)
    return c


def testcomp():
    temp = compose(comp1, comp2, comp3, comp4, comp5(1))(3, 4)
    a = temp
    print(a)


def test():
    """
    a = os.system('./test1.sh')
    a = a >> 8
    print(a)
    """
    h = 200
    w = 400
    num_anchors = 9
    num_classes = 20
    a = [(h // {0: 32, 1: 16}[l], w // {0: 32, 1: 16}[l], num_anchors // 2, num_classes + 5) for l in range(2)]
    test1(*a)
    test2(a)
    c = lambda a, b: b
    print(c)


def test1(*a):
    b = a
    print(b)


def test2(a):
    b = a
    print(b)


def DarknetConv2D_BN_Leaky(*args, **kwargs):
    print(args)
    print(kwargs)


def tiny_yolo_body(inputs, num_anchors, num_classes):
    a = DarknetConv2D_BN_Leaky(16, (3, 3))
    print(a)


def test_lstm1():
    length = 5
    seq = np.array([i / float(length) for i in range(length)])
    print(seq)


def fei(years, ratio, per_num):
    sum_num = 0
    for i in range(years):
        if i > 13:
            sum_num = sum_num * (1 + ratio)
        else:
            sum_num = (sum_num + per_num) * (1 + ratio)
    print(sum_num)


def comp():
    w1 = np.load('emb_weights.npy')
    w2 = np.load('emb_weights.npy.1')
    dif = w1 - w2
    print(dif)


def sales(count):
    ini = 6
    rate = 0.1
    all_sale = ini
    for i in range(count - 1):
        ini = ini * (1 + rate)
        # print('{} {}'.format(i, ini))
        all_sale += ini
        print('{} {}'.format(i + 1, all_sale))


def temp():
    img = Image.open('/Users/xiangzy/PycharmProjects/tianqi/train_data/tianqi_data/img/0a21a05089687ed72de4af78f66fbac0/001.jpg')
    crop_img = img.crop((2000, 2000, 2416, 2416))
    crop_img.save('crop.jpg')
    # paste_img = Image.new('RGB', (1000, 1000), (128, 128, 128))
    # paste_img.paste(img, (500, 500))
    # paste_img.save('paste.jpg')


# test()
# tiny_yolo_body(1, 3, 20)
# testcomp()
# test_lstm1()
# fei(3, 0.02, 1000)
# comp()
# sales(40)
temp()