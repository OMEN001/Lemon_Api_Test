# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import logging
import os

from datetime import datetime
from scripts.handle_path import LOGS_DIR
from scripts.handle_yaml import do_yaml

class HandleLog:

    @classmethod
    def create_log(cls):
        # 创建一个日志收集器
        my_log = logging.getLogger(do_yaml.read("log","log_name"))
        # 设置日志的收集等级
        my_log.setLevel("DEBUG")

        # 设置日志的输出格式
        formater = "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"

        # 创建一个输出到控制台的日志输出渠道
        sh = logging.StreamHandler()
        # 设置输出到控制台的日志输出等级
        sh.setLevel("DEBUG")
        # 设置日志的输出格式
        sh.setFormatter(logging.Formatter(formater))
        # 将输出到控制台的日志输出渠道添加到日志收集器
        my_log.addHandler(sh)

        # 日志文件生成路径
        filepath = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S') + "_" + do_yaml.read("log", "logfile_name")

        # 创建输出到文件的日志输出渠道
        fh = logging.FileHandler(filename = os.path.join(LOGS_DIR,filepath),encoding="utf8")
        # 设置输出到文件的日志格式
        fh.setFormatter(logging.Formatter(formater))
        # 设置输出刀片文件的日志输出等级
        fh.setLevel("DEBUG")
        #将输出到控制台的日志输出渠道添加到日志收集器
        my_log.addHandler(fh)

        return my_log

do_log = HandleLog.create_log()

if __name__ == '__main__':
    do_log.info("这是一个info等级的日志信息")
    do_log.debug("这是一个debug等级的日志信息")


