# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import openpyxl

# 用于存放测试用例
class case_data:
    pass

class handleexcel:
    """初始化函数:类中的实例方法都会用到实例属性实例属性的值不一样"""
    def __init__(self,filename,sheetname):
        self.filename = filename
        self.sheetname = sheetname

    def open(self):
        # 打开工作簿
        self.wb = openpyxl.load_workbook(self.filename)
        # 获取sheet表单
        self.sh = self.wb[self.sheetname]

    def read_data(self):
        #打开表格
        self.open()
        #按行获取表格数据
        row = list(self.sh.rows)
        # 用于存放测试用例
        cases = []
        #用于存放表头数据
        title = []
        for a in row[0]:
            title.append(a.value)
        for a in row[1:]:
            # 用于存放测试用例数据
            data = []
            for b in a:
                data.append(b.value)
            cases.append(dict(zip(title,data)))
        # 关闭工作簿
        self.wb.close()
        return cases

    # 通过动态设置类属性的方式保存测试用例
    def read_data_obj(self):
        # 打开工作簿
        self.open()
        # 按行获取表格数据（将对象转化为列表）
        row = list(self.sh.rows)
        # 定义列表用于存放测试用例对象
        cases = []
        # 定义一个列表用于存放表头数据
        title = []
        for a in row[0]:
            title.append(a.value)
        for a in row[1:]:
            data = []
            for b in a:
                data.append(b.value)
            # 创建一个用例数据对象
            case = case_data()
            for c in zip(title,data):
                # 不能在这里创建用例数据对象,否则每循环一次就要创建一个对象
                # case = case_data()
                print(case)
                setattr(case,c[0],c[1])
            # 将该行的用例数据加入到cases中
            cases.append(case)
        self.wb.close()
        return cases

    def write_data(self,row,column,value):
        # 打开工作簿
        self.open()
        #表单中写入数据
        self.sh.cell(row = row,column = column,value = value)
        #保存数据
        self.wb.save(self.filename)
        #关闭工作簿
        self.wb.close()

do_excel = handleexcel("cases.xlsx","register")
# res = do_excel.read_data()
# do_excel.write_data(2,8,"通过")
res = do_excel.read_data_obj()
print(res)
