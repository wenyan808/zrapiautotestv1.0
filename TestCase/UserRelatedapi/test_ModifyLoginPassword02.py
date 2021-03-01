# test_ModifyLoginPassword02
import json

import allure
import pytest

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.md5 import get_md5
from Common.tools.read_write_json import get_json, write_json
from Common.tools.read_yaml import yamltoken
from Common.tools.unique_text import get_unique_username

from glo import JSON, HTTP, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('用户相关接口-修改手机号-新手机号验证')
class TestModifyLoginPassword02():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('oldpassword',
                             get_json(BASE_DIR + r"/TestData/UserRelatedapiData/oldPassword.json"))
    def test_ModifyLoginPassword02(self, oldpassword):
        # 拼装参数
        headers = JSON

        phone = "15810433000"
        oldLoginPassword = oldpassword.get("Password")
        password = oldLoginPassword


        newLoginPassword = get_unique_username(1)[0]  # 通过获取用户名做为账号的密码，get_unique_username(1)获取的结果是一个列表

        pwd = [{"Password": newLoginPassword}]

        write_json(BASE_DIR + r"/TestData/UserRelatedapiData/oldPassword.json", pwd)
        phoneArea = "86"
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
        # 获取登录的token
        headers_token = j.get("data").get("token")
        headers1 = {}
        headers1.update(headers)
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
        url1 = HTTP + "/as_user/api/user_account/v1/modify_login_password_v2"
        paylo = {
            "oldLoginPassword": get_md5(oldLoginPassword),
            "verificationCode": verificationCode,
            "phone": phone,
            "phoneArea": phoneArea,
            "newLoginPassword": get_md5(newLoginPassword)
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r1 = Requests(self.session).post(
            url=url1, headers=headers1, data=payload, title="修改登录密码-第二步"
        )
        j1 = r1.json()
        # print(j1)
        assert r1.status_code == 200
        if j1.get("code") == "000000":
            assert j1.get("msg") == "ok"


        else:
            raise ValueError(f"{j1}")
