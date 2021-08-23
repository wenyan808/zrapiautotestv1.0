import json

import requests

from Common.sign import get_sign
from Common.tools.md5 import get_md5
from Common.tools.unique_text import get_unique_phone
from glo import JSON1, countryCode, pwd1, phoneArea, HTTP, BASE_DIR


def get_registerno():
    url0 = HTTP + "/as_notification/api/sms/v1/send_code"
    url = HTTP + "/as_user/api/user_account/v1/user_login_code"
    url1 = HTTP + "/as_user/api/user_account/v1/set_login_password"
    headers = JSON1
    phone = get_unique_phone()
    # print(phone)
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

    json0 = json.dumps(dict(payload1))
    response_getdata = requests.session().post(url=url0, headers=headers,
                                               data=json0)
    # print(response_getdata.json())
    if response_getdata.json().get("code") == "000000":
        verificationCode = response_getdata.json().get("data")
        # url = HTTP + "/as_user/api/user_account/v1/user_login_code"
        # password = "zr123456"
        paylo1 = {
            # "loginPassword": get_md5(f"{password}"),
            "verificationCode": verificationCode,
            "phone": phone,
            "phoneArea": phoneArea
        }

        sign1 = {"sign": get_sign(paylo1)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo1)
        payload1.update(sign1)

        json2 = json.dumps(dict(payload1))

        r = requests.session().post(url=url, headers=headers,
                                    data=json2)

        j = r.json()
        # print(j)
        if j.get("code") == "010003" \
                or j.get("msg") == "第一次登录，设置登录密码":
            password = pwd1
            pwd = get_md5(password)
            businessAccessToken = j.get("data").get("businessAccessToken")

            paylo = {
                "loginPassword": pwd,
                "businessAccessToken": businessAccessToken
            }
            sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
            payload1 = {}
            payload1.update(paylo)
            payload1.update(sign1)

            json3 = json.dumps(dict(payload1))
            r1 = requests.session().post(url=url1, headers=headers,
                                         data=json3)
            j1 = r1.json()
            # print(j1)
            # with open(BASE_DIR + r"/TestData/UserRelatedapiData/正常的手机号与密码.txt", "a", encoding="utf-8") as f:
            #     f.write(f"{j1.get('data').get('phone')}|{password}\n")
            return j1.get('data').get('phone'), password, headers

# print(get_registerno())
