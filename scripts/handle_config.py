# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
from configparser import ConfigParser

class HandleConfig:

    """初始化函数"""
    def __init__(self,filename):
        # self.filename = filename
        self.config = ConfigParser()
        self.config.read(filename,encoding="utf8")

    # 获取整形数据
    def get_int(self, section, option):
        return self.config.getint(section, option)

    # 获取布尔类型的数据
    def get_boolean(self, section, option):
        return self.config.getboolean(section, option)
    # 获取浮点类型的数据
    def get_float(self, section, option):
        return self.config.getfloat(section, option)

    # 获取其他类型的数据（如列表）
    def get(self, section, option):
        return self.config.get(section, option)

    # 配置文件中写入数据
    @staticmethod
    def write_data(data, filename):
        config = ConfigParser()
        for key in data:
            config[key] = data[key]
        with open(filename, "w", encoding="utf8") as file:
            config.write(file)


if __name__ == '__main__':
    handle = HandleConfig("conf1.conf")
    handle.get("excel","cases_path")
    data = {
        "excle":{
            "name":"胡汉三",
            "age":"35"
        },
        "result":{
            "ngx":"sprit"
        }
    }
    handle.write_data(data,"conf2.conf")



