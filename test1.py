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

# import hashlib
#
# md5_hash = hashlib.md5()
# md5_hash.update("9vhACx[|0Lx<".encode())
# a = md5_hash.hexdigest()
# print(a)

# import json
#
# st = '{"data":[{"id":"24185487","company_id":"1","request_id":"2b62050791b7447da37bc32f469a1d57","did":"7da87e439a845f7456b15879feac79f5","knowledge_id":"36","message_type":"0","click_message":"36","message_code":"1","action":"1","feed_back_id":null,"click_state":"0","message":"取消连续包月","result":"{"answer":"【支付宝退订】：打开支付宝“我的”→“设置”→“支付设置”→“免密支付/自动扣款”→选定“芒果TV”取消订阅。\r\n【微信退订】：打开微信“我”→“支付”→右上角“…”→“扣费服务”→选定“芒果TV”取消订阅。\r\n【苹果退订】：1、登录您开通连续包月时的Apple ID；2、点击苹果手机【设置】进入【iTunesStore与App Store】;点击【Apple ID】;点击【查看Apple ID】；在账户设置页面点击【订阅】；取消芒果TV会员的订阅即可（如果在订阅内无法找到选项，建议您可以咨询苹果客服协助您取消，苹果客服联系方式：4006668800）。\r\n【招行一网通退订】：打开招商银行APP“我的”→“设置”→“支付设置”→“免密支付”→选定“芒果TV”关闭服务。\r\n【移动话费退订】：请联系人工客服退订。\r\n【联通话费退订】：发送TD到10655198665。\r\n【电信话费退订】：拨打电话4008689689进行退订。","type":0,"list":[{"feedBack":[{"clickState":1,"title":"有用","feedBackId":"looyu_knowledge|30"},{"clickState":0,"title":"无用","feedBackId":"looyu_knowledge|30"}],"loginState":0,"icon":"","message":"【支付宝退订】：打开支付宝“我的”→“设置”→“支付设置”→“免密支付/自动扣款”→选定“芒果TV”取消订阅。\r\n【微信退订】：打开微信“我”→“支付”→右上角“…”→“扣费服务”→选定“芒果TV”取消订阅。\r\n【苹果退订】：1、登录您开通连续包月时的Apple ID；2、点击苹果手机【设置】进入【iTunesStore与App Store】;点击【Apple ID】;点击【查看Apple ID】；在账户设置页面点击【订阅】；取消芒果TV会员的订阅即可（如果在订阅内无法找到选项，建议您可以咨询苹果客服协助您取消，苹果客服联系方式：4006668800）。\r\n【招行一网通退订】：打开招商银行APP“我的”→“设置”→“支付设置”→“免密支付”→选定“芒果TV”关闭服务。\r\n【移动话费退订】：请联系人工客服退订。\r\n【联通话费退订】：发送TD到10655198665。\r\n【电信话费退订】：拨打电话4008689689进行退订。","knowledgeId":30,"imgUrl":"","voiceUrl":"","button":"","backImg":"","messageType":0,"videoUrl":"","backColor":"","ask":"取消连续包月","clickMessageCode":2,"clickMessage":"30","hrefLink":"","clickAction":"","desc":""}]}","search_time":"2020-11-10 18:25:20","platform":"android","device":"{"device":"vivo%20X9L","mod":"vivo%20X9L","ch":"vivo_sign","guid":"900000000579312054","uuid":"5d1056e769ba43d8850d7c61c0f79a90","idfa":"","ticket":"BTLHHGP9BHGGCI88TNRG","abroad":"0","sver":"aphone-7.1.2","oaid":"","sid":"0874a3f3-78f9-45cd-9ee1-cbec1bb19bcb","appVersion":"6.7.3","src":"mgtv","imei":"7da87e439a845f7456b15879feac79f5","gps":"","osVersion":"7.1.2","androidPatch":"6.7.3","channel":"vivo_sign","android_id":"7da87e439a845f7456b15879feac79f5","mf":"vivo","mac":"7da87e439a845f7456b15879feac79f5","did":"7da87e439a845f7456b15879feac79f5","net":"1","osType":"android","aver":"imgotv-aphone-6.7.3","isdebug":"0"}","extend":"","parameter":"c=1&jId=1&pageName=me"}],"database":"looyu","es":1605004278000,"id":1178,"isDdl":false,"mysqlType":{"id":"bigint(20)","company_id":"int(11)","request_id":"varchar(50)","did":"varchar(100)","knowledge_id":"int(11)","message_type":"int(11)","click_message":"varchar(500)","message_code":"int(11)","action":"int(11)","feed_back_id":"varchar(100)","click_state":"int(11)","message":"varchar(500)","result":"text","search_time":"timestamp","platform":"varchar(50)","device":"text","extend":"text","parameter":"text"},"old":null,"pkNames":["id"],"sql":"","sqlType":{"id":-5,"company_id":4,"request_id":12,"did":12,"knowledge_id":4,"message_type":4,"click_message":12,"message_code":4,"action":4,"feed_back_id":12,"click_state":4,"message":12,"result":2005,"search_time":93,"platform":12,"device":2005,"extend":2005,"parameter":2005},"table":"ol_robot_search","ts":1605004278190,"type":"INSERT"}'
# ss = json.loads(st)
# print(ss)


# s = {1: (1, 'a'), 5: (2, 'b'), 9: (3, 'c'), 11: (1, 'd'), 2: (9, 'e'), 3: (3, 'f')}
# x = sorted(s)
# y = sorted(s, reverse=True)
# z = x