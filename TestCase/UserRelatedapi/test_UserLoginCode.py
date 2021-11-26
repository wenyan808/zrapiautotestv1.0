# test_UserLoginCode
import json

import allure
import pytest

from Business.Urlpath.UrlPath_userlogin import UrlPath_send_code, UrlPath_user_login_code
from Common.register_common import get_registerno
from Common.send_code import send_code
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
        # 注册并获取手机号
        sign_in = list(get_registerno())
        phone = sign_in[0]
        # 拼装headers参数
        headers = {}
        headers.update(sign_in[-1])

        """发送短信"""
        smsCode = "1"  # /*** 登录*/LOGIN("1"),/*** 忘记密码*/FORGET("2"),/*** 更换手机号-旧手机号*/PHONE_OLD("3"),
        # /*** 更换手机号-新手机号*/PHONE_NEW("4"),/*** 修改密码*/UPDATE_PASSWORD("5"),/*** 设备认证*/DEVICE("6"),
        # /*** 绑定第三方登录短信验证*/BIND_DEVICE("7");
        url_send_code = HTTP + UrlPath_send_code
        response_getdata = send_code(url_send_code, headers, phone, smsCode)
        # 获取短信验证码
        verificationCode = response_getdata.json().get("data")
        # 用户验证码登陆
        url = HTTP + UrlPath_user_login_code
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
        try:
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
            if "data" in j:
                assert j.get("data").get("phone") == paylo.get("phone")
                assert j.get("data").get("phoneArea") == paylo.get("phoneArea")
                assert "token" in j.get("data")
                assert "userId" in j.get("data")
            else:
                print(j.get("data"))
        except:
                raise AssertionError(
                    f"\n请求地址：{url}"
                    f"\nbody参数：{payload}"
                    f"\n请求头部参数：{headers}"
                    f"\n返回数据结果：{j}")
