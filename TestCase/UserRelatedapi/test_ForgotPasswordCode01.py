# test_ForgotPasswordCode01
"""
@File  ：test_ForgotPasswordCode01.py
@Author: yishouquan
@Time  : 2020/7/27
@Desc  :  用户相关 -忘记登录密码-第一步
"""
import json

import allure

from Business.Urlpath.UrlPath_userlogin import UrlPath_send_code, UrlPath_forgot_password_code
from Common.send_code import send_code
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.redisfuction import deviceOR, phoneOR

from glo import JSON, HTTP, countryCode, phoneArea


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('用户相关接口-忘记登录密码-第一步')
class TestForgotPasswordCode01():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_ForgotPasswordCode01(self):
        # 拼装参数
        headers = {}
        headers.update(JSON)
        # 修改设备号次数
        deviceOR(2, JSON.get("deviceId"))
        phone = "15816262885"
        # 修改手机号验证次数
        phoneOR(2, phoneArea, phone)
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

        r = Requests(self.session).post(
            url=url_forgot_password_code, headers=headers, data=payload, title="忘记登录密码-第一步"
        )

        j = r.json()
        # print(j)

        assert r.status_code == 200
        try:
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"

        except:
            assert j.get("code") == "010001"
            assert j.get("msg") == "您输入的验证码不正确"

        # else:
        #     raise ValueError(
        #         f"\n请求地址：{url1}"
        #         f"\nbody参数：{payload}"
        #         f"\n请求头部参数：{headers}"
        #         f"\n返回数据结果：{j}")
