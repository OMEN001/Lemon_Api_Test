# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import os

from scripts.handle_request import HandleRequest
from scripts.handle_mysql import HandleMysql
from scripts.handle_yaml import do_yaml
from scripts.handle_path import CONFIGS_USER_FILE_PATH


# 创建mysql对象
do_mysql = HandleMysql()

# 构造请求url
url = do_yaml.read("api","profix") +"/member/register"

# 构造公共请求头
header = {
    "X-Lemonban-Media-Type": "lemonban.v2"
}

# 构造请求参数
data = {
    "mobile_phone":do_mysql.create_not_existed_mobile(),
    "pwd":"12345678",
    "type":0,
    "reg_name":"admin"
}

data1 = {
    "mobile_phone":do_mysql.create_not_existed_mobile(),
    "pwd":"12345678",
    "type":1,
    "reg_name":"borrower"
}

data2 = {
    "mobile_phone": do_mysql.create_not_existed_mobile(),
    "pwd": "12345678",
    "type": 1,
    "reg_name": "invenstor"
}

# 创建请求对象
do_request = HandleRequest()
# 添加公共请求头
do_request.add_headers(header)

# 发起请求并将请求结果转化未json
res1 = do_request.send(url=url,data=data)
res_json1 = res1.json()

res2 = do_request.send(url=url,data=data1)
res_json2 = res2.json()

res3 = do_request.send(url=url,data=data2)
res_json3 = res3.json()

user_account = {}
user_account["admin"] = res_json1["data"]
user_account["admin"]["pwd"] = "12345678"


user_account["borrower"] = res_json2["data"]
user_account["borrower"]["pwd"] = "12345678"

user_account["investor"] = res_json3["data"]
user_account["investor"]["pwd"] = "12345678"


#将数据写入指定文件
do_yaml.write(user_account,CONFIGS_USER_FILE_PATH)

# 关闭连接
do_mysql.close()







