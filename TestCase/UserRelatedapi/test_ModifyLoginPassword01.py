# test_ModifyLoginPassword01
import json

import allure
import pytest

from Common.getTestLoginToken import getlogintoken
from Common.sign import get_sign

from Common.requests_library import Requests


from glo import HTTP, JSON2


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('用户相关接口-修改手机号-当前使用手机号验证')
class TestModifyLoginPassword01():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_ModifyLoginPassword01(self):
        # 拼装参数
        header = JSON2

        phone = "15823174100"
        password = "zr123456"
        phoneArea = "86"

        # 获取登录的token
        headers_token = getlogintoken(phone, password, phoneArea)
        headers1 = {}
        headers1.update(header)
        token = {"token": headers_token}
        # print(type(token))
        headers1.update(token)  # 将token更新到headers参数中
        boby = {
            "phone": phone,
            "countryCode": phoneArea
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
        verificationCode = response_getdata.json().get("data")
        url1 = HTTP + "/as_user/api/user_account/v1/modify_login_password_v1"
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
            url=url1, headers=headers1, data=payload, title="修改登录密码-第一步（验证修改密码验证码）"
        )
        j1 = r1.json()
        # print(j1)
        assert r1.status_code == 200
        if j1.get("code") == "000000":
            assert j1.get("msg") == "ok"


        else:
            raise ValueError(f"{j1}")
