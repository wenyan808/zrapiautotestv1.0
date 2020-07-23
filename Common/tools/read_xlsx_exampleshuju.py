# 若报错:SyntaxError: Non-UTF-8 code starting with '\xd0' in fil codinggbk=
#  行数 （不包含表头，且一下均如此）
# print(len(df.index.values))
# 行索引 
# print(df.index.values)
#  列数
# print(len(df.columns.values))
#  列索引
# print(df.columns.values)
# #  读取多行数据（这里是第1行和第2行）
# data = df.loc[[1, 2]].values
# print('第1行和第2行数据: \n', data)
from copy import copy

import pandas as pd
from glo import BASE_DIR


def shuju(sheet):
    df = pd.read_excel(BASE_DIR + r'/TestData/example.xlsx', sheet_name=sheet, encoding="utf-8")
    # df = pd.read_excel(r'TestData/example.xlsx', sheet_name=sheet)     #直接copy   example.xlsx的相对路径
    data = df.values
    # print(data)
    return data




# for i in data:
# 	if "登录"  in i:
# 		# return i[5],i[6],i[7],i[8],i[9]
# 	#
# 			print("url:",i[5])
# 	# 		print('请求方式:',i[6])
#
#
# 			print('请求canshu:',eval(i[7])['phone'])
# 	# 		print('有无token:',i[3])
#
# shuju()
