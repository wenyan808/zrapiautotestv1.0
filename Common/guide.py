from Common.bacis import common
from Common.tools.read_xlsx_exampleshuju import shuju


def zhuorui(sheet, name,info=""):
    for i in shuju(sheet):
        if name in i:
            if info == "" :
                return common(i)
            else:
                return common(i, info)

# zhuorui('自选股', '自选股股票列表_SH')
# # zhuorui('自选股', '置顶自选股无token')
# zhuorui('自选股', '置顶自选股无token')
