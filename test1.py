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
import operator
import math
import xlrd
from xlwt import *
from common_requests import get_request


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
    feed = ['feed_id','notice_type','state','fantuan_id','typ','my_sort_time','notice_type','fantuan_id','state','typ','weight','fantuan_id','state','notice_type','my_sort_time','fantuan_id','uuid','state','typ','weight','hot_count','comment_count','praise_count','id','fantuan_id','uuid','state','typ','weight','id','hot_count','comment_count','praise_count','feed_id','uuid','notice_type','state','typ','source','id','data_key','data_key','typ','typ','data_key','state','fantuan_id','notice_type','typ','create_date','uuid','fantuan_id','id','state','fantuan_id','id','state','create_time','uuid','fantuan_id','fantuan_id','state','state','fantuan_id','id','state','fantuan_id','uuid','notice_type','id','state','fantuan_id','uuid','typ','notice_type','id','state','fantuan_id','uuid','typ','notice_type','feed_id','id','fantuan_id','state','notice_type','typ','id','source','link_key','typ','source','data_key']
    feed_bell = ['state','expire_time','feed_id','bell_type','fnatuan_id','topic_id','hot_search_id','update_time','feed_id','bell_type','state','expire_time','feed_id','state','expire_time','bell_type','bell_type','feed_id','fnatuan_id','topic_id','hot_search_id','update_time','id']
    feed_expand = ['feed_id','id','feed_id','feed_id','id']
    feed_rec = ['feed_id','state','update_time','id','feed_id','id','feed_id','state','feed_id','state','fantuan_id','uuid','create_time']

    dic_f = {}
    for f in feed:
        if f in dic_f.keys():
            dic_f[f] = dic_f[f] + 1
        else:
            dic_f[f] = 1
    sorted_list_a = sorted(dic_f.items(), key=operator.itemgetter(1))
    print('feed')
    print(sorted_list_a)

    dic_f = {}
    for f in feed_bell:
        if f in dic_f.keys():
            dic_f[f] = dic_f[f] + 1
        else:
            dic_f[f] = 1
    sorted_list_a = sorted(dic_f.items(), key=operator.itemgetter(1))
    print('feed_bell')
    print(sorted_list_a)

    dic_f = {}
    for f in feed_expand:
        if f in dic_f.keys():
            dic_f[f] = dic_f[f] + 1
        else:
            dic_f[f] = 1
    sorted_list_a = sorted(dic_f.items(), key=operator.itemgetter(1))
    print('feed_expand')
    print(sorted_list_a)

    dic_f = {}
    for f in feed_rec:
        if f in dic_f.keys():
            dic_f[f] = dic_f[f] + 1
        else:
            dic_f[f] = 1
    sorted_list_a = sorted(dic_f.items(), key=operator.itemgetter(1))
    print('feed_rec')
    print(sorted_list_a)

    s = 'abc'
    per = int(len(s)/2)
    print(per)
    s1 = 'abcd'
    per1 = int(len(s1)/2)
    print(per1)


    x = s[math.ceil(len(s)/2):]+s1[math.ceil(len(s1)/2):]+s[:math.ceil(len(s)/2)]+s1[:math.ceil(len(s1)/2)]
    print(x)


def fill_user_mobile():
    # ------------------读数据---------------------------------
    fileName = "/Users/xiangzy/Desktop/py.xls"
    bk = xlrd.open_workbook(fileName)
    shxrange = range(bk.nsheets)
    try:
        sh = bk.sheet_by_name("Sheet1")
    except Exception as e:
        print('read exception {}'.format(e))
    nrows = sh.nrows  # 获取行数
    book = Workbook(encoding='utf-8')
    sheet = book.add_sheet('Sheet1')  # 创建一个sheet
    for i in range(1, nrows):
        row_data = sh.row_values(i)
        # 获取第i行第3列数据
        # sh.cell_value(i,3)
        # ---------写出文件到excel--------
        print("-----正在写入 " + str(i) + " 行")
        try:
            uuid = sh.cell_value(i, 4)
            data = get_request('http://idp.hifuntv.com/in/GetUserInfoByUuid?invoker=itvsdk&sign=d3cafca88773700f411999fec9e159a9f38daf4f&data=%7B%22uuid%22%3A%22{}%22%2C%22return%22%3A%22relate_mobile%22%2C%22_support%22%3A%2210000000%22%2C%22uip%22%3A%22127.0.0.1%22%2C%22seqid%22%3A%2220b9bc2644476e5f2dff094bc7d8b3c5%22%2C%22is_sign%22%3A1%7D'.format(uuid))
            print('uuid:{} result:{}'.format(uuid, data))
            if data is not None:
                mobile = data.get('msg', {}).get('relate_mobile', '')
                if len(mobile) < 1:
                    continue
                sheet.write(i, 38, label=mobile)  # 向第1行第1列写入获取到的值
        except Exception as e:
            print('{} have exception {}'.format(i, e))
    book.save("/Users/xiangzy/Desktop/py-mobile.xls")


# test()
# tiny_yolo_body(1, 3, 20)
# testcomp()
# test_lstm1()
# fei(3, 0.02, 1000)
# comp()
# sales(40)
# temp()

import hashlib

md5_hash = hashlib.md5()
md5_hash.update("9vhACx[|0Lx<".encode())
a = md5_hash.hexdigest()
print(a)