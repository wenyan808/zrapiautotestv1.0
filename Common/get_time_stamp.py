import datetime
import time


def get_float_time_stamp():
    datetime_now = datetime.datetime.now()  # 获取系统当前时间
    return datetime_now.timestamp()


print(int(get_float_time_stamp()))

def get_time_stamp16():
    """获取当前时间转换成16位的时间戳

    :return: 返回当前时间戳（16位）
    """
    # 生成16时间戳   eg:1597195825782642
    datetime_now = datetime.datetime.now()
    # print(datetime_now)

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


def TimeTostamp30():
    """获取一个月前的时间格式转换为13位时间戳
    如：2020-08-12 09:36:40.604
    :return:时间戳值
    """
    # 先获得时间数组格式的日期
    OneMonthAgo = (datetime.datetime.now() - datetime.timedelta(days=30))
    # 10位，时间点相当于从UNIX TIME的纪元时间开始的当年时间编号
    date_stamp = str(int(time.mktime(OneMonthAgo.timetuple())))
    # 3位，微秒
    data_microsecond = str("%30d" % OneMonthAgo.microsecond)[0:3]
    date_stamp30 = date_stamp + data_microsecond
    return int(date_stamp30 * 1000)


def TimeToStamp(year: int, month: int, day: int, time1: str):
    """将指定时间格式转换为时间戳(法一)

    :param year:年 %Y
    :param month:月 %m
    :param day:日 %d
    :param time1:时分秒  %H:%M:%S
    :return:指定时间戳
    """
    # today = datetime.date.today()  # 拿到当前年月日
    today = datetime.date(year, month, day)
    while 1:  # 不指定次数循环
        new_today = str(today).split('-')  # 按-切片放入列表
        week = datetime.datetime.strptime(''.join(new_today), "%Y%m%d").weekday()  # 转换成20201212格式
        if week == 1 or week == 3:  # 判断是不是为指定星期X
            # time1 = time.strftime('%H:%M:%S')  # 拿到当前时分秒
            time_stamp = time.strptime(f'{today} {time1}', '%Y-%m-%d %H:%M:%S')  # 年月日时分秒格式化元组
            return int(str(int(time.mktime(time_stamp))) + str(time.time()).split('.')[-1][
                                                           :3])  # 年月日时分秒转换为10位时间戳再加上10位时间戳小数点后三位，等于13位
        today += datetime.timedelta(days=1)  # 年月日加1天


def TimeToStamp13(TimeStamp: str, format_string="%Y-%m-%d %H:%M:%S"):
    """(法二)
    将时间字符串转换为13位时间戳，时间字符串默认为2017-10-01 13:37:04格式
    :param TimeStamp: 时间字符串
    :param format_string: 时间字符串格式 默认为%Y-%m-%d %H:%M:%S
    :return: 13位时间戳
    """
    time_array = time.strptime(TimeStamp, format_string)
    time_stamp = int(time.mktime(time_array))
    return int(time_stamp * 1000)


def timeTostamp13(data: str, format_string='%Y-%m-%d %H:%M:%S.%f'):
    """将时间字符串转换为13位时间戳，时间字符串默认为 2021-05-08 17:03:12.59格式

    :param data:时间字符串
    :param format_string:时间字符串(毫秒)默认为 2021-05-08 17:03:12.59格式
    :return:13位时间戳
    """
    time_array = datetime.datetime.strptime(data, format_string)
    time_stamp = int(datetime.datetime.timestamp(time_array) * 1000)
    return time_stamp


def timetostamp13(data: str, format_string='%Y-%m-%d'):
    """将时间字符串转换为13位时间戳，时间字符串默认为 2021-05-08格式

    :param data:时间字符串
    :param format_string:时间字符串(毫秒)默认为 2021-05-08格式
    :return:13位时间戳
    """
    time_array = datetime.datetime.strptime(data, format_string)
    time_stamp = int(datetime.datetime.timestamp(time_array) * 1000)
    return time_stamp

def getTimeTostamp(day:int):
    """获取指定时间的时间格式转换为13位时间戳
    :param day
    :return:时间戳值
    """
    # 先获得时间数组格式的日期
    OneMonthAgo = (datetime.datetime.now() + datetime.timedelta(days=day))
    # 10位，时间点相当于从UNIX TIME的纪元时间开始的当年时间编号
    date_stamp = str(int(time.mktime(OneMonthAgo.timetuple())))
    # 3位，微秒
    data_microsecond = str("%d" % OneMonthAgo.microsecond)[0:3]
    date_stampday = date_stamp + data_microsecond
    return int(date_stampday)
# print(getTimeTostamp(30))

def gettoday():
    today = datetime.date.today()
    return today

# if __name__ == '__main__':
#     a1 = get_time_stamp16()
#     print(a1)
#     # print(stampToTime(a1))
#     a2 = get_time_stamp13()
#     print(a2)
#     print(stampToTime(a2))
