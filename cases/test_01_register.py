# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import unittest


from scripts.handle_excel import HandleExcel
from libs.ddt import ddt,data
from scripts.handle_request import HandleRequest
from scripts.handle_yaml import do_yaml
from scripts.handle_parameterize import Parameterize
from scripts.handle_log import do_log




@ddt
class TestRegister(unittest.TestCase):
    """
    测试用例类的调试方法（1）鼠标放在测试用例类上右键run或者debug
                    (2)使用if __name__ == '__main__':
                            unittest.main()  运行

    """

    # 创建HandleExcel
    excel = HandleExcel('register')
    # 读取excel中register表单下的所有数据
    cases = excel.read_data_obj()

    @classmethod
    def setUpClass(cls) -> None:  # 所有用例执行前, 会被调用一次
        # 创建请求对象
        cls.do_request = HandleRequest()
        # 添加公共请求头
        cls.do_request.add_headers(do_yaml.read("api", "version"))

    @classmethod
    def tearDownClass(cls) -> None:# 所有用例执行结束之后, 会被调用一次
        cls.do_request.close() # 释放session会话资源

    @data(*cases)
    def test_register(self,case):

        # 参数化
        new_data = Parameterize.to_param(case.data)

        # 构造url
        new_url = do_yaml.read("api","profix") + case.url

        # 向服务器发起请求
        res = self.do_request.send(url=new_url,# url地址
                                   # method=case.method, # 请求方法
                                   data=new_data # 请求参数
                                   # is_json=True   # 是否以json格式来传递数据, 默认为True
                                   )
        #将响应报文转化为json
        actual_value = res.json()

        #获取响应报文的行号
        row = case.case_id + 1

        #获取预期结果
        expected_result = case.expected

        # 获取测试用例的标题
        msg = case.title
        #获取用例成功与失败的提示
        success_msg = do_yaml.read('msg', 'success_result')
        fail_msg = do_yaml.read('msg', 'fail_result')

        try:
            self.assertEqual(expected_result, actual_value.get('code'), msg=msg)

        except Exception as e:
            # # # 将相应实际值写入到actual_col列
            # self.excel.write_data(row = row,
            #                      column = do_yaml.read("excel","actual_col"),
            #                      value = res.text)
            # 将用例执行结果写入到result_col
            self.excel.write_data(row=row,
                                 column=do_yaml.read("excel", "result_col"),
                                 value=fail_msg)
            # error 指的时日志的收集等级
            do_log.error(f"{msg}, 执行的结果为: {fail_msg}\n具体异常为: {e}\n")
            raise e
        else:
            # # # 将相应实际值写入到actual_col列
            # self.excel.write_data(row = row,
            #                      column = do_yaml.read("excel","actual_col"),
            #                      value = res.text)
            # 将用例执行结果写入到result_col
            self.excel.write_data(row = row,
                                 column = do_yaml.read("excel", "result_col"),
                                 value = success_msg)
            # info  指的时日志的收集等级
            do_log.info(f"{msg}, 执行的结果为: {success_msg}\n")
        finally:
            # 将相应实际值写入到actual_col列
            self.excel.write_data(row=row,
                                 column=do_yaml.read("excel", "actual_col"),
                                 value=res.text)

# if __name__ == '__main__':
#     unittest.main()








