#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/24 下午5:08
# @Author  : zhaoyu
# @Site    : 
# @File    : parallel.py
# @Software: PyCharm


import os
import cv2
import time
import numpy as np
import concurrent.futures


lower_red = np.array([125, 43, 46])
upper_red = np.array([155, 255, 255])


def split_video(videopath):
    """
    切图
    :param videopath:
    :return:
    """
    video_dir = os.path.split(videopath)[0]
    video_file_name = os.path.split(videopath)[1].split('.')[0]
    img_dir = os.path.join(video_dir, video_file_name)
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)

    data_txt = []
    highs = {}

    start = time.time()
    cap = cv2.VideoCapture(videopath)  # 打开视频文件
    num = 1
    while True:
        # success 表示是否成功，data是当前帧的图像数据；.read读取一帧图像，移动到下一帧
        success, data = cap.read()
        if not success:
            break
        # change to hsv model
        hsv = cv2.cvtColor(data, cv2.COLOR_BGR2HSV)

        # get mask 利用inRange()函数和HSV模型中蓝色范围的上下界获取mask，mask中原视频中的蓝色部分会被弄成白色，其他部分黑色。
        mask = cv2.inRange(hsv, lower_red, upper_red)

        # 存储原图
        if not os.path.join(os.path.join(img_dir, 'original')):
            os.mkdir(os.path.join(img_dir, 'original'))
        cv2.imwrite(os.path.join(img_dir, str(num) + '__o.jpg'), data)
        # 存储目标图
        if not os.path.exists(os.path.join(img_dir, 'high')):
            os.mkdir(os.path.join(img_dir, 'high'))
        # cv2.imwrite(os.path.join(os.path.join(img_dir, 'high'), str(num) + '__h.jpg'), mask)
        highs[int(np.sum(mask == 255))] = [num, mask, data]

        # lap
        lap = cv2.Laplacian(mask, cv2.CV_64F).var()

        num += 1
        data_txt.append('num: {} {} {}\n'.format(num, np.sum(mask == 255), lap))
        print('num: {} {} {}'.format(num, np.sum(mask == 255), lap))

    cap.release()
    data_txt.append('视频拆分时长：{:.2f}s\n'.format((time.time() - start)))
    # print('视频拆分时长：{:.2f}s'.format((time.time() - start)))
    with open(os.path.join(img_dir, 'data.txt'), 'w') as f:
        for txt in data_txt:
            f.write(txt)
    # 取top n 清晰度图片存储
    n = 0
    for key in sorted(highs, reverse=True):
        value = highs[key]
        print('num {} key {}'.format(key, value[0]))
        cv2.imwrite(os.path.join(os.path.join(img_dir, 'high'), str(value[0]) + '__h.jpg'), value[1])
        cv2.imwrite(os.path.join(os.path.join(img_dir, 'high'), str(value[0]) + '__o.jpg'), value[2])
        if n > 6:
            break
        n += 1
    return videopath


def parallel_split(videodir):
    """
    并行切图
    :param videodir:
    :return:
    """
    # 串行处理 58.85s
    start = time.time()
    for avi in os.listdir(videodir):
        if os.path.splitext(avi)[1] != '.avi':
            continue
        split_video(os.path.join(videodir, avi))
    print('视频拆分时长：{:.2f}s'.format((time.time() - start)))

    # 并行 37.63
    # start = time.time()
    # avis = []
    # xxx = []
    # for avi in os.listdir(videodir):
    #     if os.path.splitext(avi)[1] != '.avi':
    #         continue
    #     avis.append(os.path.join(videodir, avi))
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     xxx = list(executor.map(split_video, avis))
    # print('视频拆分时长：{:.2f}s'.format((time.time() - start)))
    # print(xxx)


if __name__ == '__main__':
    path = '/Users/xiangzy/Desktop/202005241514'
    parallel_split(path)