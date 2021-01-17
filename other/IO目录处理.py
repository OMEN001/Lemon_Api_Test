#_*_conding:utf-8_*_
#@Time    :2020/3/1315:39
#@Author  :xiaodong.wu
#@Email   :2586089125@qq.com
import os
import shutil

"""
#mkdir() 创建单个目录，在项目的根目录下生成一个文件夹（并不是包）
os.mkdir("report")

# os.makedirs() 创建多级目录
os.makedirs("list1/list2/list3")

#rmdir() 删除目录，只能删除路径下的一个空文件夹
os.rmdir("report")

# os.removedirs() 删除多个目录(必须为空目录)
os.removedirs("list1/list2/list3")

# shutil.rmtree() 空目录、有文件的目录都可以删除
shutil.rmtree("list1/list2")  #这里list2目录为空或者目录中有文件都可以将liat2删除


#remove() 删除文件，这能删除路径下的一个文件
os.remove("report/reports/list/file1.py")

# os.path.exists() 检验给出的路径是否真的存在
os.path.exists("list1/list2/file1.py")


#寻找目录/文件路径
path = os.getcwd()                   #获取当前路径，不包含当前文件
path1 = os.path.dirname(__file__)
path2 = os.path.realpath(__file__)   #获取当前路径，包含当前文件
path3 = os.path.basename(__file__)   #获取当前路径的文件名
print(path)
print(path1)
print(path2)
print(path3)

#isdir() 函数，判断是否是目录
#isfile() 函数，判断是否是文件
path4 = os.path.isdir(path1)
path5 = os.path.isfile(path1)
print(path4)
print(path5)

#listdir() 函数，返回当前路径下的所有目录，返回的数据类型是列表
path6 = os.listdir(path1)
print(path6)

path1 = os.path.dirname(__file__)
path2 = os.path.join(path1,"report/reports/list")

print(os.path.isfile(path2))
print(os.path.isdir(path2))
path3 = os.listdir(path2)

"""
path1 = os.path.dirname(__file__)
path2 = os.path.join(path1,"report/reports/list")
print(path1)
print(path2)

path3 = os.path.realpath("report/reports/list/file1.py")
path4 = os.path.isfile(path3)
print(path4)