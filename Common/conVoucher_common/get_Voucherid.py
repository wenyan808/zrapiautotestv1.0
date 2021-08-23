import json

import requests

from Common.getConsoleLogin import getConsoleLogin_token

from Common.sign import get_sign
from glo import console_HTTP, console_JSON


def getvoucherId(headers: dict, n: int):
    """
    获取卡券ID
    :param headers:带token的请求头参数
    :param n:下标
    :return:返回列表中的某个卡券ID（根据下标决定的）
    """
    url1 = console_HTTP + "/api/con_voucher/v1/list"

    paylo = {}
    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)
    payload = json.dumps(dict(payload1))

    r = requests.session().post(
        url=url1, headers=headers, data=payload
    )

    j_list = r.json()
    return j_list.get("data").get("list")[n].get("voucherId")
    # print(j_list)


# print(getvoucherId())

def delvoucherId(voucherId: str):
    """
    删除卡券ID
    :param voucherId: 卡券ID
    :return:
    """
    url1 = console_HTTP + "/api/con_voucher/v1/update"
    header = console_JSON


    headers = {}
    headers.update(header)

    token = {"token": getConsoleLogin_token()}
    headers.update(token)  # 将token更新到headers
    paylo = {
        "voucherId": voucherId,
        "stop": True
    }
    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)
    payload = json.dumps(dict(payload1))

    r = requests.session().post(
        url=url1, headers=headers, data=payload
    )

    j_stop = r.json()
    return j_stop
