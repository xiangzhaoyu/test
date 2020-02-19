#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/18 下午4:08
# @Author  : zhaoyu
# @Site    : 测试达梦
# @File    : dameng.py
# @Software: PyCharm

import dmPython

USER = 'U_13467555726'
PWD = 'THJwq9iDDN'
SERVER = 'ypt.dameng.com'
PORT = 30026


class DMC:
    """
    达梦数据库操作
    """
    SHOW_SQL = True

    def __init__(self, host=SERVER, port=PORT, user=USER, password=PWD):
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def get_con(self):
        try:
            conn = dmPython.connect(user=self.user, password=self.password, server=self.host, port=self.port, autoCommit=True)
            return conn
        except dmPython.Error as e:
            print("dmPython Error:%s" % e)

    def select_all(self, sql):
        try:
            con = self.get_con()
            # print(con)
            cur = con.cursor()
            # print(cur)
            cur.execute(sql)
            fc = cur.fetchall()
            # print(fc)
            return fc
        except dmPython.Error as e:
            print("dmPython Error:%s" % e)
        finally:
            cur.close()
            con.close()

    def select_by_where(self, sql, data):
        try:
            con = self.get_con()
            # print con
            d = (data,)
            cur = con.cursor()
            cur.execute(sql, d)
            fc = cur.fetchall()
            # if len(fc) > 0:
            #     for e in range(len(fc)):
            #         print(fc[e])
            return fc
        except dmPython.Error as e:
            print("dmPython Error:%s" % e)
        finally:
            cur.close()
            con.close()

    def dml_by_where(self, sql, params):
        try:
            con = self.get_con()
            cur = con.cursor()

            for d in params:
                if self.SHOW_SQL:
                    print('执行sql:[{}],参数:[{}]'.format(sql, d))
                cur.execute(sql, d)
            con.commit()

        except dmPython.Error as e:
            con.rollback()
            print("dmPython Error:%s" % e)
        finally:
            cur.close()
            con.close()

    # 不带参数的更新方法
    def dml_nowhere(self, sql):
        try:
            con = self.get_con()
            cur = con.cursor()
            count = cur.execute(sql)
            con.commit()
            return count
        except dmPython.Error as e:
            con.rollback()
            print("dmPython Error:%s" % e)
        finally:
            cur.close()
            con.close()


if __name__ == "__main__":
    db = DMC()
    # 先增加
    i1 = "insert into dm_test1 values(1, 't1')"
    db.dml_nowhere(i1)
    i2 = "insert into dm_test1 values(2, 't2')"
    db.dml_nowhere(i2)
    # 再查询
    sql = "select * from dm_test1"
    fc = db.select_all(sql)
    for row in fc:
        print(row)
