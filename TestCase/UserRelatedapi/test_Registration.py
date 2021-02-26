# test_Registration
import json

import allure
import pytest

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.md5 import get_md5
from Common.tools.read_yaml import yamltoken
from Common.tools.unique_text import get_unique_phone

from glo import JSON, HTTP, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('用户相关接口-第一次登陆注册系统账户')
class TestRegistration():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_Registration(self):
        header = JSON
        headers = {}
        headers.update(header)
        token = {"token": yamltoken()}
        headers.update(token)  # 将token更新到headers
        # print(headers)

        # 拼装参数

        phone = get_unique_phone()
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
        if response_getdata.json().get("code") =="000000":
            verificationCode = response_getdata.json().get("data")
            url = HTTP + "/as_user/api/user_account/v1/set_login_password"
            password = "zr123456"
            paylo = {
                "loginPassword": get_md5(f"{password}"),
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
                url=url, headers=headers, data=payload, title="第一次登陆注册系统账户"
            )

            j = r.json()
            # print(j)
            assert r.status_code == 200
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
            if "data" in j:
                assert j.get("data").get("phone") == paylo.get("phone")
                assert j.get("data").get("phoneArea") == paylo.get("phoneArea")
                assert "token" in j.get("data")
                assert "userId" in j.get("data")

            with open(BASE_DIR + r"/TestData/正常的手机号与密码.txt", "a", encoding="utf-8") as f:
                f.write(f"{paylo.get('phone')}|{password}\n")

        else:
            raise AssertionError(f"{response_getdata.json()}")
