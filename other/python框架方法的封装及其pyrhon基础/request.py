# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import requests
import json

from log import do_log


class handlerequest:

    def __init__(self):
        """
        这里通过回话对象发起请求是因为request请求不能模拟浏览器处理cookie,而回话对象可以模拟浏览器来处理cookie
        """
        self.one_session = requests.Session()

    def add_header(self,header):
        #添加公共请求头
        return  self.one_session.headers.update(header)

    def send(self,url,method = "post",data = None,is_json = True,**kwargs):
        """
        :param url: url地址
        :param method: 请求方法, 通常为get、post、put、delete、patch
        :param data: 传递的参数, 可以传字典、json格式的字符串、字典类型的字符串, 默认为None
        :param is_json: 是否以json的形式来传递参数, 如果为True, 则以json形式来传, 如果为False则以www-form形式来传, 默认为True
        :param kwargs: 可变参数, 可以接收关键字参数, 如headers、params、files等
        :return: None 或者 Response对象
        """
        # data可以为如下三种类型：
        # data = {"name": 'BaLiang', 'gender': True}       # 字典类型
        # data = '{"name": "BaLiang", "gender": true}'     # json格式的字符串
        # data = "{'name': 'BaLiang', 'gender': True}"     # 字典类型的字符串
        if isinstance(data,str):
            try:
                # 假设为json字符串, 先使用json.loads转化为字典
                data = json.loads(data)
            except Exception as e:
                do_log.error(f"数据{data}的格式不正确，具体异常为{e}\n")
                # 如果不为json字符串会抛出异常, 然后使用eval函数来转化
                data = eval(data)

        # 转换字符串中所有大写字符为小写
        method = method.lower()

        if method == "get":
            # 如果为get请求, 那么传递的data, 默认传查询字符串参数
            # res = self.one_session.get(url, params=data, **kwargs)
            res = self.one_session.request(method,url, params=data, **kwargs)

        elif method in ("post", "delete", "patch","put"):
            # 如果is_json为True, 那么以json格式的形式来传参
            if is_json:
                res = self.one_session.request(method,url, json = data, **kwargs)
            # 如果is_json为False, 那么以www-form的形式来传参
            else:
                res = self.one_session.request(method, url, data = data, **kwargs)
        else:
            res = None
            print(f"不支持【{method}】的请求方法")

        return res

    def close(self):
        #关闭回话对象
        self.one_session.close()

