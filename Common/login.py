import json

import pytest
import requests

from Common.tools.md5 import get_md5
from glo import HTTP, BASE_DIR, JSON, phone, pwd
from Common.sign import get_sign


def login():
    # print(phone)
    password = get_md5(pwd)
    http = HTTP
    json1 = {
        "phone": phone,
        "password": password,
        "phoneArea": "86"
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
                                         json=boby)
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
                                         json=data)
        res=response_gettoken.json().get("data").get("token")
        with open(BASE_DIR + r'/TestData/token.yaml', 'w') as file:
            file.write("token: " + res)



    else:
        # pass
        res = response_login.json().get("data").get("token")
        with open(BASE_DIR + r'/TestData/token.yaml', 'w') as file:
            file.write("token: " + res)
    # print(res)
#     print(response_login.json())
#
# login()
