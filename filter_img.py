#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/13 下午6:39
# @Author  : zhaoyu
# @Site    : 
# @File    : filter_img.py
# @Software: PyCharm

import os
import cv2
import numpy as np
import concurrent.futures
import shutil
import argparse
import sys


lower_red = np.array([125, 43, 46])
upper_red = np.array([155, 255, 255])


def get_pic_hsv(imgPath):
    """
    获取图片hsv值
    :param imgPath:
    :return:
    """
    try:
        if not os.path.exists(imgPath):
            return (0, imgPath)
        img = cv2.imread(imgPath)
        # change to hsv model
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # get mask 利用inRange()函数和HSV模型中蓝色范围的上下界获取mask，mask中原视频中的蓝色部分会被弄成白色，其他部分黑色。
        mask = cv2.inRange(hsv, lower_red, upper_red)
        return (np.sum(mask == 255), imgPath)
    except Exception as e:
        print(imgPath, e)
        return (0, imgPath)


def filter_pics(source_dir, target_dir, top_n=10):
    """
    过滤图片并输出
    :param source_dir:
    :param target_dir:
    :param top_n:
    :return:
    """
    print('筛选开始')
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    for dir_name in os.listdir(source_dir):
        img_path = os.path.join(source_dir, dir_name)
        if not os.path.isdir(img_path):
            continue
        imgs = []
        for img_name in os.listdir(img_path):
            if os.path.splitext(img_name)[-1] not in ['.jpg', '.png', '.jpeg']:
                continue
            imgs.append(os.path.join(img_path, img_name))
        target_path = os.path.join(target_dir, dir_name)
        # 处理的图片列表
        top_n_pics = []
        if not os.path.exists(target_path):
            os.makedirs(target_path)
            # 获取hsv值
            with concurrent.futures.ThreadPoolExecutor() as executor:
                hsv_result = list(executor.map(get_pic_hsv, imgs))
            # 排序取前5
            hsv_result_dict = {}
            if hsv_result:
                for hr in hsv_result:
                    if not hr or len(hr) != 2:
                        continue
                    hsv_result_dict[hr[0]] = hr[1]
            current_n = 0
            for key in sorted(hsv_result_dict, reverse=True):
                if current_n > top_n:
                    break
                value = hsv_result_dict[key]
                if value:
                    top_n_pics.append(value)
                    current_n += 1
        # 写入目标图
        for imp in top_n_pics:
            shutil.copy(imp, os.path.join(target_path, os.path.split(imp)[-1]))
            print('{} copy to {}'.format(imp, os.path.join(target_path, os.path.split(imp)[-1])))
    print('------------------------------------------------------')
    print('筛选完成')


def get_pic_hsv_lap(img_path):
    """
    获取图片的hsv和lap值
    :param img_path:
    :return:
    """
    try:
        if not os.path.exists(img_path):
            return 0, 0, img_path
        img = cv2.imread(img_path)
        # change to hsv model
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # get mask 利用inRange()函数和HSV模型中蓝色范围的上下界获取mask，mask中原视频中的蓝色部分会被弄成白色，其他部分黑色。
        mask = cv2.inRange(hsv, lower_red, upper_red)
        # change to gray
        img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # get lap
        lap = cv2.Laplacian(img2gray, cv2.CV_64F).var()
        return np.sum(mask == 255), lap, img_path
    except Exception as e:
        print(img_path, e)
        return 0, 0, img_path


def filter_pics_2(source_dir, target_dir, top_n=10):
    """
    测试virspanel exc_dir_task_2
    :param source_dir:
    :param target_dir:
    :param top_n:
    :return:
    """
    print('筛选开始')
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    for dir_name in os.listdir(source_dir):
        img_path = os.path.join(source_dir, dir_name)
        if not os.path.isdir(img_path):
            continue
        imgs = []
        for img_name in os.listdir(img_path):
            if os.path.splitext(img_name)[-1] not in ['.jpg', '.png', '.jpeg']:
                continue
            imgs.append(os.path.join(img_path, img_name))
        target_path = os.path.join(target_dir, dir_name)
        # 处理的图片列表
        top_n_pics = []
        if not os.path.exists(target_path):
            os.makedirs(target_path)
            # 获取hsv值
            with concurrent.futures.ThreadPoolExecutor() as executor:
                hsv_result = list(filter(None, executor.map(get_pic_hsv_lap, imgs)))
            # 取hsv top 20
            hsv_result_dict = {}
            result_dict = {}
            if hsv_result:
                for hr in hsv_result:
                    if not hr or len(hr) != 3:
                        continue
                    hsv_result_dict[hr[0]] = hr[2]
                    result_dict[hr[2]] = (hr[0], hr[1])
            lap_result_dict = {}
            current_n = 0
            top_n = 20
            for key in sorted(hsv_result_dict, reverse=True):
                if current_n > top_n:
                    break
                value = hsv_result_dict[key]
                if value:
                    lap_result_dict[result_dict[value][1]] = value
                    current_n += 1
            # 去lap top 5
            current_n = 0
            top_n = 5
            for key in sorted(lap_result_dict, reverse=True):
                if current_n > top_n:
                    break
                value = lap_result_dict[key]
                if value:
                    top_n_pics.append(value)
                    current_n += 1
        # 写入目标图
        for imp in top_n_pics:
            shutil.copy(imp, os.path.join(target_path, os.path.split(imp)[-1]))
            print('{} copy to {}'.format(imp, os.path.join(target_path, os.path.split(imp)[-1])))
    print('------------------------------------------------------')
    print('筛选完成')


def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('source_dir', type=str,
                        help="原始图片目录")
    parser.add_argument('target_dir', type=str,
                        help="输出图片目录")
    return parser.parse_args(argv)


if __name__ == '__main__':
    args = parse_arguments(sys.argv[1:])
    filter_pics_2(args.source_dir, args.target_dir, 20)