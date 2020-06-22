import datetime
import threading

now = datetime.datetime.now().strftime("%m%d%H%M")

count_username = 0
lock_username = threading.Lock()


def get_unique_username(n: int, prefix="t") -> list:
    """获取不重复用户名

    :param n: 数量
    :param prefix: 前缀
    :return: 列表
    """
    lock_username.acquire()
    global count_username
    L = []

    for i in range(n):
        L.append(f"{prefix}{now}{count_username}")
        count_username += 1
    lock_username.release()
    return L


count_phone = 0
lock_phone = threading.Lock()


def get_unique_phone(prefix="133"):
    """获取不重复手机号码

    :param prefix: 前缀
    :return: 手机号码
    """
    lock_phone.acquire()
    global count_phone
    phone = f"{prefix}{now[2:]}{count_phone:02}"
    count_phone += 1
    lock_phone.release()
    return phone
