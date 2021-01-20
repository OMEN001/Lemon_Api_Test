# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import pymysql
import random

from scripts.handle_yaml import do_yaml


class HandleMysql:

    def __init__(self):
        # 创建连接对象
        self.conn = pymysql.connect(host=do_yaml.read('mysql', 'host'),  # mysql服务器ip或者域名
                                    user=do_yaml.read('mysql', 'user'),  # 用户名
                                    password=do_yaml.read('mysql', 'password'),
                                    db=do_yaml.read('mysql', 'db'),  # 要连接的数据库名
                                    port=do_yaml.read('mysql', 'port'),  # 数据库端口号, 默认为3306(int型)
                                    charset='utf8',  # 数据库编码为utf8, 不能设为utf-8
                                    # 默认返回的结果为元祖或者嵌套元祖的列表
                                    # 可以指定cursorclass为DictCursor, 那么返回的结果为字典或者嵌套字典的列表
                                    cursorclass=pymysql.cursors.DictCursor)
        # 创建游标对象
        self.cursor = self.conn.cursor()

    # 执行查询语句
    def run(self,sql,args=None,is_more=False):
        # 通过游标对象执行sal
        self.cursor.execute(sql,args)
        # 通过连接对象提交
        self.conn.commit()
        if is_more:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()

    @staticmethod
    def create_mobile():
    # def create_mobile(self): 因为这里的self没有用到所以创建了静态方法（类中实例方法也可调用静态方法）
        """生成11位数字"""
        # return "183" + "".join(random.randint(10000000,99999999))
        return "183" + "".join(random.sample("0123456789",8))


    def is_existed_mobile(self, mobile):
        """判断收集好是否被注册"""
        sql = do_yaml.read("mysql","sql")

        if self.run(sql, args=[mobile]):
            return True
        else:
            return False

    def create_not_existed_mobile(self):

        """生成一个不存在的电话号码"""
        one_mobile = self.create_mobile()

        while True:
            if not self.is_existed_mobile(one_mobile):
                break
        return one_mobile

    def close(self):
        # 关闭游标对象
        self.cursor.close()
        # 关闭连接对象
        self.conn.close()

if __name__ == '__main__':
    sql = "select max(id) from member;"
    do_mysql = HandleMysql()
    max_id = do_mysql.run(sql)
    print(max_id["max(id)"] + 1)

    do_mysql.close()






