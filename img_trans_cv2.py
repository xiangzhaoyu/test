#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 上午9:42
# @Author  : zhaoyu
# @Site    : 使用opencv进行图像变换
# @File    : img_trans_cv2.py
# @Software: PyCharm

import cv2
from PIL import Image
import os
import logging as log
log.basicConfig(
    format='[%(asctime)s] [%(filename)s]:[line:%(lineno)d] [%(levelname)s] %(message)s', level=log.INFO)

class ImgPre:

    def __init__(self, rootPath, export_path_base):
        self.rootPath = rootPath  # 图像完整路径
        self.export_path_base = export_path_base

        # 创建输出根目录
        try:
            if not os.path.exists(export_path_base):
                os.mkdir(export_path_base)
        except Exception as e:
            log.error(e)
        log.info('ImgPre: %s', rootPath)

    def get_savename(self, operate):
        """
        :param export_path_base: 图像输出路径
        :param operate: 脸部区域名
        :return: 返回图像存储名
        """
        try:
            import time
            # 获取时间戳，用于区分图像
            now = time.time()
            tail_time = str(round(now * 1000000))[-4:]  # 时间戳尾数
            head_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
            # 时间标签
            label = str(head_time + tail_time)

            # 输出文件夹
            export_path_base = self.export_path_base
            # 子文件夹以“操作operate”命名
            out_path = export_path_base + operate
            # 创建子文件夹
            if not os.path.exists(out_path):
                os.mkdir(out_path)

            # 存储完整路径
            savename = out_path + '/' + operate + '_' + label + ".jpg"

            # 日志
            log.info('save:%s', savename)
            return savename

        except Exception as e:
            log.error('get_savename ERROR')
            log.error(e)

    def lightness(self, light):
        """改变图像亮度.
        推荐值：
            0.87，1.07
        明亮程度
            darker < 1.0 <lighter
        """
        try:
            operate = 'lightness_' + str(light)
            # 图像完整路径
            rootPath = self.rootPath

            with Image.open(rootPath) as image:
                # 图像左右翻转
                out = image.point(lambda p: p * light)
                # 重命名
                savename = self.get_savename(operate)
                # 图像存储
                out.save(savename)

            # 日志
            # logger.info(operate)
        except Exception as e:
            log.error('ERROR %s', operate)
            log.error(e)

    def rotate(self, angle):
        """图像旋转15度、30度."""
        try:
            operate = 'rotate_' + str(angle)
            # 图像完整路径
            rootPath = self.rootPath

            with Image.open(rootPath) as image:
                # 图像左右翻转
                out = image.rotate(angle)
                # 重命名
                savename = self.get_savename(operate)
                # 图像存储
                out.save(savename, quality=100)

            # 日志
            # logger.info(operate)
        except Exception as e:
            log.error('ERROR %s', operate)
            log.error(e)

    def transpose(self):
        """图像左右翻转操作."""
        try:
            operate = 'transpose'
            # 图像完整路径
            rootPath = self.rootPath

            with Image.open(rootPath) as image:
                # 图像左右翻转
                out = image.transpose(Image.FLIP_LEFT_RIGHT)
                # 重命名
                savename = self.get_savename(operate)
                # 图像存储
                out.save(savename, quality=100)  # quality=100

            # 日志
            # logger.info(operate)
        except Exception as e:
            log.error('ERROR %s', operate)
            log.error(e)

    def deform(self):
        """图像拉伸."""
        try:
            operate = 'deform'
            # 图像完整路径
            rootPath = self.rootPath

            with Image.open(rootPath) as image:
                w, h = image.size
                w = int(w)
                h = int(h)
                # 拉伸成宽为w的正方形
                out_ww = image.resize((int(w), int(w)))
                savename = self.get_savename(operate + '_ww')
                out_ww.save(savename, quality=100)
                # 拉伸成宽为h的正方形
                out_ww = image.resize((int(h), int(h)))
                savename = self.get_savename(operate + '_hh')
                out_ww.save(savename, quality=100)

            # 日志
            # logger.info(operate)
        except Exception as e:
            log.error('ERROR %s', operate)
            log.error(e)

    def crop(self):
        """提取四个角落和中心区域."""
        try:
            operate = 'crop'
            # 图像完整路径
            rootPath = self.rootPath

            with Image.open(rootPath) as image:
                w, h = image.size
                # 切割后尺寸
                scale = 0.875
                # 切割后长宽
                ww = int(w * scale)
                hh = int(h * scale)
                # 图像起点，左上角坐标
                x = y = 0

                # 切割左上角
                x_lu = x
                y_lu = y
                out_lu = image.crop((x_lu, y_lu, ww, hh))
                savename = self.get_savename(operate + '_lu')
                out_lu.save(savename, quality=100)
                # logger.info(operate + '_lu')

                # 切割左下角
                x_ld = int(x)
                y_ld = int(y + (h - hh))
                out_ld = image.crop((x_ld, y_ld, ww, hh))
                savename = self.get_savename(operate + '_ld')
                out_ld.save(savename, quality=100)
                # logger.info(operate + '_ld')

                # 切割右上角
                x_ru = int(x + (w - ww))
                y_ru = int(y)
                out_ru = image.crop((x_ru, y_ru, w, hh))
                savename = self.get_savename(operate + '_ru')
                out_ru.save(savename, quality=100)
                # logger.info(operate + '_ru')

                # 切割右下角
                x_rd = int(x + (w - ww))
                y_rd = int(y + (h - hh))
                out_rd = image.crop((x_rd, y_rd, w, h))
                savename = self.get_savename(operate + '_rd')
                out_rd.save(savename, quality=100)
                # logger.info(operate + '_rd')

                # 切割中心
                x_c = int(x + (w - ww) / 2)
                y_c = int(y + (h - hh) / 2)
                out_c = image.crop((x_c, y_c, ww, hh))
                savename = self.get_savename(operate + '_c')
                out_c.save(savename, quality=100)
                # logger.info('提取中心')
        except Exception as e:
            log.error('ERROR %s', operate)
            log.error(e)

    def cv2_resize(self, w, h):
        """
        使用opencv对图片进行大小改变
        :param w:
        :param h:
        :return:
        """
        try:
            operate = 'resize'
            # 图像完整路径
            rootPath = self.rootPath

            image = cv2.imread(rootPath)

            # 直接缩放
            # img = cv2.resize(image, (w, h))
            # 不直接指定缩放后大小，通过fx和fy指定缩放比例，0.5则长宽都为原来一半
            # 等效于img_200x300 = cv2.resize(img, (300, 200))，注意指定大小的格式是(宽度,高度)
            # 插值方法默认是cv2.INTER_LINEAR，这里指定为最近邻插值
            img = cv2.resize(image, (0, 0), fx=0.2, fy=0.5,
                              interpolation=cv2.INTER_NEAREST)
            # 重命名
            savename = self.get_savename(operate)
            # 图像存储
            cv2.imwrite(savename, img)

            # 日志
            #log.info(operate)
        except Exception as e:
            log.error('ERROR %s', operate)
            log.error(e)


def test():
    # 源地址和输出地址
    rootPath = '/Users/xiangzy/Desktop/1097048/1097048_31.mp4_25.0_35.0_875_0.jpg'
    export_path_base = '/Users/xiangzy/Desktop/img_trans/'
    # 声明类对象
    imgPre = ImgPre(rootPath, export_path_base)

    """
    imgPre.deform()
    imgPre.transpose()
    imgPre.rotate(15)
    imgPre.rotate(30)
    imgPre.crop()
    imgPre.lightness(1.07)
    imgPre.lightness(0.87)
    """
    imgPre.cv2_resize(100,200)


if __name__ == '__main__':
    import datetime

    print('start...')
    # 计时
    start_time = datetime.datetime.now()

    test()

    end_time = datetime.datetime.now()
    time_consume = (end_time - start_time).microseconds / 1000000

    log.info('start_time: %s', start_time)
    log.info('end_time: %s', end_time)
    log.info('time_consume: %s(s)', time_consume)  # 0.280654(s)

    log.info('main finish')