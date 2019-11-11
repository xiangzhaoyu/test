#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 下午3:45
# @Author  : zhaoyu
# @Site    : 图片审核
# @File    : pic_audit.py
# @Software: PyCharm

def test1():
    """
    https://blog.csdn.net/TIME_LEAF/article/details/80017001
    :return:
    """

    from sys import exit
    import numpy as np
    import cv2

    # 加载图片并把它转换为灰度图片
    image = cv2.imread('/Users/xiangzy/Desktop/2.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray_Image", gray)
    # cv2.waitKey(0)
    '''
    # 索贝尔算子（Sobel operator）主要用作边缘检测，在技术上，它是一离散性差分算子，用来运算图像亮度函数的灰度之近似值。在图像的任何一点使用此算子，将会产生对应的灰度矢量或是其法矢量
    gradX = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx = 1, dy = 0, ksize = -1)
    gradY = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx = 0, dy = 1, ksize = -1)
    # x灰度减去y灰度
    gradient = cv2.subtract(gradX, gradY)
    # 转回uint8
    gradient = cv2.convertScaleAbs(gradient)  
    absX = cv2.convertScaleAbs(gradX)   # 转回uint8  
    absY = cv2.convertScaleAbs(gradY)    
    gradient = cv2.addWeighted(absX,0.5,absY,0.5,0) # 组合
    '''
    gradient = cv2.Canny(gray, 50, 400)
    cv2.imshow("S/C_Image", gradient)
    # cv2.waitKey(0)

    (_, thresh) = cv2.threshold(gradient, 250, 255, cv2.THRESH_BINARY)  # 二值化
    cv2.imshow("threshold_Image", thresh)
    # cv2.waitKey(0)
    # 构建kernel然后应用到 thresholded 图像上
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 5))  # 形态学处理，定义矩形结构
    # closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)#闭运算，先膨胀后腐蚀
    # closed = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)#开运算，先腐蚀后膨胀
    # closed = cv2.erode(thresh, kernel, iterations = 1)#腐蚀图像，去除噪声点
    closed = cv2.dilate(thresh, kernel, iterations=1)  # 膨胀图像，连接断点
    cv2.imshow("dilate_Image", closed)
    # cv2.waitKey(0)
    # 找到条码轮廓
    # 保留大的区域，有时会有没过滤掉的干扰
    im, contours, hierarchy = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    c = sorted(contours, key=cv2.contourArea, reverse=True)[0]
    # 获取轮廓数量
    x = len(contours)
    s = []
    for i in range(0, x):
        s.append(cv2.contourArea(contours[i]))
    # 打印面积
    for j in s:
        print('s was : %f' % j)

    # 筛选出面积大于等于8000的轮廓
    for k in range(0, x):
        if s[k] >= 8000.0:
            rect = cv2.minAreaRect(contours[k])  # 返回矩形的中心点坐标，长宽，旋转角度
            box = np.int0(cv2.boxPoints(rect))
            cv2.drawContours(image, [box], -1, (255, 0, 0), 2)  # 画一个方框把条形码区域圈起来
        else:
            continue

    cv2.imshow("Image", image)
    cv2.waitKey(0)
    exit(0)


# http://blog.callmewhy.com/2016/04/23/opencv-find-qrcode-position/
import cv2
from matplotlib import pyplot as plt
import numpy as np
import math

def show(img, code=cv2.COLOR_BGR2RGB):
    cv_rgb = cv2.cvtColor(img, code)
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.imshow(cv_rgb)
    fig.show()

