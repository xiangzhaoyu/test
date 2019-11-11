#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 下午2:55
# @Author  : zhaoyu
# @Site    : 
# @File    : logger_helper.py
# @Software: PyCharm


import logging
from cloghandler import ConcurrentRotatingFileHandler
import os


def get_logger(file_name, logger_name):
    """
    获取logger
    :param logger_name:
    :return:
    """
    # Use an absolute path to prevent file rotation trouble.
    logfile = os.path.abspath(file_name)
    # Rotate log after reaching 512K, keep 5 old copies.
    rotateHandler = ConcurrentRotatingFileHandler(logfile, "a", 100 * 1024 * 1024, 5)
    fmt = '[%(asctime)s] [%(filename)s]:[line:%(lineno)d] [%(levelname)s] %(message)s'
    formatter = logging.Formatter(fmt)
    rotateHandler.setFormatter(formatter)

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    logger.addHandler(rotateHandler)
    return logger