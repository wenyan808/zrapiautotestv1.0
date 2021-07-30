import json

import pytest
import requests

from Common.tools.md5 import get_md5
from glo import HTTP, BASE_DIR, JSON, phone, pwd, phone2, phoneArea, pwd2
from Common.sign import get_sign


def login():
    # print(phone)
    password = get_md5(pwd2)
    http = HTTP
    json1 = {
        "phone": phone2,
        "loginPassword": password,
        "phoneArea": phoneArea
    }
    sign1 = {"sign": get_sign(json1)}
    json1.update(sign1)
    headers = JSON
    session = requests.session()
    response_login = session.post(http + "/as_user/api/user_account/v1/user_login_pwd", headers=headers,
                                  json=json1)
    if response_login.json().get("code") == "010007" \
            or response_login.json().get("msg") == "用户登陆的设备和以前不一样":
        # pass
        boby = {
            "phone": phone,
            "countryCode": "86"
        }
        sign1 = {"sign": get_sign(boby)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(boby)
        payload1.update(sign1)

        boby = json.dumps(dict(payload1))
        response_getdata = requests.post(http + "/as_notification/api/sms/v1/send_device_code", headers=headers,
                                         data=boby)
        verificationCode = response_getdata.json().get("data")
        data = {
            "phone": phone,
            "verificationCode": verificationCode,
            "phoneArea": "86"
        }

        sign1 = {"sign": get_sign(data)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(data)
        payload1.update(sign1)

        data = json.dumps(dict(payload1))
        response_gettoken = requests.post(http + "/as_user/api/user_account/v1/device_next", headers=headers,
                                          data=data)
        res = response_gettoken.json().get("data").get("token")
        with open(BASE_DIR + r'/TestData/token.yaml', 'w') as file:
            file.write("token: " + res)
        # return res




    else:
        # pass
        res = response_login.json().get("data").get("token")
        with open(BASE_DIR + r'/TestData/token.yaml', 'w') as file:
            file.write("token: " + res)
        # return res


# print(login())


def login_all(key, value, password, url, file_name):
    """

    :param key: 键
    :param value: 值
    :param password: 未加密的密码
    :param url: url链接
    :param file_name:  写入文件名字
    :return:
    """
    # header = {
    #     "Content-Type": "application/json",
    #     "appVersion": '0.2.0(00004)',
    #     "deviceId": "8556915E-DBE1-4476-91DB-CA0119517998",
    #     "osType": "ios",
    #     "osVersion": '13.5.1'
    # }
    header = JSON
    json = {
        "loginPassword": get_md5(password),
        "phoneArea": "86"
    }
    loginAccount = {key: value}
    json.update(loginAccount)
    sign1 = {"sign": get_sign(json)}
    json.update(sign1)
    session = requests.session()
    response_login = session.post(url, headers=header,
                                  json=json)
    # print(response_login.json())
    res = response_login.json().get("data").get("token")
    with open(BASE_DIR + "/" + file_name + ".yaml", 'w') as file:
        file.write("token: " + res)
    return response_login.json()

# login("loginAccount", "test@123.com", "abcd1234567", "http://192.168.1.239:8080/apisC/api/sys_user/v1/login",
# # "token_console")
# login_all("phone", "18379204795", "102522ql", "http://192.168.1.241/as_user/api/user_account/v1/user_login_pwd", "token")
