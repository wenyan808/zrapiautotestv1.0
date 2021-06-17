# test_UserLoginCode
import json

import allure
import pytest

from Common.sign import get_sign

from Common.requests_library import Requests


from glo import JSON, HTTP, countryCode, phoneArea


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('用户相关接口-用户验证码登陆')
class TestUserLoginCode():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_UserLoginCode(self):

        # 拼装参数
        headers = JSON
        phone = "15816262890"
        smsCode = "1"  # /*** 登录*/LOGIN("1"),/*** 忘记密码*/FORGET("2"),/*** 更换手机号-旧手机号*/PHONE_OLD("3"),
        # /*** 更换手机号-新手机号*/PHONE_NEW("4"),/*** 修改密码*/UPDATE_PASSWORD("5"),/*** 设备认证*/DEVICE("6"),
        # /*** 绑定第三方登录短信验证*/BIND_DEVICE("7");
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
        response_getdata = Requests(self.session).post(
            url=HTTP + "/as_notification/api/sms/v1/send_code",
            headers=headers, data=payload, title="发送短信"
        )
        verificationCode = response_getdata.json().get("data")
        url = HTTP + "/as_user/api/user_account/v1/user_login_code"
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

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="用户验证码登陆"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        if j.get("code") == "000000":
            assert j.get("msg") == "ok"
            if "data" in j:
                assert j.get("data").get("phone") == paylo.get("phone")
                assert j.get("data").get("phoneArea") == paylo.get("phoneArea")
                assert "token" in j.get("data")
                assert "userId" in j.get("data")
        else:
            raise ValueError(f"{j}")
