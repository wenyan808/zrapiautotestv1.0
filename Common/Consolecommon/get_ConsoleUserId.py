import json

import requests

from Common.get_time_stamp import TimeToStamp13
from Common.sign import get_sign
from glo import console_HTTP


def get_consoleuserId(header: dict, n: int):
    """获取用户id

    :param header:带token的headers
    :param n:下标
    :return:用户id
    """
    url = console_HTTP + "/api/con_user/v1/list"
    headers = header
    registerStartTime = TimeToStamp13("2021-06-01 16:03:33")
    paylo = {
        "registerStartTime": registerStartTime,
        "pageSize": 20,
        "currentPage": 1
    }
    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)

    payload = json.dumps(dict(payload1))

    r = requests.session().post(
        url=url, headers=headers, data=payload
    )
    j = r.json()
    # print(j)
    return j.get("data").get("list")[n].get("userId")


def get_orderId(header: dict, n: int):
    """获取单据id
    :param header ：带token的请求参数header
    :param n:下标
    :return: 返回单据id
    """
    url = console_HTTP + "/api/con_open/v1/pass_list"
    headers = header

    paylo = {
        "pageSize": 20,
        "currentPage": 1
    }
    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)

    payload = json.dumps(dict(payload1))

    r = requests.session().post(
        url=url, headers=headers, data=payload
    )
    j = r.json()
    # print(j)
    return j.get("data").get("list")[n].get("orderId")
