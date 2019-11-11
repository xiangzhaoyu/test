#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 上午12:49
# @Author  : zhaoyu
# @Site    : 
# @File    : sql.py
# @Software: PyCharm

import os, sys

#pre = "INSERT INTO `video_ai_blacklist` ( `create_time`, `update_time`,`keyword`,`author_id`,`syn_state`,`cate_id`) VALUES ('2019-02-21 09:38:14.757635','2019-02-21 09:38:14.757686','"+ +""',7,'{\"1\": 1}',4);"
classes_path = "/Users/xiangzy/PycharmProjects/test/insert.txt"
tar = '/Users/xiangzy/PycharmProjects/test/insert_1.txt'
with open(classes_path) as f:
    class_names = f.readlines()
    for c in class_names:
        print("INSERT INTO `video_ai_blacklist` ( `create_time`, `update_time`,`keyword`,`author_id`,`syn_state`,`cate_id`) VALUES ('2019-02-21 09:38:14.757635','2019-02-21 09:38:14.757686','"+ c.strip().replace('\n','') +"',7,'{\"1\": 1}',4);")
    f.close()