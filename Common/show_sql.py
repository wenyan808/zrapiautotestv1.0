# 操作数据库
import pymysql

from Common.tools.write_xlsx import write_xlsx


class OperationSql:
    _conn = None
    _cursor = None

    def __init__(self, address, user, password, database):
        """

        :param address: IP地址
        :param user: 用户名
        :param password: 密码
        :param database: 数据库名
        """
        self.address = address
        self.user = user
        self.password = password
        self.database = database

    # 获取连接数据库
    def get_connect_sql(self):
        if self._conn is None:
            self._conn = pymysql.connect(self.address, self.user, self.password, self.database)
        return self._conn

    # 获取创建游标
    def get_newCursor(self):
        if self._cursor is None:
            self._cursor = self.get_connect_sql().cursor()
        return self._cursor

    # 关闭数据库连接
    def close_sql_connect(self):
        if self._conn is not None:
            self.get_connect_sql().close()
            self._conn = None

    # 关闭游标
    def close_cursor(self):
        if self._cursor is not None:
            self.get_newCursor().close()
            self._cursor = None

    # 操作数据库
    def show_sql(self, sql):
        try:
            # 创建游标
            cursor = self.get_newCursor()
            cursor.execute(sql)
            data = cursor.fetchall()
        except Exception as e:
            raise e
        finally:
            self.close_cursor()
            self.close_sql_connect()
        # print(data)
        return data


# q = OperationSql()
# print(q.show_sql("select * from m_china_concept where `symbol`= 'BABA';"))
# import json
# q = OperationSql("192.168.1.237", "root", "123456", "stock_market")
# ts_code = q.show_sql("select ts,code from t_stock_search where ts='SH' or ts='SZ';")
# ts_code_shuju = json.dumps(list(map(lambda code: {"ts": code[0], "code": code[1]}, ts_code)))
# # write_json(r"TestData/hsgtis_lgt.json", ts_code_shuju)
# with open(r"TestData\hsgtis_lgt.json", "w", encoding="utf-8") as f:
#     json.dump(ts_code_shuju, f, indent=2, ensure_ascii=False)


# 使用pymongo模块连接mongoDB数据库
# coding=utf-8
from pymongo import MongoClient


def MongoDB(address, port, database, surface, key, price):
    """

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
