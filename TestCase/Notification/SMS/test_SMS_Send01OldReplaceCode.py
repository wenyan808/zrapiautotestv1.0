# test_SMS_SendOldReplaceCode
import json

import allure
import pytest

from Common.getTestLoginToken import getlogintoken
from Common.sign import get_sign

from Common.requests_library import Requests

from glo import JSON1, HTTP, countryCode, phoneArea, pwd1


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('短信相关接口-修改手机号发送短信验证码-当前手机号')
class TestSMSSendOldReplaceCode():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_SMS_SendOldReplaceCode(self):
        url = HTTP + "/as_notification/api/sms/v1/send_old_replace_code"
        phone = "15816144700"
        # password = "zr123456"
        password = pwd1
        headers_token = getlogintoken(phone, password, phoneArea)
        header = JSON1
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
            url=url,
            headers=headers1, data=payload, title="修改手机号发送短信验证码-当前手机号"
        )
        j = response_getdata.json()
        assert response_getdata.status_code == 200
        if j.get("code") == "000000":
            assert j.get("msg") == "ok"

        else:
            raise AssertionError(
                f"\n请求地址：{url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers1}"
                f"\n返回数据结果：{j}"
            )
