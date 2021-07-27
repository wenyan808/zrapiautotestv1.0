# test_ModifyLoginPassword02
"""
@File  ：test_ModifyLoginPassword02.py
@Author: yishouquan
@Time  : 2020/7/26
@Desc  :  修改手机号-新手机号验证
"""
import json

import allure
import pytest

from Common.getTestLoginToken import getlogintoken
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.md5 import get_md5
from Common.tools.read_write_json import get_json, write_json

from Common.tools.unique_text import get_unique_username

from glo import JSON2, HTTP, BASE_DIR, phoneArea, countryCode


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('用户相关接口-修改手机号-新手机号验证')
class TestModifyLoginPassword02():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('oldpassword',
                             get_json(BASE_DIR + r"/TestData/UserRelatedapiData/oldPassword.json"))
    def test_ModifyLoginPassword02(self, oldpassword):
        # 拼装参数
        headers = JSON2

        phone = "15815453900"
        oldLoginPassword = oldpassword.get("LoginPassword")
        password = oldLoginPassword

        newLoginPassword = get_unique_username(1)[0]  # 通过获取用户名做为账号的密码，get_unique_username(1)获取的结果是一个列表

        pwd = [{"LoginPassword": newLoginPassword}]

        write_json(BASE_DIR + r"/TestData/UserRelatedapiData/oldPassword.json", pwd)

        headers_token = getlogintoken(phone, password, phoneArea)
        # print(headers_token)
        headers1 = {}
        headers1.update(headers)
        token = {"token": headers_token}
        # print(type(token))
        headers1.update(token)  # 将token更新到headers参数中
        smsCode = "5"  # /*** 登录*/LOGIN("1"),/*** 忘记密码*/FORGET("2"),/*** 更换手机号-旧手机号*/PHONE_OLD("3"),
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
        response_getdata = Requests(self.session).post(
            url=HTTP + "/as_notification/api/sms/v1/send_code",
            headers=headers1, data=payload, title="发送短信"
        )
        verificationCode = response_getdata.json().get("data")
        url1 = HTTP + "/as_user/api/user_account/v1/modify_login_password_v1"
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

        r = Requests(self.session).post(
            url=url1, headers=headers1, data=payload, title="修改登录密码-第一步（验证修改密码验证码）"
        )
        j = r.json()
        businessAccessToken = j.get("data").get('businessAccessToken')
        # print(businessAccessToken)
        url2 = HTTP + "/as_user/api/user_account/v1/modify_login_password_v2"
        paylo = {
            "oldLoginPassword": get_md5(oldLoginPassword),
            "businessAccessToken": businessAccessToken,
            "newLoginPassword": get_md5(newLoginPassword)
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r1 = Requests(self.session).post(
            url=url2, headers=headers1, data=payload, title="修改登录密码-第二步"
        )
        j1 = r1.json()
        # print(j1)
        assert r1.status_code == 200
        try:
            assert j1.get("code") == "000000"
            assert j1.get("msg") == "ok"

        except:
            raise ValueError(
                f"\n请求地址：{url2}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers1}"
                f"\n返回数据结果：{j1}"
            )
