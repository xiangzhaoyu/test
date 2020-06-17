#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/14 下午9:20
# @Author  : zhaoyu
# @Site    : 
# @File    : draw_img.py
# @Software: PyCharm

import json
import os
import numpy as np
from PIL import Image, ImageFont, ImageDraw


def draw_img(image, out_boxes):
    """
    画图
    :param image:
    :param out_boxes:
    :param out_scores:
    :param out_classes:
    :return:
    """
    for box in out_boxes:
        top, left, bottom, right = box
        # top = max(0, np.floor(top + 0.5).astype('int32'))
        # left = max(0, np.floor(left + 0.5).astype('int32'))
        # bottom = min(image.size[1], np.floor(bottom + 0.5).astype('int32'))
        # right = min(image.size[0], np.floor(right + 0.5).astype('int32'))
        draw = ImageDraw.Draw(image)
        # 左上角x，左上角y，右下角x，右下角y
        draw.rectangle([left, top, right, bottom], outline=(255, 0, 0))
    image.save('xxxxx.jpg')


if __name__ == '__main__':
    image = Image.open('/Volumes/xiangzy_16/aaa/000.jpg', 'r')
    with open('/Volumes/xiangzy_16/aaa/000_config.json', 'rb') as f:
        data = json.load(f)
        boxs = []
        for j in data:
            box = j.get('Rect', "")
            box = box.split(',')
            box = [int(box[0]), int(box[1]), int(box[0]) + int(box[2]), int(box[1]) + int(box[3])]
            boxs.append(box)
        draw_img(image, boxs)