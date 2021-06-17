import json

import requests

from Common.getConsoleLogin import getConsoleLogin_token
from Common.sign import get_sign
from glo import console_HTTP, console_JSON, loginAccount_phone


def first_audit_list():
    """初审列表

    :return:
    """
    url = console_HTTP + "/api/con_open/v1/first_audit_list"
    # 拼装参数
    headers = console_JSON
    headers1 = {}
    token = {"token": getConsoleLogin_token()}
    headers1.update(headers)
    headers1.update(token)  # 将token更新到headers
    # print(headers)
    phone = loginAccount_phone

    paylo = {
        "phone": phone
    }

    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)

    payload = json.dumps(dict(payload1))

    r = requests.session().post(
        url=url, headers=headers1, data=payload
    )

    j = r.json()
    return j, headers1, phone


# print(list(first_audit_list()))


def first_audit_list01(phone: str):
    """初审列表

    :param phone: 手机号
    :param consoleloginAccount: console登录账户
    :param consolepwd: console密码
    :return: 返回初审列表json数据，header,phone
    """
    url = console_HTTP + "/api/con_open/v1/first_audit_list"
    # 拼装参数
    headers = console_JSON
    headers1 = {}
    token = {"token": getConsoleLogin_token()}
    headers1.update(headers)
    headers1.update(token)  # 将token更新到headers
    # print(headers)

    paylo = {
        "phone": phone
    }

    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)

    payload = json.dumps(dict(payload1))

    r = requests.session().post(
        url=url, headers=headers1, data=payload
    )

    j = r.json()
    return j, headers1, phone

# print(list(first_audit_list()))
