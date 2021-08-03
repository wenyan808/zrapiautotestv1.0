"""

 :@author 修改人 chenjialuo 2021/8/3 优化密码错误多次，优化return返回的模块化

 """
import json
import requests
from Common.redisfuction import phoneORpwd
from Common.tools.md5 import get_md5
from glo import HTTP, BASE_DIR, JSON, phone, pwd, phone2, phoneArea, pwd2
from Common.sign import get_sign


def login():
    # 手机的请求报文
    json1 = {
        "phone": phone,
        "loginPassword": get_md5(pwd),
        "phoneArea": phoneArea
    }
    sign1 = {"sign": get_sign(json1)}
    json1.update(sign1)
    headers = {}
    headers.update(JSON)
    # 发送post请求
    response_login = requests.post(HTTP + "/as_user/api/user_account/v1/user_login_pwd", headers=headers,json=json1)

    # 当用户登陆的设备和以前不一样,进行验证
    if response_login.json().get("code") == "010007" \
            or response_login.json().get("msg") == "用户登陆的设备和以前不一样":
        # 用户登陆的设备和以前不一样，验证的请求报文
        boby = {
            "phone": phone2,
            "countryCode": "86"
        }
        sign1 = {"sign": get_sign(boby)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(boby)
        payload1.update(sign1)
        boby = json.dumps(dict(payload1))
        # 发送post请求
        response_getdata = requests.post(HTTP + "/as_notification/api/sms/v1/send_device_code", headers=headers, data=boby)
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
        # 发送post请求
        response_gettoken = requests.post(HTTP + "/as_user/api/user_account/v1/device_next", headers=headers, data=data)
        #  return的公用方法
        returnFunction(response_gettoken)

    # 当账户或密码错误次数较多的时候，链接redis池，修改账户密码错误的次数
    elif response_login.json().get("code") == "010005"\
            or response_login.json().get("msg") == "账户或密码错误次数较多，请明日再试":

        # 当账户或者密码次数较多的时候，修改账户密码错误次数
        phoneORpwd(phone)
        # 发送post请求
        response_login = requests.post(HTTP + "/as_user/api/user_account/v1/user_login_pwd", headers=headers, json=json1)
        #  return的公用方法
        returnFunction(response_login)

    else:
        #  return的公用方法
        returnFunction(response_login)

# return的方法
def returnFunction(response_login):
    """

    :param response_login: 代表发送请求的值

    """
    res = response_login.json().get("data").get("token")
    print(res)
    with open(BASE_DIR + r'/TestData/token.yaml', 'w') as file:
        file.write("token: " + res)
    return response_login.json().get("data").get("userId")



login()

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
    header = {}
    header.update(JSON)
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
    return response_login.json().get("data").get("userId")

# login("loginAccount", "test@123.com", "abcd1234567", "http://192.168.1.239:8080/apisC/api/sys_user/v1/login",
# "token_console")
# print(login_all("phone", "18379204795", "102522ql",
#                 "http://192.168.1.241/as_user/api/user_account/v1/user_login_pwd", "token"))
