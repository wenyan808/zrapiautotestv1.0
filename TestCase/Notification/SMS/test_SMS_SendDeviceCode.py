# test_SMS_SendDeviceCode
import json

import allure
import pytest

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.md5 import get_md5

from glo import HTTP, countryCode


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('短信相关接口-新设备登录短信验证')
class TestSMSSendDeviceCode():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_SMS_SendDeviceCode(self):

        # 拼装参数
        headers = {
            "Content-Type": "application/json",
            "appVersion": "0.2.4",
            "deviceId": "A109B58C-D9C4-474A-87B5-878091E317AC",
            "osType": "ios",
            "osVersion": "13.1.1",
            "lang": "zh_CN"
        }

        phone = "15817293400"

        boby = {
            "phone": phone,
            "countryCode": countryCode
        }
        sign1 = {"sign": get_sign(boby)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(boby)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))
        response_getdata = Requests(self.session).post(
            url=HTTP + "/as_notification/api/sms/v1/send_device_code",
            headers=headers, data=payload, title="新设备登录短信验证"
        )
        j = response_getdata.json()
        assert response_getdata.status_code == 200
        if j.get("code") == "000000":
            assert j.get("msg") == "ok"

        else:
            raise AssertionError(f"{j}")
