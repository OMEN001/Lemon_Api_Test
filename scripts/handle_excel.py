# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import openpyxl
import os

from scripts.handle_yaml import do_yaml
from scripts.handle_path import DATAS_DIR

class Case_Data:
    """创建这个类通过动态设置类属性，以对象的方式保存数据"""
    pass

class HandleExcel:

    """初始化函数用于创建实例属性"""
    def __init__(self,sheetname,filename = None):
        if filename is None:
            self.filename =os.path.join(DATAS_DIR,do_yaml.read("excel","cases_path"))
        else:
            self.filename = filename
        self.sheetname = sheetname

    # 打开工作簿
    def open(self):
        self.wb = openpyxl.load_workbook(self.filename)
        self.sh = self.wb[self.sheetname]

    # 读取数据
    def read_data(self) -> object:
        # 代开工作簿
        self.open()
        #按行获取表单中所有格子
        row = list(self.sh.rows)
        # 定义一个列表用于存放数据
        cases = []
        # 定义一个列表用于存放表头数据
        title = []
        for a in row[0]:
            title.append(a.value)
        # 获取除表头以外的其他行数据
        for a in row[1:]:
            data = []
            for b in a:
                data.append(b.value)
            # 将表头和除表头以外的其他行数据通过聚合打包的方式转化为字典添加到列表中
            cases.append(dict(zip(title,data)))
        self.wb.close()
        return cases
    # 通过动态设置类属性的方式保存测试用例
    def read_data_obj(self):
        # 代开工作簿
        self.open()
        # 按行获取表单中所有格子
        row = list(self.sh.rows)
        # 定义一个列表用于存放数据
        cases = []
        # 定义一个列表用于存放表头数据
        title = []
        for a in row[0]:
            title.append(a.value)
        # 获取除表头以外的其他行数据
        for a in row[1:]:
            data = []
            for b in a:
                data.append(b.value)
            # 创建一个用例数据对象
            case = Case_Data()
            for c in (zip(title, data)):
                # 动态设置类属性将表头设置为对象的属性，对应值设为对象的属性值
                setattr(case,c[0],c[1])
            # 将该行的用例数据加入到cases中
            cases.append(case)
        print(cases)
        self.wb.close()
        return cases

    # 表格中写入数据
    def write_data(self,row,column,value):
        # 打开工作簿
        self.open()
        # 往工作簿的表格中写入数据
        self.sh.cell(row=row,column=column,value=value)
        # 保存工作簿
        self.wb.save(self.filename)
        #关闭工作簿
        self.wb.close()

if __name__ == '__main__':

    one = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    datas = os.path.join(one,"data")
    datas1 = os.path.join(datas,"cases.xlsx")
    do_excle = HandleExcel("register")
    do_excle.read_data_obj()



