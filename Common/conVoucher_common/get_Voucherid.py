import json

import requests

from Common.getConsoleLogin import getConsoleLogin_token
from Common.get_time_stamp import gettoday
from Common.sign import get_sign
from glo import console_HTTP, console_JSON


def getvoucherId(n: int):
    url = console_HTTP + "/api/con_voucher/v1/add"
    url1 = console_HTTP + "/api/con_voucher/v1/list"
    header = console_JSON
    header = header

    headers = {}
    headers.update(header)

    token = {"token": getConsoleLogin_token()}
    headers.update(token)  # 将token更新到headers

    paylo = {
        "voucherName": "高级行情-美股LV1权益" + str(gettoday()),
        "type": 1,
        "description": "高级行情-美股LV1活动卡券",
        "usedType": 1,
        "voucherTotalNum": 1000
    }

    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)
    payload = json.dumps(dict(payload1))

    r_add = requests.session().post(
        url=url, headers=headers, data=payload
    )

    j_add = r_add.json()

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

def delvoucherId(voucherId):
    url1 = console_HTTP + "/api/con_voucher/v1/update"
    header = console_JSON
    header = header

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
