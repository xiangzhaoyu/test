#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 下午4:19
# @Author  : zhaoyu
# @Site    : 
# @File    : zq.py
# @Software: PyCharm


import xml.etree.ElementTree as ET
import os
import shutil


def tmp_split_img():
    r_dir = '/Users/xiangzy/Downloads/2796d732d475dadc-1#1'
    for d in os.listdir(r_dir):
        e_dir = os.path.join(r_dir, d)
        if not os.path.isdir(e_dir):
            continue
        is_txt = False
        is_mul = False
        is_xml = False
        for i in os.listdir(e_dir):
            if os.path.splitext(i)[-1] in ['.txt']:
                is_txt = True
            if os.path.splitext(i)[-1] in ['.xml']:
                is_xml = True
            if is_txt and is_xml:
                is_mul = True
        if is_mul:
            shutil.move(e_dir, "/Users/xiangzy/Downloads/mul")
            continue
        if is_txt:
            shutil.move(e_dir, "/Users/xiangzy/Downloads/txt")
        if is_xml:
            shutil.move(e_dir, "/Users/xiangzy/Downloads/xml")


def filter_img(s_dir, t_dir):
    """
    过滤图片，只要有xml标记的图片
    :param s_dir:
    :param t_dir:
    :return:
    """
    if not os.path.exists(t_dir):
        os.makedirs(t_dir)
    for d in os.listdir(s_dir):
        e_dir = os.path.join(s_dir, d)
        if not os.path.isdir(e_dir):
            continue
        for i in os.listdir(e_dir):
            file_name = os.path.splitext(i)[0]
            file_ext = os.path.splitext(i)[-1]
            if file_ext not in ['.xml']:
                continue
            # 有xml文件则验证两个文件是否存在，存在就准备复制

            img_path = os.path.join(e_dir, file_name + '.jpg')
            if not os.path.exists(img_path):
                continue
            t_e_dir = os.path.join(t_dir, d)
            if not os.path.exists(t_e_dir):
                os.makedirs(t_e_dir)
            t_img_path = os.path.join(t_e_dir, file_name + '.jpg')
            shutil.copy(img_path, t_img_path)
            print(img_path + ' copy to ' + t_img_path)
            xml_path = os.path.join(e_dir, file_name + '.xml')
            t_xml_path = os.path.join(t_e_dir, file_name + '.xml')
            shutil.copy(xml_path, t_xml_path)
            print(xml_path + ' copy to ' + t_xml_path)


def convert_annotation(classes, xmlPath, imgPath):
    """
    转换一个文件的xml
    :param classes:
    :param xmlPath:
    :param imgPath:
    :return:
    """
    result = ''
    try:
        if classes is not None and os.path.exists(xmlPath) and os.path.exists(imgPath):
            with open(xmlPath) as xf:
                tree = ET.parse(xf)
                root = tree.getroot()
                result = imgPath
                for obj in root.iter('object'):
                    difficult = obj.find('difficult').text
                    cls = obj.find('name').text
                    if cls not in classes or int(difficult) == 1:
                        continue
                    cls_id = classes.index(cls)
                    xmlbox = obj.find('bndbox')
                    b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text),
                         int(xmlbox.find('ymax').text))
                    result = result + " " + ",".join([str(a) for a in b]) + ',' + str(cls_id)
    except Exception as e:
        print(e)
    return result


def xml_2_yolo(s_dir, t_path):
    """
    xml转yolo
    :param s_dir:
    :param t_path:
    :return:
    """
    classes = ['TB', 'TB2']
    with open(t_path, 'w') as tf:
        for e in os.listdir(s_dir):
            e_dir = os.path.join(s_dir, e)
            if not os.path.isdir(e_dir):
                continue
            for i in os.listdir(e_dir):
                if os.path.splitext(i)[-1] not in ['.jpg']:
                    continue
                file_name = os.path.splitext(i)[0]
                img_path = os.path.join(e_dir, i)
                xml_path = os.path.join(e_dir, file_name + '.xml')
                if not os.path.exists(img_path) or not os.path.exists(xml_path):
                    continue
                content = convert_annotation(classes, xml_path, img_path)
                if len(content) < len(img_path):
                    continue
                tf.write(content)
                tf.write('\n')
                print(content)


def del_txt(t_dir):
    """

    :param t_dir:
    :return:
    """
    for e in os.listdir(t_dir):
        if not os.path.isdir(os.path.join(t_dir, e)):
            continue
        for i in os.path.join(t_dir, e):
            if os.path.splitext(i)[-1] in ['.txt']:
                os.remove(os.path.join(os.path.join(t_dir, e), i))


def check_dir(t_dir):
    """
    检查当前目录下是否有三级目录
    :param t_dir:
    :return:
    """
    for d1 in os.listdir(t_dir):
        d1_dir = os.path.join(t_dir, d1)
        if os.path.isdir(d1_dir):
            for d2 in os.listdir(d1_dir):
                d2_dir = os.path.join(d1_dir, d2)
                if os.path.isdir(d2_dir):
                    print(d2_dir + "下面有目录请查看")
                    break


def getFiles(t_dir):
    files = []
    for file in os.listdir(t_dir):
        x_dir = os.path.join(t_dir, file)
        if os.path.isdir(x_dir):
            fs = getFiles(x_dir)
            files.extend(fs)
        else:
            files.append(x_dir)
    return files


def del_rubbshi(s_dir):
    # 删除git直接拷贝产生的垃圾文件
    # s_dir = '/Volumes/HIKVISION/pycharm/tianqi'
    files = getFiles(s_dir)
    for f in files:
        if not os.path.isfile(f):
            continue
        xx = os.path.split(f)[-1]
        if xx[0:2] == '._':
            os.remove(f)
            # print(f)


if __name__ == '__main__':
    # check_dir('/Users/xiangzy/Desktop/xx')
    # filter_img('/Users/xiangzy/Desktop/x2', '/Users/xiangzy/Desktop/x3')
    xml_2_yolo('/Volumes/HIKVISION/pycharm/tianqi/train_data/20201201/xml', '/Volumes/HIKVISION/pycharm/tianqi/train_data/20201201/data.txt')





