# 操作数据库
from os.path import join

from pymysql import *
from Common.tools.write_xlsx import write_xlsx
from glo import phone


def showsql(host, user, password, database, sql):
    """

    :param host: ip地址
    :param user: mysql用户名
    :param password: mysql密码
    :param database: 数据表名
    :param sql: 查询语句
    :return: 查询的数据
    """
    conn = connect(
        host=host,
        port=3306, user=user,
        password=password,
        database=database,
        charset='utf8')

    # 创建游标
    c = conn.cursor()
    # 执行sql语句
    c.execute(sql)
    # 查询一行数据
    result = c.fetchall()
    # 关闭游标
    c.close()
    # 关闭数据库连接
    conn.close()
    return result




# 使用pymongo模块连接mongoDB数据库
# coding=utf-8
from pymongo import MongoClient


def MongoDB(address, port, database, surface, key, price):
    """查询指定条件的所有字段

    :param address:ip地址
    :param port: 端口号
    :param database: 数据名
    :param surface: 表名
    :param key: 键
    :param price:值
    :return:返回查询的MongoDB数据库里面的符合条件的所有数据
    """
    # 建立MongoDB数据库连接
    client = MongoClient(address, port)

    # 连接所需数据库,database为数据库名
    db = client[database]

    # 连接所用集合，也就是我们通常所说的表，surface为表名
    collection = db[surface]

    # 接下里就可以用collection来完成对数据库表的一些操作

    # 查找集合中所有数据
    # for item in collection.find():
    #     print(item)

    # 查找集合中单条数据
    mydoc = collection.find({key: price})
    list1 = list()
    for x in mydoc:
        # print(x)
        list1.append(x)
    return list1


def MongoDBField(address, port, database, surface, args):
    """查询指定条件的多个字段

    :param address: ip地址
    :param port: 端口号
    :param database: 数据名
    :param surface: 表名
    :param args: 传递类型为list，传递参数用于指定查询字段   type：为0，不显示type     为1，显示type
    :return:返回查询的MongoDB数据库里面的符合条件的所有数据列表
    """

    a, b = args
    # 建立MongoDB数据库连接
    client = MongoClient(address, port)

    # 连接所需数据库,database为数据库名
    db = client[database]

    # 连接所用集合，也就是我们通常所说的表，surface为表名
    collection = db[surface]

    # 接下里就可以用collection来完成对数据库表的一些操作

    # 查找集合中所有数据
    # for item in collection.find():
    #     print(item)

    # 查找集合中单条数据
    mydoc = collection.find(a, b)
    list1 = list()
    for x in mydoc:
        # print(x)
        list1.append(x)
    return list1


# print(MongoDBField("192.168.1.237", 27017, "community", "t_report", [{}, {"type": 1}]))
# ts_code = showsql('192.168.1.237','root','123456','stock_market',
#                    "select ts,code from t_stock_search;")
# ts_code = showsql(
#             "192.168.1.237", "root", "123456", "stock_market",
#             "select ts,code,type from t_stock_search;"
#         )
# print(ts_code)
# a = showsql(
#             '192.168.1.237', 'root', '123456', "user_account",
#             "select user_id from t_user_account where `zr_no`= '68904140';"
#         )
# print((list(list(a)[0])[0]))
# id = MongoDB("192.168.1.236", 27017, "stock_market", "t_stock_selected", "userId", '90106be7c8444dda8f0f5b745b50a08e')
# print(id)