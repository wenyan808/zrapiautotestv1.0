import json

import requests

from Common.getConsoleLogin import getConsoleLogin_token
from Common.sign import get_sign
from glo import console_HTTP, console_JSON


def get_ConTopicCategoryId():
    url = console_HTTP + "/api/con_topic/v1/add"
    url1 = console_HTTP + "/api/con_topic/v1/list"
    header = console_JSON
    header = header

    headers = {}
    headers.update(header)

    token = {"token": getConsoleLogin_token()}
    headers.update(token)  # 将token更新到headers
    name = "自动化测试专题分类01"

    paylo = {
        "name": name
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

    paylo = {
    }
    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)
    payload = json.dumps(dict(payload1))

    r = requests.session().post(
        url=url1, headers=headers, data=payload
    )

    j_list = r.json()
    return j_list.get("data").get("list")[0].get("id"), headers, j_list


# print(get_ConTopicCategoryId())
