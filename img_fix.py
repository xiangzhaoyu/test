#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 上午9:15
# @Author  : zhaoyu
# @Site    : 图片修复，主要是噪音去除
# @File    : img_fix.py
# @Software: PyCharm

import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.stats

def show_img(path):
    """
    显示图片
    :param path:
    :return:
    """
    img = cv2.imread(path)
    img_resize = cv2.resize(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), (200, 200))
    plt.imshow(img_resize)
    plt.axis("off")
    plt.show()

def GaussieNoisy(image,sigma):
    """
    给图片增加高斯噪音
    高斯噪声是指它的概率密度函数服从高斯分布（即正态分布）的一类噪声
    与椒盐噪声相似（Salt And Pepper Noise），高斯噪声（gauss noise）也是数字图像的一个常见噪声。
    椒盐噪声是出现在随机位置、噪点深度基本固定的噪声，高斯噪声与其相反，是几乎每个点上都出现噪声、噪点深度随机的噪声。
    示例：
    plt.imshow(GaussieNoisy(cv2.imread(path), 25))
    plt.show()
    :param image:
    :param sigma:
    :return:
    """
    row,col,ch = image.shape
    mean = 0
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    return noisy.astype(np.uint8)

def spNoisy(image,s_vs_p = 0.5,amount = 0.004):
    """
    椒盐噪音
    相比高斯噪声，椒盐噪声的概念非常简单，即在图像中随机选点，使其为0或255
    示例：
    plt.imshow(spNoisy(cv2.imread(path)))
    plt.show()
    :param image:
    :param s_vs_p:
    :param amount:
    :return:
    """
    row,col,ch = image.shape
    out = np.copy(image)
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    out[coords] = 1
    num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    out[coords] = 0
    return out

def ArithmeticMeanOperator(roi):
    """
    计算均值
    :param roi:
    :return:
    """
    return np.mean(roi)

def ArithmeticMeanAlogrithm(image):
    """

    :param image:
    :return:
    """
    new_image = np.zeros(image.shape)
    image = cv2.copyMakeBorder(image,1,1,1,1,cv2.BORDER_DEFAULT)
    for i in range(1,image.shape[0]-1):
        for j in range(1,image.shape[1]-1):
            new_image[i-1,j-1] = ArithmeticMeanOperator(image[i-1:i+2,j-1:j+2])
    new_image = (new_image-np.min(image))*(255/np.max(image))
    return new_image.astype(np.uint8)

def rgbArithmeticMean(image):
    """
    算术均值滤波器即求某一范围内图像的均值，代替范围中心点的值
    示例：
    plt.imshow(rgbArithmeticMean(image))
    plt.show()
    :param image:
    :return:
    """
    r,g,b = cv2.split(image)
    r = ArithmeticMeanAlogrithm(r)
    g = ArithmeticMeanAlogrithm(g)
    b = ArithmeticMeanAlogrithm(b)
    return cv2.merge([r,g,b])


def GeometricMeanOperator(roi):
    roi = roi.astype(np.float64)
    p = np.prod(roi)
    return p ** (1 / (roi.shape[0] * roi.shape[1]))


def GeometricMeanAlogrithm(image):
    new_image = np.zeros(image.shape)
    image = cv2.copyMakeBorder(image, 1, 1, 1, 1, cv2.BORDER_DEFAULT)
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            new_image[i - 1, j - 1] = GeometricMeanOperator(image[i - 1:i + 2, j - 1:j + 2])
    new_image = (new_image - np.min(image)) * (255 / np.max(image))
    return new_image.astype(np.uint8)

def rgbGemotriccMean(image):
    """
    几何均值滤波
    示例：
    plt.imshow(rgbGemotriccMean(image))
    plt.show()
    :param image:
    :return:
    """
    r,g,b = cv2.split(image)
    r = GeometricMeanAlogrithm(r)
    g = GeometricMeanAlogrithm(g)
    b = GeometricMeanAlogrithm(b)
    return cv2.merge([r,g,b])

def HMeanOperator(roi):
    roi = roi.astype(np.float64)
    if 0 in roi:
        roi = 0
    else:
        roi = scipy.stats.hmean(roi.reshape(-1))
    return roi

