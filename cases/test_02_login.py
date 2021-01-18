# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import unittest
import json

from libs.ddt import ddt,data
from scripts.handle_excel import HandleExcel
from scripts.handle_request import HandleRequest
from scripts.handle_yaml import do_yaml
from scripts.handle_parameterize import Parameterize
from scripts.handle_log import do_log


@ddt
class TestLogin(unittest.TestCase):

    excel = HandleExcel("login")
    cases = excel.read_data_obj()

    @classmethod
    def setUpClass(cls) -> None: #所有用例执行前会被调用一次
        # 创建请求对象
        cls.do_request = HandleRequest()
        # 添加公共请求头
        cls.do_request.add_headers(do_yaml.read("api","version"))

    @classmethod
    def tearDownClass(cls) -> None: #所有用例执行结束后会被调用一次
        #释放session会话资源
        cls.do_request.close()

    @data(*cases)
    def test_login(self,case):
        #参数化
        new_data = Parameterize.to_param(case.data)

        #构造请求url
        new_url = do_yaml.read("api","profix") + case.url

        #发起请求
        res = self.do_request.send(url = new_url,data = new_data)

        #将响应报文转化为json
        actual_value = res.json()

        # 获取测试用例行号
        row = case.case_id + 1

        # 获取预期结果
        expected_result = json.loads(case.expected,encoding="utf8")

        #获取测试用例的标题
        msg = case.title

        success_msg = do_yaml.read('msg', 'success_result')  # 获取用例执行成功的提示
        fail_msg = do_yaml.read('msg', 'fail_result')  # 获取用例执行失败的提示
        try:
            # 先断言code, 再断言msg
            self.assertEqual(expected_result.get("code"),actual_value.get("code"),msg = msg)
            self.assertEqual(expected_result.get("msg"),actual_value.get("msg"),msg = msg)

        except Exception as e:
            # 将用例执行结果写入到result_col
            self.excel.write_data(row = row,
                                  column = do_yaml.read("excel","result_col"),
                                  value = fail_msg)

            # error 指的时日志的收集等级
            do_log.error(f"{msg}, 执行的结果为: {fail_msg}\n具体异常为: {e}\n")
            raise e

        else:
            # 将用例执行结果写入到result_col
            self.excel.write_data(row = row,
                                  column = do_yaml.read("excel","result_col"),
                                  value = success_msg)
            # info  指的时日志的收集等级
            do_log.info(f"{msg}, 执行的结果为: {success_msg}\n")

        finally:
            # 将相应实际值写入到actual_col列
            self.excel.write_data(row=row,
                                  column=do_yaml.read("excel", "actual_col"),
                                  value=res.text)


if __name__ == '__main__':
    unittest.main()







