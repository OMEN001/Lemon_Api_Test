# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import yaml

class handleyaml:

    """初始化方法：打开并读取yaml文件数据"""
    def __init__(self,filename):
        with open(filename,encoding="utf8") as one:
            # 读取出的数据我嵌套字典的字典
            self.data = yaml.full_load(one)

    # 读取数据
    def read(self,section,option):
        return self.data[section][option]

    @staticmethod
    # 这里为静态方法的原因为（1）写入的数据到变得yaml文件中去
    #                  （2）没有用到类中的data和filename和类无关
    def write_data(data,filename):
        with open(filename,"w",encoding="utf8") as two:
            # allow_unicode=True中文转译
            yaml.dump(data,two,allow_unicode=True)

do_yaml = handleyaml("case.yaml")
data = {
    "excel":{"cases_path":"cases.xlsx", "result_col": 5},
    "msg":{"success_result": "Success","fail_result": "Fail"}}
handleyaml.write_data(data,"case1.yaml")
