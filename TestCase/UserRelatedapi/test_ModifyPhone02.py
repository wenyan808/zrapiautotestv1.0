# test_ModifyPhone02

"""
@File  ：test_Registration.py
@Author: yishouquan
@Time  : 2020/7/26
@Desc  : 第一次登陆注册系统账户
"""

import json
import logging

import allure
import pytest

from Business.Urlpath.UrlPath_userlogin import UrlPath_send_code, UrlPath_modify_phone_v1, UrlPath_modify_phone_v2
from Common.getTestLoginToken import getlogintoken
from Common.register_common import get_registerno
from Common.send_code import send_code
from Common.sign import get_sign

from Common.requests_library import Requests
# from Common.tools.md5 import get_md5
from Common.tools.read_write_json import get_json, write_json

from Common.tools.unique_text import get_unique_phone

from glo import JSON_dev, HTTP, BASE_DIR, countryCode, pwd1, phoneArea, newPhoneArea


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('用户相关接口-修改手机号-当前使用手机号验证')
class TestModifyPhone02():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        # 生成新的手机号并写入到oldphone.json文件中
        paylonewphone = [{"phone": list(get_registerno())[0]}]
        # print(paylonewphone)
        write_json(BASE_DIR + r"/TestData/UserRelatedapiData/oldPhone.json", paylonewphone)

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('oldphone',
                             get_json(BASE_DIR + r"/TestData/UserRelatedapiData/oldPhone.json"))
    def test_ModifyPhone02(self, oldphone):
        # url管理
        url_send_code = HTTP + UrlPath_send_code
        url_modify_phone_v1 = HTTP + UrlPath_modify_phone_v1
        url_modify_phone_v2 = HTTP + UrlPath_modify_phone_v2
        # 从oldPhone.json文件中获取手机号
        phone = oldphone.get("phone")
        password = pwd1
        # 获取不重复手机号码以158开头的
        newPhone = get_unique_phone()
        paylonewname = [{"phone": newPhone}]
        # 写入到oldPhone.json文件中并替换掉旧的手机号
        write_json(BASE_DIR + r"/TestData/UserRelatedapiData/oldPhone.json", paylonewname)
        # 获取登录的token
        headers_token = getlogintoken(phone, password, phoneArea)
        # 获取JSON2和登录token参数并update到自定义headers中
        headers = {}
        headers.update(JSON_dev)
        token = {"token": headers_token}
        headers.update(token)  # 将token更新到headers参数中
        """发送短信—当前手机"""
        # 将smsCode传入的值写死
        smsCode = "3"  # /*** 登录*/LOGIN("1"),/*** 忘记密码*/FORGET("2"),/*** 更换手机号-旧手机号*/PHONE_OLD("3"),
        # /*** 更换手机号-新手机号*/PHONE_NEW("4"),/*** 修改密码*/UPDATE_PASSWORD("5"),/*** 设备认证*/DEVICE("6"),
        # /*** 绑定第三方登录短信验证*/BIND_DEVICE("7");

        response_getdata = send_code(url_send_code, headers, phone, smsCode)
        # print(response_getdata.json())
        verificationCode = response_getdata.json().get("data")
        # url1 = HTTP + "/as_user/api/user_account/v1/modify_phone_v1"
        paylo = {
            "verificationCode": verificationCode,
            "phone": phone,
            "phoneArea": phoneArea
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload2 = {}
        payload2.update(paylo)
        payload2.update(sign1)

        payload0 = json.dumps(dict(payload2))

        r_modify_phone_v1 = Requests(self.session).post(
            url=url_modify_phone_v1, headers=headers, data=payload0, title="修改手机号-当前使用手机号验证"
        )

        j_modify_phone_v1 = r_modify_phone_v1.json()
        # print(j)
        """发送短信—新手机号"""
        smsCode1 = "4"  # /*** 登录*/LOGIN("1"),/*** 忘记密码*/FORGET("2"),/*** 更换手机号-旧手机号*/PHONE_OLD("3"),
        # /*** 更换手机号-新手机号*/PHONE_NEW("4"),/*** 修改密码*/UPDATE_PASSWORD("5"),/*** 设备认证*/DEVICE("6"),
        # /*** 绑定第三方登录短信验证*/BIND_DEVICE("7");
        response1_getdata1 = send_code(url_send_code, headers, newPhone, smsCode1)
        newVerificationCode = response1_getdata1.json().get("data")
        businessAccessToken = j_modify_phone_v1.get("data").get('businessAccessToken')
        # print(businessAccessToken)

        paylo = {
            "businessAccessToken": businessAccessToken,
            "newPhone": newPhone,
            "newVerificationCode": newVerificationCode,
            "newPhoneArea": newPhoneArea
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload4 = {}
        payload4.update(paylo)
        payload4.update(sign1)

        payload02 = json.dumps(dict(payload4))

        r_modify_phone_v2 = Requests(self.session).post(
            url=url_modify_phone_v2, headers=headers, data=payload02, title="修改手机号-新手机号验证"
        )
        j_modify_phone_v2 = r_modify_phone_v2.json()

        assert r_modify_phone_v2.status_code == 200
        try:
            assert j_modify_phone_v2.get("code") == "000000"
            assert j_modify_phone_v2.get("msg") == "ok"
        except:
            assert j_modify_phone_v2.get("code") == "010017"
            assert j_modify_phone_v2.get("msg") == "新手机号不能于原手机号相同"
        # else:
        #     raise AssertionError(
        #         f"\n请求地址：{url_modify_phone_v2}"
        #         f"\nbody参数：{payload02}"
        #         f"\n请求头部参数：{headers}"
        #         f"\n返回数据结果：{j_modify_phone_v2}"
        #     )
