# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import logging

class handlelog:

    # 这里创建类方法是为了方便调用
    @classmethod
    def create_log(cls):
        #创建日志收集器
        my_log = logging.getLogger("log")
        #设置日志收集等级
        my_log.setLevel("DEBUG")

        #设置日志的输出格式
        formater =  "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"

        #创建输出到控制台的日志输出渠道
        sh = logging.StreamHandler()
        # 设置输出到控制台的输出格式
        sh.setFormatter(logging.Formatter(formater))
        #设置输出到控制台的日志输出等级
        sh.setLevel("DEBUG")
        #将输出渠道添加到收集器
        my_log.addHandler(sh)

        #创建输出到文件的日志输出渠道
        fh = logging.FileHandler("test.log",encoding="utf8")
        # 设置输出到文件的日志输出格式
        fh.setFormatter(logging.Formatter(formater))
        #设置输出到渠道的日志收集等级
        fh.setLevel("DEBUG")
        #将输出到文件的日志输出渠道添加到收集器
        my_log.addHandler(fh)

        return my_log

do_log = handlelog.create_log()
if __name__ == '__main__':
    do_log.info("这是一个INFO等级的日志信息")
