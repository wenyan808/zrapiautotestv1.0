# test_SMS_SendUpdatePasswordCode
import json

import allure
import pytest


from Common.getTestLoginToken import getlogintoken
from Common.sign import get_sign

from Common.requests_library import Requests

from glo import JSON1, HTTP, phoneArea, countryCode, phone5, pwd5


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('短信相关接口-发送修改密码短信')
class TestSMSSendUpdatePasswordCode():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_SMS_SendUpdatePasswordCode(self):
        # 拼装参数
        headers_token = getlogintoken(phone5, pwd5, phoneArea)
        header = JSON1
        headers1 = {}
        headers1.update(header)
        token = {"token": headers_token}
        # print(type(token))
        headers1.update(token)  # 将token更新到headers
        boby = {
            "phone": phone5,
            "countryCode": countryCode
        }
        sign1 = {"sign": get_sign(boby)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(boby)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))
        response_getdata = Requests(self.session).post(
            url=HTTP + "/as_notification/api/sms/v1/send_update_password_code",
            headers=headers1, data=payload, title="发送修改密码短信"
        )
        j = response_getdata.json()
        assert response_getdata.status_code == 200
        if j.get("code") == "000000":
            assert j.get("msg") == "ok"

        else:
            raise ValueError(f"{j}")
