# test_Registration
"""
@File  ：test_Registration.py
@Author: yishouquan
@Time  : 2020/7/26
@Desc  : 第一次登陆注册系统账户
"""

import json

import allure
import pytest

from Business.Urlpath.UrlPath_userlogin import UrlPath_send_code, UrlPath_set_login_password, \
    UrlPath_user_login_code
from Common.send_code import send_code
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.md5 import get_md5

from Common.tools.unique_text import get_unique_phone

from glo import JSON3, HTTP, BASE_DIR, phoneArea, countryCode, pwd1


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
        # url管理
        url_send_code = HTTP + UrlPath_send_code
        url_user_login_pwd = HTTP + UrlPath_user_login_code
        url_set_login_password = HTTP + UrlPath_set_login_password
        # 拼装headers参数
        headers = {}
        headers.update(JSON3)
        # 获取不重复手机号码
        phone = get_unique_phone()
        # 注册登录新手机号
        # 写死smsCode
        smsCode = "1"  # /*** 登录*/LOGIN("1"),/*** 忘记密码*/FORGET("2"),/*** 更换手机号-旧手机号*/PHONE_OLD("3"),
        # /*** 更换手机号-新手机号*/PHONE_NEW("4"),/*** 修改密码*/UPDATE_PASSWORD("5"),/*** 设备认证*/DEVICE("6"),
        # /*** 绑定第三方登录短信验证*/BIND_DEVICE("7");
        """发送短信"""
        response_getdata = send_code(url_send_code, headers, phone, smsCode)
        # print(response_getdata.json())
        # 发送短信接口成功
        if response_getdata.json().get("code") == "000000":
            # 获取短信验证码
            verificationCode = response_getdata.json().get("data")

            # 获取密码并进行MD5加密
            password = pwd1
            pwd = get_md5(password)
            # 拼接body参数
            paylo1 = {
                # "loginPassword": pwd,
                "verificationCode": verificationCode,
                "phone": phone,
                "phoneArea": phoneArea
            }
            # 获取sign并把参数签名后通过sign1传出来
            sign1 = {"sign": get_sign(paylo1)}
            # 拼接payload参数
            payload1 = {}
            payload1.update(paylo1)
            payload1.update(sign1)

            payload = json.dumps(dict(payload1))
            """第一次登陆注册系统账户"""
            r = Requests(self.session).post(
                url=url_user_login_pwd, headers=headers, data=payload, title="第一次登陆注册系统账户"
            )

            j = r.json()
            # print(j)
            # 注册登陆手机号第一次登录需设置密码
            if j.get("code") == "010003" \
                    or j.get("msg") == "第一次登录，设置登录密码":

                # 获取businessAccessToke
                businessAccessToken = j.get("data").get("businessAccessToken")

                paylo = {
                    "loginPassword": pwd,
                    "businessAccessToken": businessAccessToken
                }
                sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
                payload1 = {}
                payload1.update(paylo)
                payload1.update(sign1)

                payload = json.dumps(dict(payload1))
                # 第一次登陆注册系统账户时设置登录密码
                r1 = Requests(self.session).post(
                    url=url_set_login_password, headers=headers, data=payload, title="第一次登陆注册系统账户时设置登录密码"
                )
                j_set_login_password = r1.json()
                # print(j_set_login_password)
                # 断言部分
                assert r1.status_code == 200
                assert j_set_login_password.get("code") == "000000"
                assert j_set_login_password.get("msg") == "ok"
                if "data" in j_set_login_password:
                    assert j_set_login_password.get("data").get("phone") == paylo1.get("phone")
                    assert j_set_login_password.get("data").get("phoneArea") == paylo1.get("phoneArea")
                    assert "token" in j_set_login_password.get("data")
                    assert "userId" in j_set_login_password.get("data")

                with open(BASE_DIR + r"/TestData/UserRelatedapiData/正常的手机号与密码.txt", "a", encoding="utf-8") as f:
                    f.write(f"{j_set_login_password.get('data').get('phone')}|{password}\n")

        else:
            raise AssertionError(f"{response_getdata.json()}")
