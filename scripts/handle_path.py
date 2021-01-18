# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187

import os


# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取配置文件所在的路径
CONFIGS_DIR = os.path.join(BASE_DIR, "configs")
CONFIGS_FILE_PATH = os.path.join(CONFIGS_DIR,"case.yaml")
# 用户文件保存路劲
CONFIGS_USER_FILE_PATH = os.path.join(CONFIGS_DIR,"user.yaml")

#获取日志文件所在的目录路径
LOGS_DIR = os.path.join(BASE_DIR,"logs")

# 获取测试报告所在项目路径
REPORTS_DIR = os.path.join(BASE_DIR,"reports")

# 获取excel文件所在路径
DATAS_DIR = os.path.join(BASE_DIR,"data")

# 获取测试用例路径
CESES_DIR = os.path.join(BASE_DIR,"cases")
