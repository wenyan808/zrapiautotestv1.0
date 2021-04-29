import json

import requests

from Common.getConsoleLogin import getConsoleLogin_token
from Common.sign import get_sign
from glo import console_HTTP, console_JSON


def delete_ConTopicID(ID: int):
    url = console_HTTP + "/api/con_topic/v1/delete"

    header = console_JSON
    header = header

    headers = {}
    headers.update(header)

    token = {"token": getConsoleLogin_token()}
    headers.update(token)  # 将token更新到headers

    paylo = {
        "id": ID
    }
    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)
    payload = json.dumps(dict(payload1))

    r_delete = requests.session().post(
        url=url, headers=headers, data=payload
    )

    j_delete = r_delete.json()
    return j_delete


# print(delete_ConTopicID())


def delete_ConTopiccategory(categoryId: int):
    url = console_HTTP + "/api/con_topic/v1/delete"

    header = console_JSON
    header = header

    headers = {}
    headers.update(header)

    token = {"token": getConsoleLogin_token()}
    headers.update(token)  # 将token更新到headers

    paylo = {
        "categoryId": categoryId
    }
    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)
    payload = json.dumps(dict(payload1))

    r_delete = requests.session().post(
        url=url, headers=headers, data=payload
    )

    j_delete = r_delete.json()
    return j_delete

# print(delete_ConTopiccategory())
