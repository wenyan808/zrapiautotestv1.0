# test_DeviceNext
"""
@File  ：test_DeviceNext.py
@Author: yishouquan
@Time  : 2020/7/27
@Desc  :  用户相关-设备验证
"""
import json

import allure
import pytest

from Common.send_code import send_code
from Common.sign import get_sign

from Common.requests_library import Requests

from glo import HTTP, phoneArea, countryCode


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('用户相关接口-用户密码登陆')
class TestDeviceNext():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_DeviceNext(self):
        # 拼装参数
        headers = {
            "Content-Type": "application/json",
            "appVersion": "0.2.4",
            "deviceId": "A109B58C-D9C4-474A-87B5-878091E317AC",
            "osType": "ios",
            "osVersion": "13.1.1",
            "lang": "zh_CN"
        }

        phone = "15811365600"
        # password = "zr123456"
        smsCode = "6"  # /*** 登录*/LOGIN("1"),/*** 忘记密码*/FORGET("2"),/*** 更换手机号-旧手机号*/PHONE_OLD("3"),
        # /*** 更换手机号-新手机号*/PHONE_NEW("4"),/*** 修改密码*/UPDATE_PASSWORD("5"),/*** 设备认证*/DEVICE("6"),
        # /*** 绑定第三方登录短信验证*/BIND_DEVICE("7");
        url = HTTP + "/as_notification/api/sms/v1/send_code"
        boby = {
            "phone": phone,
            "countryCode": countryCode,
            "smsCode": smsCode
        }
        """发送短信"""
        response_getdata = send_code(url, headers, boby)
        if "data" in response_getdata.json():
            verificationCode = response_getdata.json().get("data")
        else:
            verificationCode = "123456"
        url1 = HTTP + "/as_user/api/user_account/v1/device_next"
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
            url=url1, headers=headers, data=payload, title="设备验证下一步"
        )
        j1 = r1.json()
        # print(j1)
        assert r1.status_code == 200
        try:
            assert j1.get("code") == "000000"
            assert j1.get("msg") == "ok"
            assert "userId" in j1.get("data")
            assert "token" in j1.get("data")
            assert j1.get("data").get("phone") == phone
            assert j1.get("data").get("phoneArea") == phoneArea

        except:
            assert j1.get("code") == "010001"
            assert j1.get("msg") == "您输入的验证码不正确"

        # else:
        #     raise ValueError(
        #         f"\n请求地址：{url1}"
        #         f"\nbody参数：{payload}"
        #         f"\n请求头部参数：{headers}"
        #         f"\n返回数据结果：{j1}")
