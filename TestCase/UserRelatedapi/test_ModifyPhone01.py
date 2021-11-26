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

from Business.Urlpath.UrlPath_userlogin import UrlPath_send_code, UrlPath_modify_phone_v1
from Common.getTestLoginToken import getlogintoken
from Common.send_code import send_code
from Common.sign import get_sign

from Common.requests_library import Requests

from glo import JSON_dev, HTTP, phoneArea, countryCode, pwd1


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('用户相关接口-修改手机号-当前使用手机号验证')
class TestModifyPhone01():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        cls.url_send_code = HTTP + UrlPath_send_code
        cls.url_modify_phone_v1 = HTTP + UrlPath_modify_phone_v1

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_ModifyPhone01(self):

        phone = "15816430500"
        password = pwd1
        headers = {}
        headers.update(JSON_dev)
        headers_token = getlogintoken(phone, password, phoneArea)

        token = {"token": headers_token}
        # print(token)

        headers.update(token)  # 将token更新到headers
        # print(headers)
        """发送短信"""
        smsCode = "3"  # /*** 登录*/LOGIN("1"),/*** 忘记密码*/FORGET("2"),/*** 更换手机号-旧手机号*/PHONE_OLD("3"),
        # /*** 更换手机号-新手机号*/PHONE_NEW("4"),/*** 修改密码*/UPDATE_PASSWORD("5"),/*** 设备认证*/DEVICE("6"),
        # /*** 绑定第三方登录短信验证*/BIND_DEVICE("7");
        # url = HTTP + "/as_notification/api/sms/v1/send_code"
        response_getdata = send_code(self.url_send_code, headers, phone, smsCode)
        # print(response_getdata.json())
        verificationCode = response_getdata.json().get("data")

        if verificationCode != None:
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
            r1 = Requests(self.session).post(
                url=self.url_modify_phone_v1, headers=headers, data=payload, title="修改手机号-当前使用手机号验证"
            )
            j1 = r1.json()
            # print(j1)
            assert r1.status_code == 200
            try:
                assert j1.get("code") == "000000"
                assert j1.get("msg") == "ok"
                if "data" in j1:
                    assert "businessAccessToken" in j1.get("data")

            except:
                raise AssertionError(
                    f"\n请求地址：{self.url_modify_phone_v1}"
                    f"\nbody参数：{payload}"
                    f"\n请求头部参数：{headers}"
                    f"\n返回数据结果：{j1}"
                )
        else:
            logging.info("验证码获取失败")
