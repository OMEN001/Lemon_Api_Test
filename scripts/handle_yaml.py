# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import yaml

from scripts.handle_path import CONFIGS_FILE_PATH

class HandleYaml:

    """初始化函数"""
    def __init__ (self,filename):
        with open(filename,encoding="utf8") as one:
            self.data = yaml.full_load(one)

    # 读取数据
    def read(self,section,option):
        """
        :param section: 
        :param option:
        :return:
        """
        return self.data[section][option]

    @staticmethod
    def write(data,filename):
        """
        :param data:
        :param filename:
        :return:
        """
        with open(filename, mode="w", encoding="utf-8") as one_file:
            yaml.dump(data, one_file, allow_unicode=True)


do_yaml = HandleYaml(CONFIGS_FILE_PATH)

if __name__ == '__main__':
    # handle = HandleYaml("case.yaml")
    # res = handle.read("log","log_name")
    # print(res)
    # data = {
    #     "excel":{"cases_path":"cases.xlsx", "result_col": 5},
    #     "msg":{"success_result": "Success","fail_result": "Fail"}}
    # handle.write(data,"cases.yaml")
    print(do_yaml.read("report","name"))

