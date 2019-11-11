#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 下午3:50
# @Author  : zhaoyu
# @Site    : 
# @File    : pic_audit_zbar.py
# @Software: PyCharm


def audit_use_zbar(img_path):
    """
    http://ju.outofmemory.cn/entry/362681
    :return:
    """
    from pyzbar import pyzbar
    import cv2

    # 加载输入图像
    image = cv2.imread(img_path)

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


if __name__ == '__main__':
    audit_use_zbar('/Users/xiangzy/Desktop/二维码/5.png')