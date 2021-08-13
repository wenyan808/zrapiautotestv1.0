# test_AccountApp_DerivativeConfirm         衍生品风险交易披露确认     /as_user/api/client/v1/derivative_confirm
"""
@File  ：test_AccountApp_DerivativeConfirm.py
@Author: yishouquan
@Time  : 2020/8/12
@Desc  :  衍生品风险交易披露确认
"""
import json
import time

import allure
import pytest

from Common.Accountcommon.getAccountConsoleList import getAccountConsoleList
from Common.getConsoleLogin import getConsoleLogin_token
from Common.getTestLoginToken import getUserLogincodeToken

from Common.sign import get_sign

from Common.requests_library import Requests


from glo import HTTP, JSON_dev,loginAccount_phone


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('衍生品风险交易披露确认')
class TestAccountAppDerivativeConfirm():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        # login()  # 调用登录接口通过token传出来
        cls.url = HTTP + "/as_user/api/client/v1/derivative_confirm"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_AccountApp_DerivativeConfirm(self):

        headers = {}
        headers.update(JSON_dev)

        token = {"token": getUserLogincodeToken(loginAccount_phone)}
        headers.update(token)  # 将token更新到headers
        # print(headers)

        paylo = {
        }
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=self.url, headers=headers, data=payload, title="衍生品风险交易披露确认"
        )
        j = r.json()
        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("msg") == "ok"
            assert j.get("code") == "000000"

        except:
            raise AssertionError(
                f"\n请求地址：{self.url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}")

