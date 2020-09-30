from Common.bacis import common
from Common.tools.read_xlsx_exampleshuju import shuju


def zhuorui(sheet, name):
    for i in shuju(sheet):
        if name in i:
            # common(i)
            return common(i)
# zhuorui("市场行情",'查询股票市场涨跌概况_参数为4')
# zhuorui('拆合股', '查询更多股票信息')
# zhuorui('交易', '行情汇率列表')
