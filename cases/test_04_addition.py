# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import unittest
import json

from libs.ddt import data,ddt
from scripts.handle_excel import HandleExcel
from scripts.handle_request import HandleRequest
from scripts.handle_yaml import do_yaml
from scripts.handle_parameterize import Parameterize
from scripts.handle_log import do_log

@ddt
class TestAddition(unittest.TestCase):
    """读取表单数据"""
    excel = HandleExcel("add")
    cases = excel.read_data_obj()

    @classmethod
    def setUpClass(cls) -> None:
        cls.do_request = HandleRequest()
        cls.do_request.add_headers(do_yaml.read("api","version"))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.do_request.close()

    @data(*cases)
    def test_addition(self,case):
        #参数化
        new_data = Parameterize.to_param(case.data)

        #构造请求url
        new_url = do_yaml.read("api","profix") + case.url

        #发起加标请求
        res = self.do_request.send(url = new_url,data = new_data)

        #将相应报文中的数据转化为字典
        actul_value = res.json()

        #获取测试用例所在的行
        row = case.case_id + 1

        # 获取预期结果
        expected_result = case.expected

        #获取测试用例标题
        msg = case.title

        success_msg = do_yaml.read('msg', 'success_result')  # 获取用例执行成功的提示
        fail_msg = do_yaml.read('msg', 'fail_result')  # 获取用例执行失败的提示

        try:
            self.assertEqual(expected_result,actul_value.get("code"),msg = msg)

        except Exception as e:
            # 将用例执行结果写入到result_col
            self.excel.write_data(row = row ,
                                  column = do_yaml.read("excel","result_col"),
                                  value = fail_msg)
            do_log.error(f"{msg}, 执行的结果为: {fail_msg}\n具体异常为: {e}\n")
            raise e

        else:
            if "token_info" in res.text:
                token = actul_value["data"]["token_info"]["token"]
                header = {"Authorization":"Bearer " + token}
                self.do_request.add_headers(header)
                # 将用例执行结果写入到result_col
            self.excel.write_data(row=row,
                                    column=do_yaml.read("excel", "result_col"),
                                    value=success_msg)
            # info  指的时日志的收集等级
            do_log.info(f"{msg}, 执行的结果为: {success_msg}\n")

        finally:
            # 将相应实际值写入到actual_col列
            self.excel.write_data(row = row ,
                                  column =do_yaml.read("excel","actual_col"),
                                  value = res.text)



