# test_ModifyPhone01
"""
@File  ：test_ModifyPhone01.py
@Author: yishouquan
@Time  : 2020/7/27
@Desc  :  修改手机号-新手机号
"""
import json
import logging

import allure
import pytest

from Common.getTestLoginToken import getlogintoken
from Common.sign import get_sign

from Common.requests_library import Requests

from glo import JSON2, HTTP, phoneArea, countryCode, pwd1


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('用户相关接口-修改手机号-当前使用手机号验证')
class TestModifyPhone01():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        cls.url = HTTP + "/as_notification/api/sms/v1/send_code"
        cls.url1 = HTTP + "/as_user/api/user_account/v1/modify_phone_v1"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_ModifyPhone01(self):
        # 拼装参数
        headers = JSON2
        phone = "13321165200"
        password = pwd1
        headers_token = getlogintoken(phone, password, phoneArea)
        # print(headers_token)
        headers1 = {}
        headers1.update(headers)
        token = {"token": headers_token}
        # print(type(token))
        headers1.update(token)  # 将token更新到headers
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
            url=self.url, headers=headers1, data=payload, title="发送短信-当前手机号"
        )
        j = response_getdata.json()
        if "data" in j:
            paylo = {
                "verificationCode": j.get("data"),
                "phone": phone,
                "phoneArea": phoneArea
            }
            sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
            payload1 = {}
            payload1.update(paylo)
            payload1.update(sign1)
            payload = json.dumps(dict(payload1))
            r1 = Requests(self.session).post(
                url=self.url1, headers=headers1, data=payload, title="修改手机号-当前使用手机号验证"
            )
            j1 = r1.json()
            # print(j1)
            assert r1.status_code == 200
            if j1.get("code") == "000000":
                assert j1.get("msg") == "ok"
                if "data" in j1:
                    assert "businessAccessToken" in j1.get("data")

            else:
                raise ValueError(f"{j1}")
        else:
            logging.info("验证码获取失败")
