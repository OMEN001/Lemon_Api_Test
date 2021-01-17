# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import re

from scripts.handle_mysql import HandleMysql

class Parameterize:

    not_existed_tel_pattern = r'{not_existed_tel}'

    @classmethod
    def to_param(cls,data):
        if re.search(cls.not_existed_tel_pattern,data):
            do_mysql = HandleMysql()
            data = re.sub(cls.not_existed_tel_pattern,do_mysql.create_not_existed_mobile(),data)
            do_mysql.close()

        return data


# if __name__ == '__main__':
    # one_str = '{"mobile_phone": "{not_existed_tel}", "pwd": "12345678", "type": 1, "reg_name": "KeYou"}'
    # print(type(Parameterize.to_param(one_str)))


