# test_ForgotPasswordCode01
import json

import allure
import pytest

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.md5 import get_md5
from Common.tools.read_yaml import yamltoken

from glo import JSON, HTTP


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
        header = JSON
        headers = {}
        headers.update(header)
        token = {"token": yamltoken()}
        headers.update(token)  # 将token更新到headers
        # print(headers)

        phone = "15816262885"
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
            url=HTTP + "/as_notification/api/sms/v1/send_forget_code",
            headers=headers, data=payload, title="发送登陆短信验证码"
        )
        verificationCode = response_getdata.json().get("data")

        url = HTTP + "/as_user/api/user_account/v1/forgot_password_code"
        paylo = {
            "verificationCode": verificationCode,
            "phone": phone,
            "phoneArea": "86"
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="忘记登录密码-第一步"
        )

        j = r.json()
        # print(j)

        assert r.status_code == 200
        if j.get("code") == "000000":
            assert j.get("msg") == "ok"
            # if "data" in j:
            #     assert j.get("data").get("phone") == paylo.get("phone")
            #     assert j.get("data").get("phoneArea") == paylo.get("phoneArea")
            #     assert "token" in j.get("data")
            #     assert "userId" in j.get("data")
        else:
            raise ValueError(f"{j}")
