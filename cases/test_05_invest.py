# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import unittest

from libs.ddt import ddt,data
from scripts.handle_excel import HandleExcel
from scripts.handle_request import HandleRequest
from scripts.handle_yaml import do_yaml
from scripts.handle_parameterize import Parameterize
from scripts.handle_mysql import HandleMysql
from scripts.handle_log import do_log


@ddt
class TestInvest(unittest.TestCase):

    excel = HandleExcel("invest")
    cases = excel.read_data_obj()

    @classmethod
    def setUpClass(cls) -> None:
        cls.do_request = HandleRequest()
        cls.do_request.add_headers(do_yaml.read("api","version"))
        cls.do_mysql = HandleMysql()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.do_request.close()
        cls.do_mysql.close()

    @data(*cases)
    def test_invest(self,case):
        #参数化
        new_data = Parameterize.to_param(case.data)

        #构造请求URL
        new_url = do_yaml.read("api","profix") + case.url

        res = self.do_request.send(url = new_url,
                                   method = case.method,
                                   data = new_data)

        #将响应报文转化为字典类型
        actul_value = res.json()

        #获取测试用例所在的行
        row = case.case_id + 1

        #获取预期结果
        expected_result = case.expected

        #获取测试用例标题
        msg = case.title

        # 获取用例执行成功的提示
        success_msg = do_yaml.read('msg', 'success_result')
        # 获取用例执行失败的提示
        fail_msg = do_yaml.read('msg', 'fail_result')

        try:
            self.assertEqual(actul_value.get("code"),expected_result,msg = msg)
            # check_sql = case.check_sql
            # if check_sql:
            #     check_sql = Parameterize.to_param(case.check_sql)
            #     mysql_data = self.do_mysql.run(sql=check_sql)
            #     loan_id = mysql_data["id"]
            #     setattr(Parameterize, "loan_id", loan_id)

        except Exception as e:
            # 将用例执行结果写入到result_col
            self.excel.write_data(row = row,
                                  column = do_yaml.read("excel","result_col"),
                                  value = fail_msg)
            #
            do_log.error(f"{msg}, 执行的结果为: {fail_msg}\n具体异常为: {e}\n")
            raise e


        else:
            if "token_info" in res.text:
                token = actul_value["data"]["token_info"]["token"]
                header = {"Authorization":"Bearer " + token}
                self.do_request.add_headers(header)

            # 获取表的编号
            check_sql = case.check_sql
            if check_sql:
                check_sql = Parameterize.to_param(case.check_sql)
                mysql_data = self.do_mysql.run(sql=check_sql)
                loan_id = mysql_data["id"]
                setattr(Parameterize, "loan_id", loan_id)

            # 取出load id的第二种方法
            # if case.case_id == 2:
            #     load_id = actual_value["data"]["id"]
            #     setattr(Parameterize, 'loan_id', load_id)

            # 将用例执行结果写入到result_col
            self.excel.write_data(row=row,
                                  column=do_yaml.read("excel", "result_col"),
                                  value=success_msg)
            do_log.info(f"{msg}, 执行的结果为: {success_msg}\n")

        finally:
            # 将相应实际值写入到actual_col列
            self.excel.write_data(row=row,
                                  column=do_yaml.read("excel", "actual_col"),
                                  value=res.text)






