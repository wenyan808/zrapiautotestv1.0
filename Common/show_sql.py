# 操作数据库
import pymysql

from Common.tools.write_xlsx import write_xlsx


class OperationSql:
    _conn = None
    _cursor = None

    def __init__(self, address, user, password, database):
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
            data = cursor.fetchone()
        except Exception as e:
            raise e
        finally:
            self.close_cursor()
            self.close_sql_connect()
        return data


# q = OperationSql("192.168.1.237", "root", "123456", "user_account")
# print(q.show_sql("select * from t_user_account where `zr_no`= '10000071';"))

# 使用pymongo模块连接mongoDB数据库
# coding=utf-8
from pymongo import MongoClient


def MongoDB(key, price):
    # 建立MongoDB数据库连接
    client = MongoClient('192.168.1.236', 27017)

    # 连接所需数据库,stock_market为数据库名
    db = client.stock_market

    # 连接所用集合，也就是我们通常所说的表，t_stock_selected为表名
    collection = db.t_stock_selected

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



