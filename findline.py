#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/24 下午1:13
# @Author  : zhaoyu
# @Site    : 寻找照片中的线条
# @File    : findline.py
# @Software: PyCharm


import sys
import os
import cv2
import time
import numpy as np

# os.environ["CUDA_VISIBLE_DEVICES"] = "0"
logo_main_path = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(logo_main_path)[0]
sys.path.append(rootPath)


def get_laplacian(img):
    """
    描述：
        计算图片清晰度，目前标准为300以上算清晰
    """
    imageVar = 0.0
    try:
        img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imageVar = cv2.Laplacian(img2gray, cv2.CV_64F).var()
    except Exception as e:
        print(repr(e))
    return imageVar


# 设置颜色区间hsv值
# -- 红色 1
# lower_red = np.array([0, 43, 46])
# upper_red = np.array([10, 255, 255])
# -- 红色 2
# lower_red = np.array([156, 43, 46])
# upper_red = np.array([180, 255, 255])
# -- 紫色
lower_red = np.array([125, 43, 46])
upper_red = np.array([155, 255, 255])


def split_video(videopath):
    """
    拆分视频
    :param videopath:
    :return:
    """
    start = time.time()
    cap = cv2.VideoCapture(videopath)  # 打开视频文件
    num = 1
    while True:
        # success 表示是否成功，data是当前帧的图像数据；.read读取一帧图像，移动到下一帧
        success, data = cap.read()
        if not success:
            break
        lap = get_laplacian(data)
        # cv2.imwrite('/Users/xiangzy/Desktop/1-2/' + str(num) + ".jpg", data)

        num = num + 1
        print("{} lap {}".format(num, lap))
    cap.release()
    print('视频拆分时长：{:.2f}s'.format((time.time() - start)))


def split_video1(videopath):
    # video_dir = os.path.split(videopath)[0]
    # video_file_name = os.path.split(videopath)[1].split('.')[0]
    # img_dir = os.path.join(video_dir, video_file_name)
    # if not os.path.exists(img_dir):
    #     os.mkdir(img_dir)
    #
    # data_txt = []

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
        # cv2.imshow("test", mask)
        # cv2.imwrite('/Users/xiangzy/Desktop/202005241514/' + str(num) + ".jpg", mask)

        # cv2.imwrite(os.path.join(img_dir, str(num) + '__o.jpg'), data)
        # cv2.imwrite(os.path.join(img_dir, str(num) + '__h.jpg'), mask)

        imageVar = 0
        # imageVar = cv2.Laplacian(mask, cv2.CV_64F).var()

        num += 1
        # data_txt.append('num: {} {} {}\n'.format(num, np.sum(mask == 255), imageVar))
        print('num: {} {} {}'.format(num, np.sum(mask == 255), imageVar))

    cap.release()
    # data_txt.append('视频拆分时长：{:.2f}s\n'.format((time.time() - start)))
    print('视频拆分时长：{:.2f}s'.format((time.time() - start)))
    # with open(os.path.join(img_dir, 'data.txt'), 'w') as f:
    #     for txt in data_txt:
    #         f.write(txt)
    # cv2.destroyAllWindows()


if __name__ == '__main__':
    path = '/Users/xiangzy/Desktop/202005241514/202005241514522020.avi'
    split_video1(path)