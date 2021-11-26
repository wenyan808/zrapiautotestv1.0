# test_ForgotPasswordCode02
"""
@File  ：test_ForgotPasswordCode02.py
@Author: yishouquan
@Time  : 2020/7/27
@Desc  :  用户相关 -忘记登录密码-第二步
"""
import json

import allure
import pytest

from Business.Urlpath.UrlPath_userlogin import UrlPath_send_code, UrlPath_reset_login_password, \
    UrlPath_forgot_password_code
from Common.send_code import send_code
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.md5 import get_md5

from glo import JSON, HTTP, countryCode, phoneArea


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('用户相关接口-忘记登录密码-第二步')
class TestForgotPasswordCode02():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_ForgotPasswordCode02(self):
        """拼装参数：headers,phone,password,smsCode为2固定传值"""
        headers = {}
        headers.update(JSON)

        phone = "15816262885"
        password = "zr1234567"
        smsCode = "2"  # /*** 登录*/LOGIN("1"),/*** 忘记密码*/FORGET("2"),/*** 更换手机号-旧手机号*/PHONE_OLD("3"),
        # /*** 更换手机号-新手机号*/PHONE_NEW("4"),/*** 修改密码*/UPDATE_PASSWORD("5"),/*** 设备认证*/DEVICE("6"),
        # /*** 绑定第三方登录短信验证*/BIND_DEVICE("7");
        url_send_code = HTTP + UrlPath_send_code
        """发送短信"""
        response_getdata = send_code(url_send_code, headers, phone, smsCode)
        if "data" in response_getdata.json():
            verificationCode = response_getdata.json().get("data")
        else:
            verificationCode = "123456"
        """忘记登录密码-第一步"""
        url_forgot_password_code = HTTP + UrlPath_forgot_password_code
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

        r_forgot_password_code = Requests(self.session).post(
            url=url_forgot_password_code, headers=headers, data=payload, title="忘记登录密码-第一步"
        )
        # print(r_forgot_password_code.json())
        if r_forgot_password_code.json().get("code") == "000000" and r_forgot_password_code.json().get("msg") == "ok":
            businessAccessToken = r_forgot_password_code.json().get("data").get("businessAccessToken")
            """忘记登录密码-第二步"""
            url_reset_login_password = HTTP + UrlPath_reset_login_password
            paylo = {
                "newLoginPassword": get_md5(password),
                "businessAccessToken": businessAccessToken
            }
            sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
            payload1 = {}
            payload1.update(paylo)
            payload1.update(sign1)

            payload = json.dumps(dict(payload1))

            r = Requests(self.session).post(
                url=url_reset_login_password, headers=headers, data=payload, title="忘记登录密码-第二步"
            )

            j = r.json()
            # print(j)

            assert r.status_code == 200
            try:
                assert j.get("code") == "000000"
                assert j.get("msg") == "ok"
            except:
                assert j.get("code") == "010010"
                assert j.get("msg") == "用户暂未注册"
        else:
            raise AssertionError(f"\n请求地址：{url_forgot_password_code}"
                                 f"\nbody参数：{payload}"
                                 f"\n请求头部参数：{headers}"
                                 f"\n返回数据结果：{r_forgot_password_code.json()}")
