import json

import requests

from Common.getTestLoginToken import gettestLoginToken, getlogintoken
from Common.get_payload_headers import get_headers, get_payload

from Common.sign import get_sign
from Common.tools.get_gmssl import get_sm2

from glo import http, JSON_dev, user_password


def AccountAuth():
    """登录认证

    :return:登录认证的结果r_auth.json(),headers,http
    """
    url = http + "/as_trade/api/account/v1/auth"
    url1 = http + "/as_trade/api/account/v1/info"
    # 拼装参数
    token = {"token": gettestLoginToken()}
    headers = get_headers(JSON_dev, token)
    # print(headers)
    paylo = {}

    payload1 = get_payload(paylo)

    r_info = requests.session().post(
        url=url1, headers=headers, json=payload1
    )

    K = r_info.json()
    # print(K)
    clientId = K.get("data").get("clientId")
    # if yamlconfig("flag"):
    #     password = "123456"
    # else:
    #     password = "111111"

    body = {
        "clientId": clientId,
        "password": get_sm2(user_password)
    }

    payload = get_payload(body)

    # print(payload)
    r_auth = requests.session().post(
        url=url, headers=headers, json=payload
    )

    l = r_auth.json()
    # print(l)
    return l, headers, http


# print(AccountAuth())
# print(list(AccountAuth())[1])


def UserLoginAuth(phone: str, password: str, phoneArea: str, authpwd: str):
    """

    :param phone: login手机号
    :param password: login密码
    :param phoneArea: 手机所属地区
    :param authpwd: 交易密码
    :return: 登录认证的结果r_auth.json(),headers,http
    """
    url = http + "/as_trade/api/account/v1/auth"
    url1 = http + "/as_trade/api/account/v1/info"

    token = {"token": getlogintoken(phone, password, phoneArea)}
    # print(token)
    # headers1 = get_headers(JSON_dev, token)
    headers1 = {}
    headers1.update(JSON_dev)
    headers1.update(token)
    # print(headers1)
    paylo = {}

    payload = get_payload(paylo)

    r_info = requests.session().post(
        url=url1, headers=headers1, json=payload
    )

    K = r_info.json()
    #
    # print(f"\n请求地址：{url1}"
    #       f"\nbody参数：{payload}"
    #       f"\n请求头部参数：{headers1}"
    #       f"\n返回数据结果：{K}")

    clientId = K.get("data").get("clientId")
    password = authpwd

    body = {
        "clientId": clientId,
        "password": get_sm2(password)
    }

    payload1 = get_payload(body)

    r_auth = requests.session().post(
        url=url, headers=headers1, json=payload1
    )

    l = r_auth.json()
    # print(f"\n请求地址：{url}"
    #       f"\nbody参数：{payload1}"
    #       f"\n请求头部参数：{headers1}"
    #       f"\n返回数据结果：{l}")
    return l, headers1, http
