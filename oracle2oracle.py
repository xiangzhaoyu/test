#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 上午11:59
# @Author  : zhaoyu
# @Site    : 
# @File    : oracle2dm.py
# @Software: PyCharm


# coding: utf-8

import cx_Oracle
import MySQLdb
import time
import urllib
import http.client
import datetime
import sys
import os
from importlib import reload


reload(sys)
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
# sys.setdefaultencoding('utf8')

EXPORT_HOST = "10.200.16.91"
EXPORT_PROT = 1521
EXPORT_USER = "laotie"
EXPORT_PASS = "123456"
EXPORT_DB_NAME = "orcl.oracle"

IMPORT_HOST = "10.200.16.91"
IMPORT_PROT = 1521
IMPORT_USER = "laotie"
IMPORT_PASS = "123456"
IMPORT_DB_NAME = "orcl.oracle"


class Oracle2Mysql(object):

    def __init__(self):
        self._conn_import = self._init_import_conn()
        self._conn_export = self._init_export_conn()

    def _init_import_conn(self):
        try:
            _conn_import = cx_Oracle.connect(IMPORT_USER, IMPORT_PASS,
                                             '{}:{}/{}'.format(IMPORT_HOST, IMPORT_PROT, IMPORT_DB_NAME))
            return _conn_import
        except Exception as ex:
            print(ex)
            pass

    def _init_export_conn(self):
        try:
            # _conn_export = cx_Oracle.connect('laotie/123456@127.0.0.1:1521/orcl.oracle');
            _conn_export = cx_Oracle.connect(EXPORT_USER, EXPORT_PASS, '{}:{}/{}'.format(EXPORT_HOST, EXPORT_PROT, EXPORT_DB_NAME))
            return _conn_export
        except Exception as ex:
            print(ex)
            pass

    def data_import(self):

        try:
            pass
            cursor = self._conn_export.cursor()
            cursor2 = self._conn_import.cursor()
            query_sql = '''select name from test'''
            cursor.execute(query_sql)
            query_sql_list = cursor.fetchall()
            query_sql_list = list(query_sql_list)
            print(query_sql_list)
            # n_qs = []
            # for q in query_sql_list:
            #     n_qs.append((q[0]))
            # print(n_qs)

            insert_sql = '''insert into test1(name) values (:1)'''
            cursor2.executemany(insert_sql, query_sql_list)
            self._conn_import.commit()
            self._conn_import.close()
            self._conn_export.close()
            print('finished insert')
        except Exception:
            raise


def system_main(args):
    try:
        da = Oracle2Mysql()
        date_now = datetime.datetime.now()
        print('job start time, ', date_now)
        start_time = time.time()
        da.data_import()
        end_time = time.time()
        print('used_time, ', (end_time - start_time))
    except Exception as ex:
        msg = 'Have Error, %s ' % ex
        # send_sms(msg)
        print(msg)
        raise

system_main(sys.argv)