# test_SMS_SendNewReplaceCode
import json

import allure
import pytest

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.md5 import get_md5

from glo import JSON, HTTP, countryCode, pwd1, phoneArea


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('短信相关接口-修改手机号发送短信验证码-新手机号')
class TestSMSSendNewReplaceCode():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_SMS_SendNewReplaceCode(self):
        # 拼装参数
        headers = {}
        headers.update(JSON)
        phone = "15816144700"
        # password = "zr123456"
        password = pwd1
        url = HTTP + "/as_user/api/user_account/v1/user_login_pwd"
        paylo = {
            "loginPassword": get_md5(password),
            "phone": phone,
            "phoneArea": phoneArea
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
        header = {}
        header.update(JSON)
        headers1 = {}
        headers1.update(header)
        token = {"token": headers_token}
        # print(type(token))
        headers1.update(token)  # 将token更新到headers
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
            url=HTTP + "/as_notification/api/sms/v1/send_new_replace_code",
            headers=headers1, data=payload, title="修改手机号发送短信验证码-新手机号"
        )
        j1 = response_getdata.json()
        assert response_getdata.status_code == 200
        if j1.get("code") == "000000":
            assert j1.get("msg") == "ok"

        else:
            raise ValueError(f"{j1}")