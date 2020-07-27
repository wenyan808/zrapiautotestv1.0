from pandas.tests.io.excel.test_xlrd import xlrd
from xlutils.copy import copy
from glo import BASE_DIR


def write_xlsx(sheet, row, rank, data):
    rb = xlrd.open_workbook(BASE_DIR + r'\TestData\example.xlsx')  # 打开weng.xls文件
    wb = copy(rb)  # 利用xlutils.copy下的copy函数复制
    ws = wb.get_sheet(sheet)  # 获取表单
    ws.write(row, rank, data)  # 改变（0,0）的值
    wb.save(BASE_DIR + r'\TestData\example.xlsx')