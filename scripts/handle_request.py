# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import requests
import json

class HandleRequest:
    """
    如果是session会话认证requests请求不能模仿浏览器维护cookie,创建session会话对象可以解决这一问题
    """

    def __init__(self):
        # 创建回话对象，通过回话对象向服务器发起请求
        self.one_session = requests.Session()

    # 添加请求头
    def add_headers(self, header):
        # 构造请求头
        return self.one_session.headers.update(header)

    def send(self, url, method="post", data=None, is_json=True, **kwargs):
        """
       发起请求
        :param url: url地址
        :param method: 请求方法, 通常为get、post、put、delete、patch
        :param data: 传递的参数, 可以传字典、json格式的字符串、字典类型的字符串, 默认为None
        :param is_json: 是否以json的形式来传递参数, 如果为True, 则以json形式来传, 如果为False则以www-form形式来传, 默认为True
        :param kwargs: 可变参数, 可以接收关键字参数, 如headers、params、files等
        :return: None 或者 Response对象
        """
        # data可以为如下三种类型：
        # data = {"name": '可优', 'gender': True}       # 字典类型
        # data = '{"name": "可优", "gender": true}'     # json格式的字符串
        # data = "{'name': '优优', 'gender': True}"     # 字典类型的字符串
        if isinstance(data, str):  #判断data是否为str字符串类型, 如果为str类型, 会返回True, 否则返回False
            try:
                # 假设为json字符串, 先使用json.loads转化为字典
                data = json.loads(data)
            except Exception as e:
                # 如果不为json字符串会抛出异常, 然后使用eval函数来转化
                print("使用日志记录")
                data = eval(data)

        # 转换字符串中所有大写字符为小写
        method = method.lower()

        if method == "get":
            # 如果为get请求, 那么传递的data, 默认传查询字符串参数
            # res = self.one_session.get(url, params=data, **kwargs)
            res = self.one_session.request(method,url, params=data, **kwargs)

        elif method in ("post", "delete", "patch","put"):
            if is_json:  # 如果is_json为True, 那么以json格式的形式来传参
                # res = self.one_session.post(url, json=data, **kwargs)
                res = self.one_session.request(method,url, json=data, **kwargs)
            else:   # 如果is_json为False, 那么以www-form的形式来传参
                # res = self.one_session.post(url, data=data, **kwargs)
                res = self.one_session.request(method,url, data=data, **kwargs)
        else:
            res = None
            print(f"不支持【{method}】的请求方法")

        return res

    def close(self):
        # 关闭回话对象
        self.one_session.close()
# do_request = HandleRequest()

if __name__ == '__main__':
    # 1. 构造请求的url
    login_url = "http://api.lemonban.com/futureloan/member/login"

    # 2. 创建请求参数
    headers = {
        "User-Agent": "Mozilla/5.0 BaLiang",
        "X-Lemonban-Media-Type": "lemonban.v2"
    }

    login_params = {
        "mobile_phone": "18244446667",
        "pwd": "12345678",
    }

    # 3. 执行登录
    do_request = HandleRequest()  # 创建HandleRequest对象
    do_request.add_headers(headers)  # 添加公共请求头
    login_res = do_request.send(login_url, data=login_params)



