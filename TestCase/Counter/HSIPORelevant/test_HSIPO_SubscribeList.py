# test_HSIPO_SubscribeList   IPO可认购列表    /as_trade/api/ipo/v1/subscribe_list
import json

import allure
import pytest
from jsonschema import validate, draft7_format_checker, SchemaError, ValidationError

from Common.getTestLoginToken import gettestLoginToken
from Common.sign import get_sign

from Common.requests_library import Requests
from TestAssertions.CounterJsonSchemadata.HSIPORelevantSchema.SubscribeListSchema import SubscribeListSchema

from glo import http_dev, JSON_dev


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_IPO可认购列表')
class TestHSIPOSubscribeList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_HSIPO_SubscribeList(self):
        url = http_dev + "/as_trade/api/ipo/v1/subscribe_list"

        # 拼装参数
        headers = JSON_dev
        headers = headers
        headers1 = {}
        token = {"token": gettestLoginToken()}
        headers1.update(headers)
        headers1.update(token)  # 将token更新到headers
        # print(headers)

        body = {}

        sign1 = {"sign": get_sign(body)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(body)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers1, data=payload, title="IPO可认购列表"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        if j.get("code") == "000000":
            assert j.get("msg") == "ok"

            schema = j
            try:
                validate(instance=SubscribeListSchema, schema=schema, format_checker=draft7_format_checker)
            except SchemaError as e:
                return 1, f"验证模式schema出错：\n出错位置：{'--> '.join([i for i in e.path])}\n提示信息：{e.message}"
            except ValidationError as e:
                return 1, f"json数据不符合schema规定：\n出错字段：{'-->'.join([i for i in e.path])}\n提示信息：{e.message}"
            else:
                return 0, "success!"
        else:
            raise AssertionError(j)