def gray_and_edge(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    fig, ax = plt.subplots(figsize=(16, 10))
    ax.imshow(img_gray)
    fig.show()

    img_gb = cv2.GaussianBlur(img_gray, (5, 5), 0)
    ax.imshow(img_gb)
    fig.show()

    edges = cv2.Canny(img_gray, 100, 200)
    ax.imshow(edges)
    fig.show()

    img_fc, contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    hierarchy = hierarchy[0]
    found = []
    for i in range(len(contours)):
        k = i
        c = 0
        while hierarchy[k][2] != -1:
            k = hierarchy[k][2]
            c = c + 1
        if c >= 5:
            found.append(i)

    for i in found:
        img_dc = img.copy()
        cv2.drawContours(img_dc, contours, i, (0, 255, 0), 3)
        show(img_dc)

    draw_img = img.copy()
    for i in found:
        rect = cv2.minAreaRect(contours[i])
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(draw_img, [box], 0, (0, 0, 255), 2)
    show(draw_img)

    boxes = []
    for i in found:
        rect = cv2.minAreaRect(contours[i])
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        box = list(map(tuple, box))
        boxes.append(box)

    def cv_distance(P, Q):
        return int(math.sqrt(pow((P[0] - Q[0]), 2) + pow((P[1] - Q[1]),2)))

    def check(a, b):
        # 存储 ab 数组里最短的两点的组合
        s1_ab = ()
        s2_ab = ()
        # 存储 ab 数组里最短的两点的距离，用于比较
        s1 = np.iinfo('i').max
        s2 = s1
        for ai in a:
            for bi in b:
                d = cv_distance(ai, bi)
                if d < s2:
                    if d < s1:
                        s1_ab, s2_ab = (ai, bi), s1_ab
                        s1, s2 = d, s1
                    else:
                        s2_ab = (ai, bi)
                        s2 = d
        a1, a2 = s1_ab[0], s2_ab[0]
        b1, b2 = s1_ab[1], s2_ab[1]
        # 将最短的两个线画出来
        cv2.line(draw_img, a1, b1, (0,0,255), 3)
        cv2.line(draw_img, a2, b2, (0,0,255), 3)

    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            check(boxes[i], boxes[j])
    show(draw_img)

    th, bi_img = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)

    def isTimingPattern(line):
        # 除去开头结尾的白色像素点
        while line[0] != 0:
            line = line[1:]
        while line[-1] != 0:
            line = line[:-1]
        # 计数连续的黑白像素点
        c = []
        count = 1
        l = line[0]
        for p in line[1:]:
            if p == l:
                count = count + 1
            else:
                c.append(count)
                count = 1
            l = p
        c.append(count)
        # 如果黑白间隔太少，直接排除
        if len(c) < 5:
            return False
        # 计算方差，根据离散程度判断是否是 Timing Pattern
        threshold = 5
        return np.var(c) < threshold

    valid = set()
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            if check(boxes[i], boxes[j]):
                valid.add(i)
                valid.add(j)
    print(valid)

    contour_all = np.array([])
    while len(valid) > 0:
        c = found[valid.pop()]
        for sublist in c:
            for p in sublist:
                contour_all.append(p)

    rect = cv2.minAreaRect(contour_all)
    box = cv2.boxPoints(rect)
    box = np.array(box)

    draw_img = img.copy()
    cv2.polylines(draw_img, np.int32([box]), True, (0, 0, 255), 10)
    show(draw_img)

# img = cv2.imread('/Users/xiangzy/Desktop/2.jpg')
# 不使用0 会有断言错误：https://github.com/aleju/imgaug/issues/157 这里可以用 1 或 0尝试
img = cv2.imread('/Users/xiangzy/Desktop/2.jpg')
# show(img, cv2.COLOR_BGR2GRAY)
gray_and_edge(img)

def test3():
    """
    http://ju.outofmemory.cn/entry/362681
    :return:
    """
    from pyzbar import pyzbar
    import argparse
    import cv2

    # 构建参数解析器并解析参数
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=False,
                    help="path to input image", default='/Users/xiangzy/Desktop/1553505182122.jpg')
    args = vars(ap.parse_args())

    # 加载输入图像
    image = cv2.imread(args["image"])

    # 图片放大
    image_resize = cv2.resize(image, None, fx=5, fy=5, interpolation=cv2.INTER_CUBIC)
    image = image_resize

    # 找到图像中的条形码并进行解码
    barcodes = pyzbar.decode(image)

    # 循环检测到的条形码
    for barcode in barcodes:
        # 提取条形码的边界框的位置
        # 画出图像中条形码的边界框
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # 条形码数据为字节对象，所以如果我们想在输出图像上
        # 画出来，就需要先将它转换成字符串
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        # 绘出图像上条形码的数据和条形码类型
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    .5, (0, 0, 255), 2)

        # 向终端打印条形码数据和条形码类型
        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))

    # 展示输出图像
    cv2.imshow("Image", image)
    cv2.waitKey(0)


# if __name__ == '__main__':
#     test3()

