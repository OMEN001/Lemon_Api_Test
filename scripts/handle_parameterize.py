# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import re

from scripts.handle_mysql import HandleMysql
from scripts.handle_yaml import HandleYaml
from scripts.handle_path import CONFIGS_USER_FILE_PATH

class Parameterize:

    #创建yaml对象
    doyaml = HandleYaml(CONFIGS_USER_FILE_PATH)

    not_existed_tel_pattern = r'{not_existed_tel}'
    existed_tel_pattern = r'{invest_user_tel}'
    existed_tel_pattern_pwd = r'{invest_user_pwd}'
    error_user_pwd = r'{invest_user_pwd}8'
    invest_user_id = r'{invest_user_id}'
    invest_user_tel = r'{invest_user_tel}'
    invest_user_pwd = r'{invest_user_pwd}'
    not_existed_id = r'{not_existed_id}'
    borrow_user_id = r'{borrow_user_id}'
    borrow_user_tel = r'{borrow_user_tel}'
    borrow_user_pwd = r'{borrow_user_pwd}'


    @classmethod
    def to_param(cls,data):
        if re.search(cls.not_existed_tel_pattern,data):
            do_mysql = HandleMysql()
            data = re.sub(cls.not_existed_tel_pattern,do_mysql.create_not_existed_mobile(),data)
            do_mysql.close()

        if re.search(cls.existed_tel_pattern,data):
            # doyaml = HandleYaml(CONFIGS_USER_FILE_PATH)
            data = re.sub(cls.existed_tel_pattern,cls.doyaml.read("investor","mobile_phone"),data)

        if re.search(cls.existed_tel_pattern_pwd,data):
            # doyaml = HandleYaml(CONFIGS_USER_FILE_PATH)
            data = re.sub(cls.existed_tel_pattern_pwd,cls.doyaml.read("investor","pwd"),data)

        if re.search(cls.error_user_pwd,data):
            do_mysql = HandleMysql()
            data = re.sub(cls.error_user_pwd,do_mysql.create_not_existed_mobile(),data)
            do_mysql.close()

        if re.search(cls.invest_user_id,data):
            # doyaml = HandleYaml(CONFIGS_USER_FILE_PATH)
            data = re.sub(cls.invest_user_id,str(cls.doyaml.read("investor","id")),data)

        if re.search(cls.invest_user_tel,data):
            # doyaml = HandleYaml(CONFIGS_USER_FILE_PATH)
            data = re.sub(cls.invest_user_tel,cls.doyaml.read("investor","mobile_phone"),data)

        if re.search(cls.invest_user_pwd,data):
            # doyaml = HandleYaml(CONFIGS_USER_FILE_PATH)
            data = re.sub(cls.invest_user_pwd,cls.doyaml.read("investor","pwd"),data)

        if re.search(cls.not_existed_id,data):
            do_mysql = HandleMysql()
            sql = "select max(id) from member;"
            max_id = do_mysql.run(sql)
            data = re.sub(cls.not_existed_id,str(max_id["max(id)"]+1),data)
            do_mysql.close()

        if re.search(cls.borrow_user_id,data):
            # doyaml = HandleYaml(CONFIGS_USER_FILE_PATH)
            data = re.sub(cls.borrow_user_id,str(cls.doyaml.read("borrower","id")),data)

        if re.search(cls.borrow_user_tel,data):
            # doyaml = HandleYaml(CONFIGS_USER_FILE_PATH)
            data = re.sub(cls.borrow_user_tel,cls.doyaml.read("borrower","mobile_phone"),data)

        if re.search(cls.borrow_user_pwd,data):
            # doyaml = HandleYaml(CONFIGS_USER_FILE_PATH)
            data = re.sub(cls.borrow_user_pwd,cls.doyaml.read("borrower","pwd"),data)

        return data

# if __name__ == '__main__':
    # one_str = '{"mobile_phone": "{not_existed_tel}", "pwd": "12345678", "type": 1, "reg_name": "KeYou"}'
    # print(type(Parameterize.to_param(one_str)))
    doyaml = HandleYaml(CONFIGS_USER_FILE_PATH)
    # data = {"member_id": {invest_user_id},"amount":600}
    # invest_user_id = r'{invest_user_id}'
    # re.search(invest_user_id,data)
    # datas = re.sub(invest_user_id,doyaml.read("investor","id"),data)
    # print(type(doyaml.read("investor","id")))


