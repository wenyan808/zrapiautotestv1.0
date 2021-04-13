# getdevLoginToken
import json

import pytest
import requests

from Common.tools.md5 import get_md5
from glo import http, phone2, pwd2, JSON_dev, HTTP, JSON2
from Common.sign import get_sign


def gettestLoginToken():
    """TEST环境 用户手机号密码登录

    :return: 返回登录token
    """
    url = http + "/as_user/api/user_account/v1/user_login_pwd"
    url1 = http + "/as_notification/api/sms/v1/send_device_code"
    url2 = http + "/as_user/api/user_account/v1/device_next"
    phoneArea = "86"
    password = get_md5(pwd2)

    json1 = {
        "phone": phone2,
        "password": password,
        "phoneArea": phoneArea
    }
    sign1 = {"sign": get_sign(json1)}
    json1.update(sign1)
    headers = JSON_dev

    response_login = requests.session().post(url=url, headers=headers,
                                             json=json1)

    if response_login.json().get("code") == "010007" \
            or response_login.json().get("msg") == "用户登陆的设备和以前不一样":

        boby = {
            "phone": phone2,
            "countryCode": phoneArea
        }
        sign1 = {"sign": get_sign(boby)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(boby)
        payload1.update(sign1)

        boby = json.dumps(dict(payload1))
        response_getdata = requests.session().post(url=url1, headers=headers,
                                                   data=boby)

        verificationCode = response_getdata.json().get("data")
        data = {
            "phone": phone2,
            "verificationCode": verificationCode,
            "phoneArea": phoneArea
        }

        sign1 = {"sign": get_sign(data)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(data)
        payload1.update(sign1)

        data = json.dumps(dict(payload1))
        response_gettoken = requests.session().post(url=url2, headers=headers,
                                                    data=data)

        res = response_gettoken.json().get("data").get("token")
        return res

    else:
        return response_login.json().get("data").get("token")


# print(getdevLoginToken())


def getUserLogincodeToken(phone: str):
    """TEST环境 获取手机验证登录的token

    :param phone: 手机号
    :return: token
    """
    HTTP = http
    JSON = JSON_dev
    headers = JSON
    # phone = "13418923886"
    phone = phone
    phoneArea = "86"
    boby = {
        "phone": phone,
        "countryCode": phoneArea
    }
    sign1 = {"sign": get_sign(boby)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(boby)
    payload1.update(sign1)

    payload = json.dumps(dict(payload1))
    response_getdata = requests.session().post(
        url=HTTP + "/as_notification/api/sms/v1/send_login_code",
        headers=headers, data=payload
    )
    verificationCode = response_getdata.json().get("data")
    url = HTTP + "/as_user/api/user_account/v1/user_login_code"
    paylo = {
        "verificationCode": verificationCode,
        "phone": phone,
        "phoneArea": "86"
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
    return j.get("data").get("token")


# print(getUserLogincodeToken())


def getlogintoken(phone: str, password: str, phoneArea: str):
    """test 获取登录token

    :param phone:   手机号
    :param password:   未加密的密码
    :param phoneArea:  地区码
    :return:登录token
    """
    url = HTTP + "/as_user/api/user_account/v1/user_login_pwd"
    url1 = HTTP + "/as_notification/api/sms/v1/send_device_code"
    url2 = HTTP + "/as_user/api/user_account/v1/device_next"

    pwd = get_md5(password)

    json1 = {
        "phone": phone,
        "password": pwd,
        "phoneArea": phoneArea
    }
    sign1 = {"sign": get_sign(json1)}
    json1.update(sign1)
    headers = JSON2

    res_login = requests.session().post(url=url, headers=headers,
                                        json=json1)

    if res_login.json().get("code") == "010007" \
            or res_login.json().get("msg") == "用户登陆的设备和以前不一样":

        boby = {
            "phone": phone,
            "countryCode": phoneArea
        }
        sign1 = {"sign": get_sign(boby)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(boby)
        payload1.update(sign1)

        boby = json.dumps(dict(payload1))
        response_getdata = requests.session().post(url=url1, headers=headers,
                                                   data=boby)

        verificationCode = response_getdata.json().get("data")
        data = {
            "phone": phone,
            "verificationCode": verificationCode,
            "phoneArea": phoneArea
        }

        sign1 = {"sign": get_sign(data)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(data)
        payload1.update(sign1)

        data = json.dumps(dict(payload1))
        response_gettoken = requests.session().post(url=url2, headers=headers,
                                                    data=data)

        res = response_gettoken.json().get("data").get("token")
        return res

    else:
        return res_login.json().get("data").get("token")



