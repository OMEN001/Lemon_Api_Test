# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import unittest
import os

from datetime import datetime

from scripts.handle_yaml import do_yaml
from libs.HTMLTestRunnerNew import HTMLTestRunner

from scripts.handle_path import REPORTS_DIR
from scripts.handle_path import CESES_DIR


# 创建测试套件
suite = unittest.TestSuite()

# 加载测试用例套件
loder = unittest.TestLoader()

"""
测试用例的加载方式(单个测试用例、测试用例类(也就是class)、测试用例模块(单个py文件)
;加载测试用例目录下的所有测试用例(测试用例模块也就是该框架中的case目录))
"""

# 第一种方法：将一条测试用例加入测试套件中
# 创建测试用例对象：第一参数是测试用例的方法名（必须要传）
# case = TestLogin("test_login_pass")
# 将测试用例对象，加入测试套件
# suite.addTest(case)

# 第二种方法：将测试用例类中所有的测试用例，加入到测试套件
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(TestLogin))

# 第三种方法：将一个模块中的所有测试用例 加载到测试套件
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(test_login_case))

# 第四种方法：通过一个目录，去导入该目录下的所有模块种的测试用例
loader = unittest.TestLoader()
suite.addTest(loader.discover(CESES_DIR))

# 测试报告名称
result_full_path = do_yaml.read("report","name") + "_" + \
                   datetime.strftime(datetime.now(),'%Y%m%d%H%M%S') + ".html"
# 测试报告存放路径
result_full_path = os.path.join(REPORTS_DIR,result_full_path)

with open(result_full_path,"wb") as one:
    # 创建测试运行程序
    runner = HTMLTestRunner(stream=one,
                            title=do_yaml.read("report","title"),
                            description=do_yaml.read("report","description"),
                            tester=do_yaml.read("report","tester"))
    # 运行测试用例.0
    runner.run(suite)

