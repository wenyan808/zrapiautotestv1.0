# test_ModifyLoginPassword02
"""
@File  ：test_ModifyLoginPassword02.py
@Author: yishouquan
@Time  : 2020/7/26
@Desc  :  修改手机号-新手机号验证
"""
import json
import logging

import allure
import pytest

from Business.Urlpath.UrlPath_userlogin import UrlPath_send_code, UrlPath_modify_login_password_v1, \
    UrlPath_modify_login_password_v2
from Common.getTestLoginToken import getlogintoken
from Common.send_code import send_code
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.md5 import get_md5
from Common.tools.read_write_json import get_json, write_json

from Common.tools.unique_text import get_unique_username

from glo import JSON_dev, HTTP, BASE_DIR, phoneArea, countryCode


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('用户相关接口-修改手机号-新手机号验证')
class TestModifyLoginPassword02():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        # cls.url = HTTP + "/as_notification/api/sms/v1/send_code",
        # cls.url1 = HTTP + "/as_user/api/user_account/v1/modify_login_password_v1"
        # cls.url2 = HTTP + "/as_user/api/user_account/v1/modify_login_password_v2"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('oldpassword',
                             get_json(BASE_DIR + r"/TestData/UserRelatedapiData/oldPassword.json"))
    def test_ModifyLoginPassword02(self, oldpassword):
        # 固定写死已登录的手机号
        phone = "15815425100"
        # 从oldPassword.json文件中获取登陆密码并赋值给password
        oldLoginPassword = oldpassword.get("LoginPassword")
        password = oldLoginPassword
        # 获取headers参数，先定义一个headers的空dict
        headers = {}
        # 将JSON2 update到headers参数中
        headers.update(JSON_dev)
        # 获取token，并将token update到headers参数中
        headers_token = getlogintoken(phone, password, phoneArea)
        # print(headers_token)
        token = {"token": headers_token}
        # print(type(token))
        headers.update(token)  # 将token更新到headers参数中

        newLoginPassword = get_unique_username(1)[0]  # 通过获取用户名做为账号的密码，get_unique_username(1)获取的结果是一个列表
        # newLoginPassword = "zr1234567"
        # oldLoginPassword, newLoginPassword = newLoginPassword, oldLoginPassword
        # 将list赋值给pwd
        pwd = [{"LoginPassword": newLoginPassword}]
        # 写入到oldPassword.json中，方便下次直接调取password
        write_json(BASE_DIR + r"/TestData/UserRelatedapiData/oldPassword.json", pwd)
        """发送短信"""
        smsCode = "5"  # /*** 登录*/LOGIN("1"),/*** 忘记密码*/FORGET("2"),/*** 更换手机号-旧手机号*/PHONE_OLD("3"),
        # /*** 更换手机号-新手机号*/PHONE_NEW("4"),/*** 修改密码*/UPDATE_PASSWORD("5"),/*** 设备认证*/DEVICE("6"),
        # /*** 绑定第三方登录短信验证*/BIND_DEVICE("7");
        url_send_code = HTTP + UrlPath_send_code
        response_getdata = send_code(url_send_code, headers, phone, smsCode)
        if "data" in response_getdata.json():
            verificationCode = response_getdata.json().get("data")
        else:
            verificationCode = "123456"
        """修改登录密码-第一步"""
        url_modify_login_password_v1 = HTTP + UrlPath_modify_login_password_v1
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

        r_modify_login_password_v1 = Requests(self.session).post(
            url=url_modify_login_password_v1, headers=headers, data=payload, title="修改登录密码-第一步（验证修改密码验证码）"
        )
        j_modify_login_password_v1 = r_modify_login_password_v1.json()
        # print(j_modify_login_password_v1)
        """修改登陆密码-第二步"""
        if j_modify_login_password_v1.get("code") == "000000" and j_modify_login_password_v1.get("msg") == "ok":
            businessAccessToken = j_modify_login_password_v1.get("data").get('businessAccessToken')
            # print(businessAccessToken)
            url_modify_login_password_v2 = HTTP + UrlPath_modify_login_password_v2
            paylo = {
                "oldLoginPassword": get_md5(oldLoginPassword),
                "businessAccessToken": businessAccessToken,
                "newLoginPassword": get_md5(newLoginPassword)
            }
            sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
            payload1 = {}
            payload1.update(paylo)
            payload1.update(sign1)

            payload = json.dumps(dict(payload1))

            r_modify_login_password_v2 = Requests(self.session).post(
                url=url_modify_login_password_v2, headers=headers, data=payload, title="修改登录密码-第二步"
            )
            j_modify_login_password_v2 = r_modify_login_password_v2.json()
            # print(j_modify_login_password_v2)
            assert r_modify_login_password_v2.status_code == 200
            try:
                assert j_modify_login_password_v2.get("code") == "000000"
                assert j_modify_login_password_v2.get("msg") == "ok"

            except:
                raise AssertionError(
                    f"\n请求地址：{url_modify_login_password_v2}"
                    f"\nbody参数：{payload}"
                    f"\n请求头部参数：{headers}"
                    f"\n返回数据结果：{j_modify_login_password_v2}"
                )
        else:
            raise AssertionError(f"修改登录密码-第一步（验证修改密码验证码）错误信息:{j_modify_login_password_v1}")
