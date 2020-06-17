#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 上午11:59
# @Author  : zhaoyu
# @Site    : 
# @File    : oracle2dm.py
# @Software: PyCharm


# coding: utf-8

import dmPython
import cx_Oracle
import MySQLdb
import time
import urllib
import http.client
import datetime
import sys
import os
import logging
from importlib import reload

log = logging.getLogger("airflow.task.operators")

reload(sys)
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
# sys.setdefaultencoding('utf8')

EXPORT_HOST = "10.200.16.91"
EXPORT_PROT = 3306
EXPORT_USER = "root"
EXPORT_PASS = "123456"
EXPORT_DB_NAME = "test"

IMPORT_HOST = "10.200.16.91"
IMPORT_PROT = 3306
IMPORT_USER = "root"
IMPORT_PASS = "123456"
IMPORT_DB_NAME = "test"


class Oracle2Mysql(object):

    def __init__(self):
        self._conn_import = self._init_import_conn()
        self._conn_export = self._init_export_conn()

    def _init_import_conn(self):
        try:
            _conn_import = dmPython.connect(host=IMPORT_HOST, port=IMPORT_PROT, user=IMPORT_USER,
                                           passwd=IMPORT_PASS, db=IMPORT_DB_NAME, charset="utf8")
            return _conn_import
        except Exception as ex:
            print(ex)
            pass

    def _init_export_conn(self):
        try:
            _conn_export = MySQLdb.connect(host=EXPORT_HOST, port=EXPORT_PROT, user=EXPORT_USER, passwd=EXPORT_PASS,
                                           db=EXPORT_DB_NAME, charset="utf8")
            return _conn_export
        except Exception as ex:
            print(ex)
            pass

    def data_import(self):

        try:
            pass
            cursor = self._conn_export.cursor()
            cursor2 = self._conn_import.cursor()
            query_sql = '''select name from test1'''
            cursor.execute(query_sql)
            query_sql_list = cursor.fetchall()
            query_sql_list = list(query_sql_list)
            log.info(query_sql_list)

            insert_sql = '''insert into test2(name) values (%s)'''
            cursor2.executemany(insert_sql, query_sql_list)
            self._conn_import.commit()
            self._conn_import.close()
            self._conn_export.close()
            log.info('finished insert')
        except Exception:
            raise


def system_main(args):
    try:
        da = Oracle2Mysql()
        date_now = datetime.datetime.now()
        log.info('job start time, ', date_now)
        start_time = time.time()
        da.data_import()
        end_time = time.time()
        log.info('used_time, ', (end_time - start_time))
    except Exception as ex:
        msg = 'Have Error, %s ' % ex
        # send_sms(msg)
        log.info(msg)
        raise

system_main(sys.argv)