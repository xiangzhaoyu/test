#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/25 下午5:42
# @Author  : zhaoyu
# @Site    : 
# @File    : test_opencv.py
# @Software: PyCharm


# Python 2/3 compatibility
from __future__ import print_function

import time
import numpy as np
import cv2

lower_red = np.array([125, 43, 46])
upper_red = np.array([155, 255, 255])

# t1 = time.time()
img_path = '/Users/xiangzy/Desktop/平台架构.png'
# img = cv2.imread(img_path)
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# mask = cv2.inRange(hsv, lower_red, upper_red)
# print(np.sum(mask == 255), img_path)
# t2 = time.time()
# print('cpu-hsv:{}'.format(t2 - t1))
#
t1 = time.time()
img = cv2.imread(img_path)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, lower_red, upper_red)
img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
lap = cv2.Laplacian(img2gray, cv2.CV_64F).var()
print(int(np.sum(mask == 255)), int(round(lap, 5) * 100000), img_path)
t2 = time.time()
print('cpu-hsv lap:{}'.format(t2 - t1))
#
# t1 = time.time()
# img = cv2.imread(img_path)
# img = cv2.UMat(img)
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# mask = cv2.inRange(hsv, lower_red, upper_red)
# print(np.sum(mask == 255), img_path)
# t2 = time.time()
# print('gpu-hsv:{}'.format(t2 - t1))

t1 = time.time()
img = cv2.imread(img_path)
img = cv2.UMat(img)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(cv2.UMat.get(hsv), lower_red, upper_red)
img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
lap = cv2.Laplacian(cv2.UMat.get(img2gray), cv2.CV_64F).var()
print(int(np.sum(mask == 255)), int(round(lap, 5) * 100000), img_path)
t2 = time.time()
print('gpu-hsv lap:{}'.format(t2 - t1))



