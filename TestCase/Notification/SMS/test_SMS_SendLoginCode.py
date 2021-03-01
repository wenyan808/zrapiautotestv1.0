# test_SMS_SendLoginCode
import json

import allure
import pytest

from Common.sign import get_sign

from Common.requests_library import Requests

from glo import JSON, HTTP


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('短信相关接口-发送登陆短信验证码')
class TestSMSSendLoginCode():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_SMS_SendLoginCode(self):
        # 拼装参数
        headers = JSON
        phone = "15809433400"
        boby = {
            "phone": phone,
            "countryCode": "86"
        }
        sign1 = {"sign": get_sign(boby)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(boby)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))
        response_getdata = Requests(self.session).post(
            url=HTTP + "/as_notification/api/sms/v1/send_login_code",
            headers=headers, data=payload, title="发送登陆短信验证码"
        )
        j =response_getdata.json()
        assert response_getdata.status_code == 200
        if j.get("code") == "000000":
            assert j.get("msg") == "ok"

        else:
            raise ValueError(f"{j}")