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
from scripts.handle_mysql import HandleMysql
from scripts.handle_log import do_log

@ddt
class TestRecharge(unittest.TestCase):
    """读取表格数据"""
    excel = HandleExcel("recharge")
    cases = excel.read_data_obj()

    @classmethod
    def setUpClass(cls) -> None:
        # 创建请求对象
        cls.do_request = HandleRequest()
        # 添加公共请求头
        cls.do_request.add_headers(do_yaml.read("api","version"))
        #创建mysql对象
        cls.do_mysql = HandleMysql()


    @classmethod
    def tearDownClass(cls) -> None:
        # 关闭请求对象
        cls.do_request.close()
        cls.do_mysql.close()

    @data(*cases)
    def test_recharge(self,case):
        # 参数化
        new_data = Parameterize.to_param(case.data)

        # 构造请求url
        new_url = do_yaml.read("api","profix") + case.url

        check_sql = case.check_sql
        # 判断check_sql字段是否为空（非空即为True）
        if check_sql: # 如果check_sql不为空, 则代表当前用例需要进行数据校验
            #参数化check_sql
            check_sql = Parameterize.to_param(case.check_sql)
            #执行sql获取充值前金额
            mysql_data = self.do_mysql.run(check_sql)
            # 不是float类型, 也不是int类型, 是decimal类型
            amount_before = float(mysql_data["leave_amount"])
            # 由于使用float转化之后的数, 有可能小数位数超过2位, 需要使用round保留2位小数
            amount_before = round(amount_before,2)

        #发起请求
        res = self.do_request.send(url = new_url,data = new_data)

        # 将相应报文中的数据转化为字典
        actual_value = res.json()

        #获取测试用例的行
        row = case.case_id + 1

        #获取预期结果
        expected_result = case.expected

        # 获取测试用例的标题
        msg = case.title

        success_msg = do_yaml.read('msg', 'success_result')  # 获取用例执行成功的提示
        fail_msg = do_yaml.read('msg', 'fail_result')  # 获取用例执行失败的提示
        try:
            self.assertEqual(actual_value.get("code"),expected_result,msg = msg)
            if check_sql:
                check_sql = Parameterize.to_param(check_sql)
                mysql_data = self.do_mysql.run(sql=check_sql)
                amount_after = float(mysql_data["leave_amount"])
                amount_after = round(amount_after,2)

                #从data中取出充值金额
                data = json.loads(new_data,encoding="utf8")
                # 充值金额
                current_recharge_amount = data["amount"]
                #充值后金额
                actual_amount = round(amount_before + current_recharge_amount,2)
                self.assertEqual(amount_after,actual_amount,msg = "数据库中的金额有误")

        except Exception as e:
            # 将用例执行结果写入到result_col
            self.excel.write_data(row=row,
                                  column=do_yaml.read("excel", "result_col"),
                                  value=fail_msg)

            # error 指的时日志的收集等级
            do_log.error(f"{msg}, 执行的结果为: {fail_msg}\n具体异常为: {e}\n")
            raise e

        else:
            if "token_info" in res.text:
                token = actual_value["data"]["token_info"]["token"]
                header = {"Authorization":"Bearer "+ token}
                self.do_request.add_headers(header)

            # 将用例执行结果写入到result_col
            self.excel.write_data(row=row,
                                    column=do_yaml.read("excel", "result_col"),
                                    value=success_msg)
            # info  指的时日志的收集等级
            do_log.info(f"{msg}, 执行的结果为: {success_msg}\n")

        finally:
            # 将相应实际值写入到actual_col列
            self.excel.write_data(row=row,
                                  column=do_yaml.read("excel", "actual_col"),
                                  value=res.text)

if __name__ == '__main__':
    unittest.main()
