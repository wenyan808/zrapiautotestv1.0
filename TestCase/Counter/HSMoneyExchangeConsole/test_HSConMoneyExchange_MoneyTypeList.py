# test_HSConMoneyExchange_MoneyTypeList     获取币种汇率列表       /api/con_rate/v1/money_type_list
import json


import allure
import pytest

from Common.getConsoleLogin import getConsoleLogin_token
from Common.sign import get_sign

from Common.requests_library import Requests

from glo import console_JSON, console_HTTP


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('恒生3.0-货币兑换(console)_获取币种汇率列表')
class TestHSConMoneyExchangeMoneyTypeList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        cls.url = console_HTTP + "/api/con_rate/v1/money_type_list"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_HSConMoneyExchange_MoneyTypeList(self):
        # 拼装参数
        header = console_JSON
        header = header
        headers = {}
        headers.update(header)

        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)

        paylo = {}

        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=self.url, headers=headers, data=payload, title="获取币种汇率列表"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        if j.get("code") == "000000":
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
        else:
            raise AssertionError(j)
