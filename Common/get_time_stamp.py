import datetime
import time


def get_float_time_stamp():
    datetime_now = datetime.datetime.now()  # 获取系统当前时间
    return datetime_now.timestamp()


def get_time_stamp16():
    """获取当前时间转换成16位的时间戳

    :return: 返回当前时间戳（16位）
    """
    # 生成16时间戳   eg:1597195825782642
    datetime_now = datetime.datetime.now()
    print(datetime_now)

    # 10位，时间点相当于从UNIX TIME的纪元时间开始的当年时间编号
    date_stamp = str(int(time.mktime(datetime_now.timetuple())))

    # 6位，微秒
    data_microsecond = str("%06d" % datetime_now.microsecond)

    date_stamp = date_stamp + data_microsecond
    return int(date_stamp)


def get_time_stamp13():
    """获取当前时间并转换成13位的时间戳

    :return: 返回当前时间戳（13位）
    """
    # 生成13时间戳   eg:1597195825782
    datetime_now = datetime.datetime.now()

    # 10位，时间点相当于从UNIX TIME的纪元时间开始的当年时间编号
    date_stamp = str(int(time.mktime(datetime_now.timetuple())))

    # 3位，微秒
    data_microsecond = str("%03d" % datetime_now.microsecond)[0:3]

    date_stamp = date_stamp + data_microsecond
    return int(date_stamp)


def stampToTime(stamp):
    """时间戳转换为当前时间格式
    如：2020-08-12 09:36:40.604
    :param stamp: 时间戳值
    :return:
    """
    datatime = time.strftime("%Y-%m-%d %H:%M:%S",
                             time.localtime(float(str(stamp)[0:10]))
                             )  # 将指定时间戳转换为其他日期格式（如%Y-%m-%d %H:%M:%S）
    datatime = datatime + '.' + str(stamp)[10:]
    return datatime


def TimeTostamp():
    """获取三天前的时间格式转换为13位时间戳
    如：2020-08-12 09:36:40.604
    :return:时间戳值
    """
    # 先获得时间数组格式的日期
    threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days=3))
    # 10位，时间点相当于从UNIX TIME的纪元时间开始的当年时间编号
    date_stamp = str(int(time.mktime(threeDayAgo.timetuple())))
    # 3位，微秒
    data_microsecond = str("%03d" % threeDayAgo.microsecond)[0:3]
    date_stamp3 = date_stamp + data_microsecond
    return int(date_stamp3)

# if __name__ == '__main__':
#     a1 = get_time_stamp16()
#     print(a1)
#     # print(stampToTime(a1))
#     a2 = get_time_stamp13()
#     print(a2)
#     print(stampToTime(a2))
