# test_ModifyPhone02
import json

import allure
import pytest

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.md5 import get_md5
from Common.tools.read_write_json import get_json, write_json

from Common.tools.unique_text import get_unique_phone

from glo import JSON, HTTP, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('用户相关接口-修改手机号-当前使用手机号验证')
class TestModifyPhone02():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('oldphone',
                             get_json(BASE_DIR + r"/TestData/UserRelatedapiData/oldPhone.json"))
    def test_ModifyPhone02(self, oldphone):
        # 拼装参数
        headers = JSON

        phone = oldphone.get("phone")

        password = "zr123456"
        newPhone = get_unique_phone()

        paylonewname = [{"phone": newPhone}]

        write_json(BASE_DIR + r"/TestData/UserRelatedapiData/oldPhone.json", paylonewname)

        phoneArea = oldPhoneArea = newPhoneArea = "86"
        # 用户手机号密码登录
        url = HTTP + "/as_user/api/user_account/v1/user_login_pwd"
        paylo = {
            "password": get_md5(password),
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
        # 获取登录的token
        headers_token = j.get("data").get("token")
        header = JSON
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
            url=HTTP + "/as_notification/api/sms/v1/send_old_replace_code",
            headers=headers1, data=payload, title="修改手机号发送短信验证码-当前手机号"
        )
        verificationCode = response_getdata.json().get("data")
        boby1 = {
            "phone": newPhone,
            "countryCode": phoneArea
        }
        sign1 = {"sign": get_sign(boby1)}  # 把参数签名后通过sign1传出来
        payload2 = {}
        payload2.update(boby1)
        payload2.update(sign1)

        payload3 = json.dumps(dict(payload2))
        response1_getdata = Requests(self.session).post(
            url=HTTP + "/as_notification/api/sms/v1/send_new_replace_code",
            headers=headers1, data=payload3, title="修改手机号发送短信验证码-新手机号"
        )
        newVerificationCode = response1_getdata.json().get("data")

        url = HTTP + "/as_user/api/user_account/v1/modify_phone_v2"
        paylo = {
            "verificationCode": verificationCode,
            "phone": phone,
            "oldPhoneArea": oldPhoneArea,
            "newPhone": newPhone,
            "newVerificationCode": newVerificationCode,
            "newPhoneArea": newPhoneArea
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r1 = Requests(self.session).post(
            url=url, headers=headers1, data=payload, title="修改手机号-新手机号验证"
        )
        j1 = r1.json()
        # print(j1)

        assert r1.status_code == 200
        if j1.get("code") == "000000":
            assert j1.get("msg") == "ok"


        else:
            raise ValueError(f"{j1}")
