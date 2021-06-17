# test_DeviceNext
import json

import allure
import pytest

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
            headers=headers, data=payload, title="发送短信"
        )
        verificationCode = response_getdata.json().get("data")
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
        if j1.get("code") == "000000":
            assert j1.get("msg") == "ok"
            assert "userId" in j1.get("data")
            assert "token" in j1.get("data")
            assert j1.get("data").get("phone") == phone
            assert j1.get("data").get("phoneArea") == phoneArea


        else:
            raise ValueError(f"{j1}")
