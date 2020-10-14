#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 上午11:32
# @Author  : zhaoyu
# @Site    : 
# @File    : delete_feed_bell.py
# @Software: PyCharm

import pymysql
import datetime

_host = '10.200.8.89'
_port = 7001
_user = 'fantuan_rw'
_pwd = '6cCSKkZQBmTtnPMR'
_db_name = 'fantuan'

# _host = '10.43.15.42'
# _port = 7017
# _user = 'fantuan_rw'
# _pwd = 'rXs8aD_5x8e*TzJd'
# _db_name = 'fantuan'

# 打开链接
db = pymysql.connect(host=_host, port=_port, user=_user, password=_pwd, db=_db_name,
                     charset='utf8')
try:
    # 创建游标对象
    cursor = db.cursor()
    # query sql
    query_sql = 'select id,feed_id,fnatuan_id,bell_type, count(*) as fc from feed_bell group by feed_id,fnatuan_id,bell_type having fc >1'
    print('{} 开始执行 {}'.format(datetime.datetime.now(), query_sql))
    cursor.execute(query_sql, [])
    result = cursor.fetchall()
    print('{} 执行完成 {} 影响行数 {}'.format(datetime.datetime.now(), query_sql, cursor.rowcount))
    # cursor.close()

    # 逐行删除
    for fb in result:
        try:
            # 查询符合条件的删除对象
            delete_query = 'select id from feed_bell where feed_id=%s and fnatuan_id=%s and bell_type=%s'
            cursor.execute(delete_query, [fb[0], fb[1], fb[2]])
            delete_result = cursor.fetchall()

            d_count = 1
            for dr in delete_result:
                if d_count == len(delete_result):
                    break
                delete_sql = 'delete from feed_bell where id=%s'
                cursor.execute(delete_sql, [dr[0]])
                d_count += 1
                print('delete id {}'.format(dr))

            # 提交删除
            db.commit()
            # print('delete fb {}'.format(fb))
            # break
        except Exception as dfb:
            print('delete fb exception {}'.format(str(dfb)))

    cursor.close()
except Exception as e:
    print('query dt exception {}'.format(str(repr(e))))
finally:
    db.close()