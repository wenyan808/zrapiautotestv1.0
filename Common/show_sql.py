# 操作数据库
import pymysql

from Common.tools.write_xlsx import write_xlsx


class OperationSql:
    _conn = None
    _cursor = None

    # 获取连接数据库
    @classmethod
    def get_connect_sql(cls):
        if cls._conn is None:
            cls._conn = pymysql.connect("192.168.1.237", "root", "123456", "user_account")
        return cls._conn

    # 获取创建游标
    @classmethod
    def get_newCursor(cls):
        if cls._cursor is None:
            cls._cursor = cls.get_connect_sql().cursor()
        return cls._cursor

    # 关闭数据库连接
    @classmethod
    def close_sql_connect(cls):
        if cls._conn is not None:
            cls.get_connect_sql().close()
            cls._conn = None

    # 关闭游标
    @classmethod
    def close_cursor(cls):
        if cls._cursor is not None:
            cls.get_newCursor().close()
            cls._cursor = None

    # 操作数据库
    @classmethod
    def show_sql(cls, sql):
        try:
            # 创建游标
            cursor = cls.get_newCursor()
            cursor.execute(sql)
            data = cursor.fetchone()
        except Exception as e:
            raise e
        finally:
            cls.close_cursor()
            cls.close_sql_connect()
        return data


# q = OperationSql()
# print(q.show_sql("select * from m_china_concept where `symbol`= 'BABA';"))

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



