# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import cx_Oracle
import logging


class CxOracle:

    # 创建连接
    def __init__(self,username,pwd,tns):
        try:
            # cx_Oracle.connect('username','pwd','ora的tns信息')
            # tns的取值tnsnames.ora对应的配置项的值
            self.coon = CxOracle.connect(username = username,
                                         pwd = pwd,
                                         tns = tns)
        except Exception as e:
            logging.error(f"数据库连接失败具体的异常为{e}")
            raise e
        # 创建操作游标
        self.cursor = self.coon.cursor()

    def run(self,sql,is_More = False):

        # 通过游标对象执行sql
        self.cursor.execute(sql)
        # 通过连接对象提交
        self.conn.commit()

        if is_More:

            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()


    def close(self):
        # 关闭连接
        self.coon.close()
        # 关闭操作游标
        self.cursor.close()





