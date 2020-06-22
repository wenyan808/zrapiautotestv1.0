from Common.bacis import common
from Common.tools.read_xlsx_exampleshuju import shuju


def zhuorui(sheet, name):
    for i in shuju(sheet):
        if name in i:
            # common(i)
            return common(i)
# zhuorui('查询股票市场涨跌概况_参数为4')
