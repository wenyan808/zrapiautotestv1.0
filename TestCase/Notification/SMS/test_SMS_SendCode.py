# test_SMS_SendCode
import json

import allure
import pytest

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.md5 import get_md5
from Common.tools.read_write_json import get_json

from glo import HTTP, countryCode, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('短信相关接口-发送短信')
class TestSMSSendCode():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/testSMSData/test_SMS_SendCode.json"))
    def test_SMS_SendCode(self, info):

        url = HTTP + "/as_notification/api/sms/v1/send_code"
        headers = {
            "Content-Type": "application/json",
            "appVersion": "0.2.4",
            "deviceId": "A109B58C-D9C4-474A-87B5-878091E317AC",
            "osType": "ios",
            "osVersion": "13.1.1",
            "lang": "zh_CN"
        }

        phone = "15817293400"

        smsCode = info.get("smsCode")  # /*** 登录*/LOGIN("1"),/*** 忘记密码*/FORGET("2"),/*** 更换手机号-旧手机号*/PHONE_OLD("3"),
        # /*** 更换手机号-新手机号*/PHONE_NEW("4"),/*** 修改密码*/UPDATE_PASSWORD("5"),/*** 设备认证*/DEVICE("6"),
        # /*** 绑定第三方登录短信验证*/BIND_DEVICE("7");
        type = info.get("type")  # 当smsCode为7（绑定第三方登录短信验证）时必传type。第三方登录类型：1-微信2-weibo
        if smsCode == "7":
            boby = {
                "phone": phone,
                "countryCode": countryCode,
                "smsCode": smsCode,
                "type": type
            }
        else:
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
        r = Requests(self.session).post(
            url=url,
            headers=headers, data=payload, title="发送短信"
        )
        j = r.json()
        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
            assert "data" in j

        except:
            raise AssertionError(
                f"\n请求地址：{url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}"
            )
