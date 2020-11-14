#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/12 上午10:40
# @Author  : zhaoyu
# @Site    : 下载所有训练样本
# @File    : load_samples.py
# @Software: PyCharm


import pymysql
import datetime
import traceback
import shutil
import os

# _host = '10.200.16.253'
# _port = 3306
# _user = 'video_ai_rw'
# _pwd = '_apay6bp3rsG!Ban'
# _db_name = 'bigdata_video_ai'

_host = '10.200.16.91'
_port = 3306
_user = 'root'
_pwd = '123456'
_db_name = 'bigdata_video_ai'

source_dir = '/data/online/bigdata-score-web/media'
target_dir = '/home/dataai/samples'


def query(sql, params):
    """
    查询数据集
    :param sql:
    :param params:
    :return:
    """
    result = {}
    # 打开链接
    db = pymysql.connect(host=_host, port=_port, user=_user, password=_pwd, db=_db_name,
                         charset='utf8')
    try:
        # 创建游标对象
        cursor = db.cursor()
        # case history
        print('{} 开始执行 {} {}'.format(datetime.datetime.now(), sql, params))
        cursor.execute(sql, params)
        result = cursor.fetchall()
        print('{} 执行完成 {} 影响行数 {}'.format(datetime.datetime.now(), sql, cursor.rowcount))
        cursor.close()
    except Exception as e:
        print(str(repr(e)))
        traceback.print_exc()
    finally:
        db.close()
    return result


def load_samples():
    sql = 'select * from video_ai_keywords where cate_id=1'
    keywords = query(sql, [])
    if keywords is None:
        return
    for keyword in keywords:
        try:
            keyword_id = keyword[0]
            keyword_name = keyword[3]
            tar_dir = os.path.join(target_dir, keyword_name)
            if not os.path.exists(tar_dir):
                os.makedirs(tar_dir)
            sql_checked_medias = 'select * from video_ai_checked_medias where data_status=1 and keyword_id=%s'
            checked_medias = query(sql_checked_medias, [keyword_id])
            if checked_medias is None or len(checked_medias) < 3:
                continue
            i = 0
            for checked_media in checked_medias:
                source_path = os.path.join(source_dir, checked_media[3])
                if not os.path.exists(source_path):
                    continue
                shutil.copy(source_path, os.path.join(tar_dir, "{}_{}".format(i, os.path.splitext(source_path)[-1])))
                print('from {} to {}'.format(source_path, os.path.join(tar_dir, "{}_{}".format(i, os.path.splitext(source_path)[-1]))))
                i += 1
        except Exception as e:
            print('have exception', keyword, e)


if __name__ == '__main__':
    load_samples()