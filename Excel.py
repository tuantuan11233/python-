#!/miniconda3/bin/python3
# -*- coding:utf-8 -*-

import xlwt, xlrd
from xlutils.copy import copy

'''

#xlwt只能写不能读
list = [['姓名', '年龄', '性别', '分数'], ['mary', 20, '女', 90.9], ['mary', 21, '女', 90.9], ['mary', 22, '女', 0.9], ['mary', 23, '女', 89.9]]

print(len(list))
book = xlwt.Workbook()#新建一个excel
sheet = book.add_sheet('test_sheet')#添加一个sheet页
row = 0#控制行

for i in list:
    col = 0#控制列
    for s in i:
        sheet.write(row, col, s)#再循环里面list的值，每一列
        col += 1
    row += 1

sheet.write(5, 0, '王冶')
book.save('wangye.xls')#保存到当前目录下


for i in range(0, len(list[0])):
    print(i)

'''
#xlrd只能读不能写
book = xlrd.open_workbook('wangye.xls')#打开一个excel
sheet = book.sheet_by_index(0)#根据顺序获取sheet
sheet2 = book.sheet_by_name('test_sheet')#根据sheet页名字获取sheet

print(sheet.cell(0, 0).value)#指定行和列获取数据
print(sheet.cell(0, 1).value)
print(sheet.cell(0, 2).value)
print(sheet.cell(0, 3).value)
print(sheet.ncols)#获取excel里面有多少列
print(sheet.nrows)#获取excel里面有多少行

print(sheet.get_rows())#
for i in sheet.get_rows():
    print(i)#获取每一行的数据

print(sheet.row_values(0))#获取第一行
for i in range(sheet.nrows):#0 1 2 3 4 5
    print(sheet.row_values(i))#获取第几行的数据

print(sheet.col_values(1))#取第一列的数据
for i in range(sheet.ncols):
    print(sheet.col_values(i))#获取第几列的数据



'''
#xlutils:修改excel
book1 = xlrd.open_workbook('wangye.xls')
book2 = copy(book1)#拷贝一份原来的excel
#print(dir(book2))
sheet = book2.get_sheet(0)#获取第几个sheet页，book2现在的是xlutils里的方法，不是xlrd的
sheet.write(1, 3, 0)
sheet.write(1, 0, 'hello')
book2.save('wangye1.xls')
'''


