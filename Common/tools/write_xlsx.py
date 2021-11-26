from pandas.tests.io.excel.test_xlrd import xlrd
from xlutils.copy import copy
from glo import BASE_DIR


def write_xlsx(sheet, row, rank, data):
    """写入xlsx

    :param sheet: 获取表单sheet名称
    :param row: 列
    :param rank: 行
    :param data: 写入的data数据
    :return:
    """
    rb = xlrd.open_workbook(BASE_DIR + r'/TestData/example.xlsx')  # 打开weng.xls文件
    wb = copy(rb)  # 利用xlutils.copy下的copy函数复制
    ws = wb.get_sheet(sheet)  # 获取表单
    ws.write(row, rank, data)  # 改变（0,0）的值
    wb.save(BASE_DIR + r'/TestData/example.xlsx')
