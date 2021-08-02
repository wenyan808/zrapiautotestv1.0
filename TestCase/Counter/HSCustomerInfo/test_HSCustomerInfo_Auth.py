# test_HSCustomerInfo_Auth            登录认证      /as_trade/api/account/v1/auth
import json

import allure
import pytest
from jsonschema import validate, draft7_format_checker, SchemaError, ValidationError

from Common.assertapi import assert_data, jsonschema_assert
from Common.getTestLoginToken import gettestLoginToken
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_yaml import yamlconfig
from TestAssertions.CounterJsonSchemadata.HSCustomerInfo.AuthSchema import authSchema

from glo import http, JSON_dev, user_password, userId2


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_登录认证')
class TestHSCustomerInfoAuth():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        cls.url = http + "/as_trade/api/account/v1/auth"
        cls.url1 = http + "/as_trade/api/account/v1/info"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_HSCustomerInfo_Auth(self):
        # 拼装参数
        headers = {}
        headers.update(JSON_dev)

        headers1 = {}
        token = {"token": gettestLoginToken()}
        headers1.update(headers)
        headers1.update(token)  # 将token更新到headers
        # print(headers)
        paylo = {}

        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload2 = json.dumps(dict(payload1))

        r_info = Requests(self.session).post(
            url=self.url1, headers=headers1, data=payload2, title="获取客户证券等信息"
        )

        k = r_info.json()
        clientId = k.get("data").get("clientId")
        if yamlconfig("flag"):
            password = "123456"
        else:
            password = "111111"

        body = {
            "clientId": clientId,
            "password": password
        }

        sign1 = {"sign": get_sign(body)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(body)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=self.url, headers=headers1, data=payload, title="登录认证"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        if j.get("code") == "000000":
            if len(j.get("data")) != 0:
                assert j.get("data").get("userId") == userId2
                assert j.get("data").get("forceChangePwd") == 0
            jsonschema_assert(j.get("code"), j.get("msg"), j, authSchema)
        else:
            raise AssertionError(j)
