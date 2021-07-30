import json

import requests

from Common.getTestLoginToken import gettestLoginToken, getlogintoken

from Common.sign import get_sign
from TestCase.UserRelatedapi.redisfuction import deviceOR
from glo import http, JSON_dev, user_password, JSON2


def AccountAuth():
    """登录认证

    :return:登录认证的结果r_auth.json(),headers,http
    """
    url = http + "/as_trade/api/account/v1/auth"
    url1 = http + "/as_trade/api/account/v1/info"
    # 拼装参数
    headers = JSON_dev
    headers = headers
    headers1 = {}
    token = {"token": gettestLoginToken()}
    # print(token)
    headers1.update(headers)
    headers1.update(token)  # 将token更新到headers
    # print(headers)
    paylo = {}

    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)

    payload2 = json.dumps(dict(payload1))

    r_info = requests.session().post(
        url=url1, headers=headers1, data=payload2
    )

    K = r_info.json()
    # print(K)
    clientId = K.get("data").get("clientId")
    password = user_password

    body = {
        "clientId": clientId,
        "password": password
    }

    sign1 = {"sign": get_sign(body)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(body)
    payload1.update(sign1)

    payload = json.dumps(dict(payload1))
    r_auth = requests.session().post(
        url=url, headers=headers1, data=payload
    )

    l = r_auth.json()
    # print(l)
    return l, headers1, http


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
    headers = JSON_dev
    headers = headers
    headers1 = {}
    token = {"token": getlogintoken(phone, password, phoneArea)}
    # print(token)
    headers1.update(headers)
    headers1.update(token)  # 将token更新到headers
    # print(headers)
    paylo = {}

    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)

    payload2 = json.dumps(dict(payload1))

    r_info = requests.session().post(
        url=url1, headers=headers1, data=payload2
    )

    K = r_info.json()
    clientId = K.get("data").get("clientId")
    password = authpwd

    body = {
        "clientId": clientId,
        "password": password
    }

    sign1 = {"sign": get_sign(body)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(body)
    payload1.update(sign1)

    payload = json.dumps(dict(payload1))

    r_auth = requests.session().post(
        url=url, headers=headers1, data=payload
    )

    l = r_auth.json()
    # print(l)
    return l, headers1, http
