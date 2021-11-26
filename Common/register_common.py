import json

import requests

from Business.Urlpath.UrlPath_userlogin import UrlPath_send_code, UrlPath_user_login_code, \
    UrlPath_set_login_password
from Common.send_code import send_code
from Common.sign import get_sign
from Common.tools.md5 import get_md5
from Common.tools.unique_text import get_unique_phone
from glo import JSON1, pwd1, phoneArea, HTTP


def get_registerno():
    # url管理
    url_send_code = HTTP + UrlPath_send_code
    url_user_login_code = HTTP + UrlPath_user_login_code
    url_set_login_password = HTTP + UrlPath_set_login_password
    # 拼装headers参数
    headers = JSON1
    # 获取不重复手机号码
    phone = get_unique_phone()
    # print(phone)
    # 注册登录新手机号
    # 写死smsCode
    smsCode = "1"  # /*** 登录*/LOGIN("1"),/*** 忘记密码*/FORGET("2"),/*** 更换手机号-旧手机号*/PHONE_OLD("3"),
    # /*** 更换手机号-新手机号*/PHONE_NEW("4"),/*** 修改密码*/UPDATE_PASSWORD("5"),/*** 设备认证*/DEVICE("6"),
    # /*** 绑定第三方登录短信验证*/BIND_DEVICE("7");
    """发送短信"""
    response_getdata = send_code(url_send_code, headers, phone, smsCode)
    # print(response_getdata.json())
    # 发送短信接口成功
    if response_getdata.json().get("code") == "000000":
        # 获取短信验证码
        verificationCode = response_getdata.json().get("data")
        # url = HTTP + "/as_user/api/user_account/v1/user_login_code"
        # password = "zr123456"
        # 拼接body参数
        paylo1 = {
            # "loginPassword": get_md5(f"{password}"),
            "verificationCode": verificationCode,
            "phone": phone,
            "phoneArea": phoneArea
        }
        # 获取sign并把参数签名后通过sign1传出来
        sign1 = {"sign": get_sign(paylo1)}
        payload1 = {}
        payload1.update(paylo1)
        payload1.update(sign1)

        json2 = json.dumps(dict(payload1))
        """第一次登陆注册系统账户"""
        r = requests.session().post(url=url_user_login_code, headers=headers,
                                    data=json2)

        j = r.json()
        # print(j)
        if j.get("code") == "010003" \
                or j.get("msg") == "第一次登录，设置登录密码":
            # 获取密码并进行MD5加密
            password = pwd1
            pwd = get_md5(password)
            # 获取businessAccessToke
            businessAccessToken = j.get("data").get("businessAccessToken")
            # 拼接body参数
            paylo = {
                "phone": phone,
                "phoneArea": phoneArea,
                "loginPassword": pwd,
                "businessAccessToken": businessAccessToken
            }
            sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
            payload1 = {}
            payload1.update(paylo)
            payload1.update(sign1)

            json3 = json.dumps(dict(payload1))
            # 注册登陆手机号第一次登录需设置密码
            r1 = requests.session().post(url=url_set_login_password, headers=headers,
                                         data=json3)
            j_set_login_password = r1.json()
            # print(j_set_login_password)
            # with open(BASE_DIR + r"/TestData/UserRelatedapiData/正常的手机号与密码.txt", "a", encoding="utf-8") as f:
            #     f.write(f"{j1.get('data').get('phone')}|{password}\n")
            return j_set_login_password.get('data').get('phone'), password, headers


# print(get_registerno())
# paylonewphone = [{"phone": list(get_registerno())[0]}]
# print(paylonewphone)
