import json

import requests

from Common.getTestLoginToken import gettestLoginToken, getlogintoken
from Common.get_payload_headers import get_headers, get_payload

from Common.sign import get_sign
from Common.tools.read_write_yaml import yamlconfig
# from TestCase.UserRelatedapi.redisfuction import deviceOR
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
        "password": user_password
    }

    payload = get_payload(body)
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
    # 拼装参数
    token = {"token": getlogintoken(phone, password, phoneArea)}
    headers1 = get_headers(JSON_dev, token)
    # print(headers)
    paylo = {}

    payload = get_payload(paylo)

    r_info = requests.session().post(
        url=url1, headers=headers1, data=payload
    )

    K = r_info.json()
    clientId = K.get("data").get("clientId")
    password = authpwd

    body = {
        "clientId": clientId,
        "password": password
    }

    payload = get_payload(body)

    r_auth = requests.session().post(
        url=url, headers=headers1, data=payload
    )

    l = r_auth.json()
    # print(l)
    return l, headers1, http
