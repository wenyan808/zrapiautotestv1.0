# test_ModifyPhone01
import json

import allure
import pytest

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.md5 import get_md5
from Common.tools.read_yaml import yamltoken

from glo import JSON, HTTP


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('用户相关接口-修改手机号-当前使用手机号验证')
class TestModifyPhone01():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_ModifyPhone01(self):
        # 拼装参数
        header = JSON
        headers = {}
        headers.update(header)
        token = {"token": yamltoken()}
        headers.update(token)  # 将token更新到headers
        # print(headers)

        phone = "13321165200"
        password = "zr123456"
        url = HTTP + "/as_user/api/user_account/v1/user_login_pwd"
        paylo = {
            "password": get_md5(password),
            "phone": phone,
            "phoneArea": "86"
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="用户密码登陆"
        )

        j = r.json()
        # print(j)
        headers_token = j.get("data").get("token")
        headers1 = {}
        headers1.update(header)
        token = {"token": headers_token}
        # print(type(token))
        headers1.update(token)  # 将token更新到headers
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
            url=HTTP + "/as_notification/api/sms/v1/send_old_replace_code",
            headers=headers1, data=payload, title="修改手机号发送短信验证码-当前手机号"
        )
        verificationCode = response_getdata.json().get("data")

        url = HTTP + "/as_user/api/user_account/v1/modify_phone_v1"
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

        r1 = Requests(self.session).post(
            url=url, headers=headers1, data=payload, title="修改手机号-当前使用手机号验证"
        )

        j1 = r1.json()
        # print(j1)

        assert r1.status_code == 200
        if j1.get("code") == "000000":
            assert j1.get("msg") == "ok"
            if "data" in j1:
                assert j1.get("data").get("phone") == paylo.get("phone")

        else:
            raise ValueError(f"{j1}")
