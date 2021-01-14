# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import logging

class HandleLog:

    @classmethod
    def create_log(cls):
        # 创建日志收集器
        # 日志收集器name默认为root
        my_log = logging.getLogger("loger")
        # 设置日志收集器的收集等级
        my_log.setLevel("DEBUG")
        # 设置日志的输出格式
        formatter = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        # 设置输出到控制台的日志输出渠道
        sh = logging.StreamHandler()
        # 设置输出等级
        sh.setLevel("DEBUG")
        # 设置日志的输出格式
        sh.setFormatter(logging.Formatter(formatter))
        # 将输出到控制台的输出渠道添加到日志收集器中
        my_log.addHandler(sh)
        #设置输出到文件的日志输出渠道
        fh = logging.FileHandler("test.log",encoding="utf8")
        # 设置日志的输出格式
        sh.setFormatter(logging.Formatter(formatter))
        fh.setLevel("DEBUG")
        #将输出渠道添加到日志收集器中
        my_log.addHandler(fh)
        # 返回日志收集器
        return my_log

do_log = HandleLog.create_log()

if __name__ == '__main__':
    do_log.info("这是一个INFO等级的日志信息")
    do_log.debug("这是一个DEBUG等级的日志信息")
    do_log.warning("这是一个WARN等级的日志信息")

