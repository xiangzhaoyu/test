#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 下午2:56
# @Author  : zhaoyu
# @Site    : 
# @File    : log2.py
# @Software: PyCharm

import threading
import time
from logger_helper import get_logger


def log_2_print(thread_name):
    logger = get_logger('log/log2.log', thread_name)
    while True:
        logger.info('this is log2 , thread:{} print'.format(thread_name))
        time.sleep(1)


if __name__ == '__main__':
    t1 = threading.Thread(target=log_2_print, args=('thread_1',))
    t1.start()
    t2 = threading.Thread(target=log_2_print, args=('thread_2',))
    t2.start()
    t3 = threading.Thread(target=log_2_print, args=('thread_3',))
    t3.start()
    t4 = threading.Thread(target=log_2_print, args=('thread_4',))
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()