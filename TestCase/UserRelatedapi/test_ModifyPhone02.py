# test_ModifyPhone02

"""
@File  ：test_Registration.py
@Author: yishouquan
@Time  : 2020/7/26
@Desc  : 第一次登陆注册系统账户
"""

import json

import allure
import pytest

from Common.getTestLoginToken import getlogintoken
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.md5 import get_md5
from Common.tools.read_write_json import get_json, write_json

from Common.tools.unique_text import get_unique_phone

from glo import JSON2, HTTP, BASE_DIR, countryCode, pwd1, phoneArea, newPhoneArea


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('用户相关接口-修改手机号-当前使用手机号验证')
class TestModifyPhone02():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('oldphone',
                             get_json(BASE_DIR + r"/TestData/UserRelatedapiData/oldPhone.json"))
    def test_ModifyPhone02(self, oldphone):

        phone = oldphone.get("phone")

        password = pwd1
        newPhone = get_unique_phone()

        paylonewname = [{"phone": newPhone}]

        write_json(BASE_DIR + r"/TestData/UserRelatedapiData/oldPhone.json", paylonewname)

        # 获取登录的token
        headers_token = getlogintoken(phone, password, phoneArea)
        header = JSON2
        headers1 = {}
        headers1.update(header)
        token = {"token": headers_token}

        headers1.update(token)  # 将token更新到headers参数中
        smsCode = "3"  # /*** 登录*/LOGIN("1"),/*** 忘记密码*/FORGET("2"),/*** 更换手机号-旧手机号*/PHONE_OLD("3"),
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
            headers=headers1, data=payload, title="发送短信-当前手机号"
        )
        verificationCode = response_getdata.json().get("data")

        url = HTTP + "/as_user/api/user_account/v1/modify_phone_v1"
        paylo = {
            "verificationCode": verificationCode,
            "phone": phone,
            "phoneArea": phoneArea
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload2 = {}
        payload2.update(paylo)
        payload2.update(sign1)

        payload0 = json.dumps(dict(payload2))

        r = Requests(self.session).post(
            url=url, headers=headers1, data=payload0, title="修改手机号-当前使用手机号验证"
        )

        j = r.json()
        # print(j)
        smsCode1 = "4"  # /*** 登录*/LOGIN("1"),/*** 忘记密码*/FORGET("2"),/*** 更换手机号-旧手机号*/PHONE_OLD("3"),
        # /*** 更换手机号-新手机号*/PHONE_NEW("4"),/*** 修改密码*/UPDATE_PASSWORD("5"),/*** 设备认证*/DEVICE("6"),
        # /*** 绑定第三方登录短信验证*/BIND_DEVICE("7");
        boby1 = {
            "phone": newPhone,
            "countryCode": countryCode,
            "smsCode": smsCode1
        }
        sign1 = {"sign": get_sign(boby1)}  # 把参数签名后通过sign1传出来
        payload3 = {}
        payload3.update(boby1)
        payload3.update(sign1)

        payload01 = json.dumps(dict(payload3))
        response1_getdata1 = Requests(self.session).post(
            url=HTTP + "/as_notification/api/sms/v1/send_code",
            headers=headers1, data=payload01, title="发送短信-新手机号"
        )
        newVerificationCode = response1_getdata1.json().get("data")
        businessAccessToken = j.get("data").get('businessAccessToken')
        # print(businessAccessToken)
        url1 = HTTP + "/as_user/api/user_account/v1/modify_phone_v2"
        paylo = {
            "businessAccessToken": businessAccessToken,
            "newPhone": newPhone,
            "newVerificationCode": newVerificationCode,
            "newPhoneArea": newPhoneArea
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload4 = {}
        payload4.update(paylo)
        payload4.update(sign1)

        payload02 = json.dumps(dict(payload4))

        r1 = Requests(self.session).post(
            url=url1, headers=headers1, data=payload02, title="修改手机号-新手机号验证"
        )
        j1 = r1.json()

        # print(j1)

        assert r1.status_code == 200
        try:
            assert j1.get("code") == "000000"
            assert j1.get("msg") == "ok"

        except:
            raise AssertionError(
                f"\n请求地址：{url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers1}"
                f"\n返回数据结果：{j}"
            )
