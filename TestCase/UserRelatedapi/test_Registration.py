# test_Registration
import json

import allure
import pytest

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.md5 import get_md5

from Common.tools.unique_text import get_unique_phone

from glo import JSON2, HTTP, BASE_DIR, phoneArea, countryCode, pwd1


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

        # 拼装参数
        headers = JSON2
        phone = get_unique_phone()
        smsCode = "1"    # /*** 登录*/LOGIN("1"),/*** 忘记密码*/FORGET("2"),/*** 更换手机号-旧手机号*/PHONE_OLD("3"),
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
        # print(response_getdata.json())
        if response_getdata.json().get("code") == "000000":
            verificationCode = response_getdata.json().get("data")
            url = HTTP + "/as_user/api/user_account/v1/user_login_code"
            # password = "zr123456"
            paylo1 = {
                # "loginPassword": get_md5(f"{password}"),
                "verificationCode": verificationCode,
                "phone": phone,
                "phoneArea": phoneArea
            }

            sign1 = {"sign": get_sign(paylo1)}  # 把参数签名后通过sign1传出来
            payload1 = {}
            payload1.update(paylo1)
            payload1.update(sign1)

            payload = json.dumps(dict(payload1))

            r = Requests(self.session).post(
                url=url, headers=headers, data=payload, title="第一次登陆注册系统账户"
            )

            j = r.json()
            # print(j)
            if j.get("code") == "010003" \
                    or j.get("msg") == "第一次登录，设置登录密码":
                password = pwd1
                pwd = get_md5(password)
                businessAccessToken = j.get("data").get("businessAccessToken")
                url1 = HTTP + "/as_user/api/user_account/v1/set_login_password"
                paylo = {
                    "loginPassword": pwd,
                    "businessAccessToken": businessAccessToken
                }
                sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
                payload1 = {}
                payload1.update(paylo)
                payload1.update(sign1)

                payload = json.dumps(dict(payload1))
                r1 = Requests(self.session).post(
                    url=url1, headers=headers, data=payload, title="第一次登陆注册系统账户时设置登录密码"
                )
                j1 = r1.json()
                # print(j1)
                assert r1.status_code == 200
                assert j1.get("code") == "000000"
                assert j1.get("msg") == "ok"
                if "data" in j1:
                    assert j1.get("data").get("phone") == paylo1.get("phone")
                    assert j1.get("data").get("phoneArea") == paylo1.get("phoneArea")
                    assert "token" in j1.get("data")
                    assert "userId" in j1.get("data")

                with open(BASE_DIR + r"/TestData/UserRelatedapiData/正常的手机号与密码.txt", "a", encoding="utf-8") as f:
                    f.write(f"{j1.get('data').get('phone')}|{password}\n")

        else:
            raise AssertionError(f"{response_getdata.json()}")