def HMeanAlogrithm(image):
    new_image = np.zeros(image.shape)
    image = cv2.copyMakeBorder(image,1,1,1,1,cv2.BORDER_DEFAULT)
    for i in range(1,image.shape[0]-1):
        for j in range(1,image.shape[1]-1):
            new_image[i-1,j-1] =HMeanOperator(image[i-1:i+2,j-1:j+2])
    new_image = (new_image-np.min(image))*(255/np.max(image))
    return new_image.astype(np.uint8)

def rgbHMean(image):
    """
    谐波均值
    :param image:
    :return:
    """
    r,g,b = cv2.split(image)
    r = HMeanAlogrithm(r)
    g = HMeanAlogrithm(g)
    b = HMeanAlogrithm(b)
    return cv2.merge([r,g,b])

def IHMeanOperator(roi,q):
    roi = roi.astype(np.float64)
    return np.mean((roi)**(q+1))/np.mean((roi)**(q))

def IHMeanAlogrithm(image,q):
    new_image = np.zeros(image.shape)
    image = cv2.copyMakeBorder(image,1,1,1,1,cv2.BORDER_DEFAULT)
    for i in range(1,image.shape[0]-1):
        for j in range(1,image.shape[1]-1):
            new_image[i-1,j-1] = IHMeanOperator(image[i-1:i+2,j-1:j+2],q)
    new_image = (new_image-np.min(image))*(255/np.max(image))
    return new_image.astype(np.uint8)

def rgbIHMean(image,q):
    """
    逆谐波过滤
    :param image:
    :param q:
    :return:
    """
    r,g,b = cv2.split(image)
    r = IHMeanAlogrithm(r,q)
    g = IHMeanAlogrithm(g,q)
    b = IHMeanAlogrithm(b,q)
    return cv2.merge([r,g,b])

if __name__ == '__main__':
    path = '/Users/xiangzy/Desktop/im.jpg'
    img = cv2.imread(path)
    spApple = spNoisy(img, 0.5, 0.1)
    gaussApple = GaussieNoisy(img, 25)
    plt.subplot(121)
    plt.title("Salt And peper Image")
    plt.imshow(spApple)
    plt.axis("off")
    plt.subplot(122)
    plt.imshow(gaussApple)
    plt.axis("off")
    plt.title("Gauss noise Image")
    plt.show()
    arith_sp_apple = rgbArithmeticMean(spApple)
    gemo_sp_apple = rgbGemotriccMean(spApple)
    plt.subplot(121)
    plt.title("Arithmatic to spImage")
    plt.imshow(arith_sp_apple)
    plt.axis("off")
    plt.subplot(122)
    plt.imshow(gemo_sp_apple)
    plt.axis("off")
    plt.title("Geomotric to spImage")
    plt.show()
    arith_gs_apple = rgbArithmeticMean(gaussApple)
    gemo_gs_apple = rgbGemotriccMean(gaussApple)
    plt.subplot(121)
    plt.title("Arithmatic to gsImage")
    plt.imshow(arith_gs_apple)
    plt.axis("off")
    plt.subplot(122)
    plt.imshow(gemo_gs_apple)
    plt.axis("off")
    plt.title("Geomotric to gsImage")
    plt.show()
    arith_sp_apple = rgbHMean(spApple)
    gemo_sp_apple = rgbIHMean(spApple, 3)
    plt.subplot(121)
    plt.title("H Mean to spImage")
    plt.imshow(arith_sp_apple)
    plt.axis("off")
    plt.subplot(122)
    plt.imshow(gemo_sp_apple)
    plt.axis("off")
    plt.title("IH mean to spImage")
    plt.show()
    arith_gs_apple = rgbHMean(gaussApple)
    gemo_gs_apple = rgbIHMean(gaussApple, 3)
    plt.subplot(121)
    plt.title("HMean to gsImage")
    plt.imshow(arith_gs_apple)
    plt.axis("off")
    plt.subplot(122)
    plt.imshow(gemo_gs_apple)
    plt.axis("off")
    plt.title("IHMean to gsImage")
    plt.show()


