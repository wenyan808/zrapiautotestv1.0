# getdevLoginToken
import json

import pytest
import requests

from Common.tools.md5 import get_md5
from glo import http, phone2, pwd2, JSON_dev, HTTP, JSON2, phoneArea, countryCode
from Common.sign import get_sign


def gettestLoginToken():
    """TEST环境 用户手机号密码登录

    :return: 返回登录token
    """
    url = http + "/as_user/api/user_account/v1/user_login_pwd"
    url1 = http + "/as_notification/api/sms/v1/send_code"
    url2 = http + "/as_user/api/user_account/v1/device_next"
    password = get_md5(pwd2)

    json1 = {
        "phone": phone2,
        "loginPassword": password,
        "phoneArea": phoneArea
    }
    sign1 = {"sign": get_sign(json1)}
    json1.update(sign1)
    headers = JSON_dev

    response_login = requests.session().post(url=url, headers=headers,
                                             json=json1)

    if response_login.json().get("code") == "010007" \
            or response_login.json().get("msg") == "用户登陆的设备和以前不一样":

        smsCode = "6"  # /*** 登录*/LOGIN("1"),/*** 忘记密码*/FORGET("2"),/*** 更换手机号-旧手机号*/PHONE_OLD("3"),
        # /*** 更换手机号-新手机号*/PHONE_NEW("4"),/*** 修改密码*/UPDATE_PASSWORD("5"),/*** 设备认证*/DEVICE("6"),
        # /*** 绑定第三方登录短信验证*/BIND_DEVICE("7");
        boby = {
            "phone": phone2,
            "countryCode": countryCode,
            "smsCode": smsCode
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


# print(gettestLoginToken())


def getUserLogincodeToken(phone: str):
    """TEST环境 获取手机验证登录的token(可以直接用手机号注册并登录)

    :param phone: 手机号
    :return: token
    """
    HTTP = http
    JSON = JSON_dev
    headers = JSON
    # phone = "13418923886"
    phone = phone
    smsCode = "1"  # /*** 登录*/LOGIN("1"),/*** 忘记密码*/FORGET("2"),/*** 更换手机号-旧手机号*/PHONE_OLD("3"),
    # /*** 更换手机号-新手机号*/PHONE_NEW("4"),/*** 修改密码*/UPDATE_PASSWORD("5"),/*** 设备认证*/DEVICE("6"),
    # /*** 绑定第三方登录短信验证*/BIND_DEVICE("7");
    boby = {
        "phone": phone,
        "countryCode": countryCode,
        "smsCode": smsCode
    }
    sign1 = {"sign": get_sign(boby)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(boby)
    payload1.update(sign1)

    payload = json.dumps(dict(payload1))
    response_getdata = requests.session().post(
        url=HTTP + "/as_notification/api/sms/v1/send_code",
        headers=headers, data=payload
    )
    verificationCode = response_getdata.json().get("data")
    url = HTTP + "/as_user/api/user_account/v1/user_login_code"
    paylo = {
        "verificationCode": verificationCode,
        "phone": phone,
        "phoneArea": phoneArea
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
    if j.get("code") == "010003" \
            or j.get("msg") == "第一次登录，设置登录密码":
        password = "zr123456"
        pwd = get_md5(password)
        businessAccessToken = j.get("data").get("businessAccessToken")
        url = HTTP + "/as_user/api/user_account/v1/set_login_password"
        paylo = {
            "loginPassword": pwd,
            "businessAccessToken": businessAccessToken
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        response = requests.session().post(
            url=url, headers=headers, data=payload
        )
        return response.json().get("data").get("token")

    else:
        return j.get("data").get("token")


# print(getUserLogincodeToken("15816265000"))


def getlogintoken(phone: str, password: str, phoneArea: str):
    """test 获取登录token

    :param phone:   手机号
    :param password:   未加密的密码
    :param phoneArea:  地区码
    :return:登录token
    """
    url = HTTP + "/as_user/api/user_account/v1/user_login_pwd"
    url1 = HTTP + "/as_notification/api/sms/v1/send_code"
    url2 = HTTP + "/as_user/api/user_account/v1/device_next"

    pwd = get_md5(password)
    json1 = {
        "phone": phone,
        "loginPassword": pwd,
        "phoneArea": phoneArea
    }
    sign1 = {"sign": get_sign(json1)}
    json1.update(sign1)
    headers = JSON2

    res_login = requests.session().post(url=url, headers=headers,
                                        json=json1)

    if res_login.json().get("code") == "010007" \
            or res_login.json().get("msg") == "用户登陆的设备和以前不一样":
        smsCode = "6"  # /*** 登录*/LOGIN("1"),/*** 忘记密码*/FORGET("2"),/*** 更换手机号-旧手机号*/PHONE_OLD("3"),
        # /*** 更换手机号-新手机号*/PHONE_NEW("4"),/*** 修改密码*/UPDATE_PASSWORD("5"),/*** 设备认证*/DEVICE("6"),
        # /*** 绑定第三方登录短信验证*/BIND_DEVICE("7");

        boby = {
            "phone": phone,
            "countryCode": countryCode,
            "smsCode": smsCode
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

# print(getlogintoken("15811354200", "zr123456", "86"))
