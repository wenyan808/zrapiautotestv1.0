# test_HSCustomerInfo_Auth            登录认证      /as_trade/api/account/v1/auth
import json

import allure
import pytest
from jsonschema import validate, draft7_format_checker, SchemaError, ValidationError

from Common.getTestLoginToken import gettestLoginToken
from Common.sign import get_sign

from Common.requests_library import Requests
from TestAssertions.CounterJsonSchemadata.HSCustomerInfo.AuthSchema import authSchema

from glo import http, JSON_dev, user_password, userId2


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_登录认证')
class TestHSCustomerInfoAuth():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_HSCustomerInfo_Auth(self):
        url = http + "/as_trade/api/account/v1/auth"
        url1 = http + "/as_trade/api/account/v1/info"
        # 拼装参数
        headers = JSON_dev
        headers = headers
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
            url=url1, headers=headers1, data=payload2, title="获取客户证券等信息"
        )

        k = r_info.json()
        clientId = k.get("data").get("clientId")
        password = user_password

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
            url=url, headers=headers1, data=payload, title="登录认证"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        if j.get("code") == "000000":
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
            if len(j.get("data")) != 0:
                assert j.get("data").get("userId") == userId2
                assert j.get("data").get("forceChangePwd") == 0

            schema = j
            try:
                validate(instance=authSchema, schema=schema, format_checker=draft7_format_checker)
            except SchemaError as e:
                return 1, f"验证模式schema出错：\n出错位置：{'--> '.join([i for i in e.path])}\n提示信息：{e.message}"
            except ValidationError as e:
                return 1, f"json数据不符合schema规定：\n出错字段：{'-->'.join([i for i in e.path])}\n提示信息：{e.message}"
            else:
                return 0, "success!"

        else:
            raise AssertionError(j)
