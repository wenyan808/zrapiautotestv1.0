import datetime
import time


def get_float_time_stamp():
    datetime_now = datetime.datetime.now()
    return datetime_now.timestamp()


def get_time_stamp16():
    """

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
    """

    :return: 返回当前时间戳（13位）
    """
    # 生成13时间戳   eg:1597195825782
    datetime_now = datetime.datetime.now()

    # 10位，时间点相当于从UNIX TIME的纪元时间开始的当年时间编号
    date_stamp = str(int(time.mktime(datetime_now.timetuple())))

    # 3位，微秒
    data_microsecond = str("%06d" % datetime_now.microsecond)[0:3]

    date_stamp = date_stamp + data_microsecond
    return int(date_stamp)


def stampToTime(stamp):
    """时间戳转换为当前时间格式
    如：2020-08-12 09:36:40.604
    :param stamp: 时间戳值
    :return:
    """
    datatime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(str(stamp)[0:10])))
    datatime = datatime + '.' + str(stamp)[10:]
    return datatime

# if __name__ == '__main__':
#     a1 = get_time_stamp16()
#     print(a1)
#     # print(stampToTime(a1))
#     a2 = get_time_stamp13()
#     print(a2)
#     print(stampToTime(a2))

