# getdevLoginToken
import json

import pytest
import requests

from Business.Urlpath.UrlPath_userlogin import UrlPath_user_login_pwd, UrlPath_send_code, UrlPath_device_next, \
    UrlPath_user_login_code, UrlPath_set_login_password
from Common.send_code import send_code
from Common.tools.md5 import get_md5
from glo import http, phone2, pwd2, JSON_dev, HTTP, JSON2, phoneArea, countryCode, BASE_DIR
from Common.sign import get_sign


def gettestLoginToken():
    """TEST环境 用户手机号密码登录
    :return: 返回登录token
    """
    url = http + UrlPath_user_login_pwd
    url_send_code = http + UrlPath_send_code
    url_device_next = http + UrlPath_device_next
    password = get_md5(pwd2)
    json1 = {
        "phone": phone2,
        "loginPassword": password,
        "phoneArea": phoneArea
    }
    sign1 = {"sign": get_sign(json1)}
    json1.update(sign1)
    headers = {}
    headers.update(JSON_dev)
    response_login = requests.session().post(url=url, headers=headers,
                                             json=json1)
    # print(response_login.json())
    if response_login.json().get("code") == "010007" \
            or response_login.json().get("msg") == "用户登陆的设备和以前不一样":

        smsCode = "6"  # /*** 登录*/LOGIN("1"),/*** 忘记密码*/FORGET("2"),/*** 更换手机号-旧手机号*/PHONE_OLD("3"),
        # /*** 更换手机号-新手机号*/PHONE_NEW("4"),/*** 修改密码*/UPDATE_PASSWORD("5"),/*** 设备认证*/DEVICE("6"),
        # /*** 绑定第三方登录短信验证*/BIND_DEVICE("7");

        """发送短信"""
        response_getdata = send_code(url_send_code, headers, phone2, smsCode)

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
        response_gettoken = requests.session().post(url=url_device_next, headers=headers,
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
    url = HTTP + UrlPath_user_login_code
    # JSON = JSON_dev
    headers = {}
    headers.update(JSON_dev)
    # phone = "13418923886"
    phone = phone
    smsCode = "1"  # /*** 登录*/LOGIN("1"),/*** 忘记密码*/FORGET("2"),/*** 更换手机号-旧手机号*/PHONE_OLD("3"),
    # /*** 更换手机号-新手机号*/PHONE_NEW("4"),/*** 修改密码*/UPDATE_PASSWORD("5"),/*** 设备认证*/DEVICE("6"),
    # /*** 绑定第三方登录短信验证*/BIND_DEVICE("7");

    """发送短信"""
    response_getdata = send_code(HTTP + UrlPath_send_code, headers, phone, smsCode)

    verificationCode = response_getdata.json().get("data")

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
        url_setloginpassword = HTTP + UrlPath_set_login_password
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
            url=url_setloginpassword, headers=headers, data=payload
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
    """接口地址"""
    url = http + UrlPath_user_login_pwd
    url_send_code = http + UrlPath_send_code
    url_device_next = http + UrlPath_device_next
    """用户使用账号密码登录"""
    # pwd = get_md5(password)
    # json参数拼接
    json1 = {
        "phone": phone,
        "loginPassword": get_md5(password),
        "phoneArea": phoneArea
    }
    sign1 = {"sign": get_sign(json1)}
    json1.update(sign1)
    # headers参数拼接
    headers = {}
    headers.update(JSON_dev)
    # headers = JSON2
    # 用户登录请求
    res_login = requests.session().post(url=url, headers=headers,
                                        json=json1)
    # print(res_login.json())
    """登录失败，需要设备验证"""
    if res_login.json().get("code") == "010007" \
            or res_login.json().get("msg") == "用户登陆的设备和以前不一样":
        smsCode = "6"  # /*** 登录*/LOGIN("1"),/*** 忘记密码*/FORGET("2"),/*** 更换手机号-旧手机号*/PHONE_OLD("3"),
        # /*** 更换手机号-新手机号*/PHONE_NEW("4"),/*** 修改密码*/UPDATE_PASSWORD("5"),/*** 设备认证*/DEVICE("6"),
        # /*** 绑定第三方登录短信验证*/BIND_DEVICE("7");
        """发送短信"""
        response_getdata = send_code(url_send_code, headers, phone, smsCode)
        # print(response_getdata.json())
        """设备验证下一步"""
        # 获取短信验证码verificationCode
        verificationCode = response_getdata.json().get("data")
        # data参数拼接
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
        response_gettoken = requests.session().post(url=url_device_next, headers=headers,
                                                    data=data)
        # print(response_gettoken.json())
        # 获取登录token
        res = res_login.json().get("data").get("token")
        with open(BASE_DIR + r'/TestData/token.yaml', 'w') as file:
            file.write("token: " + str(res))
        # print(res)
        return res

    else:
        # 如果登陆成功，直接到这里并获取登录token
        res = res_login.json().get("data").get("token")
        with open(BASE_DIR + r'/TestData/token.yaml', 'w') as file:
            file.write("token: " + str(res))
        # print(res)
        return res


# print(getlogintoken("18727087210", "123456789", "86"))
# print(getlogintoken("15816430500", "zr123456", "86"))
