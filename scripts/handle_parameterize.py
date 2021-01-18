# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import re

from scripts.handle_mysql import HandleMysql
from scripts.handle_yaml import HandleYaml
from scripts.handle_path import CONFIGS_USER_FILE_PATH

class Parameterize:

    not_existed_tel_pattern = r'{not_existed_tel}'
    existed_tel_pattern = r'{invest_user_tel}'

    @classmethod
    def to_param(cls,data):
        if re.search(cls.not_existed_tel_pattern,data):
            do_mysql = HandleMysql()
            data = re.sub(cls.not_existed_tel_pattern,do_mysql.create_not_existed_mobile(),data)
            do_mysql.close()

        if re.search(cls.existed_tel_pattern,data):
            doyaml = HandleYaml(CONFIGS_USER_FILE_PATH)
            data = re.sub(cls.existed_tel_pattern,doyaml.read("investor","mobile_phone"),data)

        return data


# if __name__ == '__main__':
    # one_str = '{"mobile_phone": "{not_existed_tel}", "pwd": "12345678", "type": 1, "reg_name": "KeYou"}'
    # print(type(Parameterize.to_param(one_str)))


