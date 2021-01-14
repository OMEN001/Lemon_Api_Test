# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import yaml

class HandleYaml:

    """初始化函数"""
    def __init__(self,filename):
        with open(filename,encoding="utf8") as one:
            self.data = yaml.full_load(one)


    def read(self,section,option):
        """
        :param section: 
        :param option:
        :return:
        """
        return self.data[section][option]

if __name__ == '__main__':
    handle = HandleYaml("case.yaml")
    res = handle.read("log","log_name")
    print(res)

