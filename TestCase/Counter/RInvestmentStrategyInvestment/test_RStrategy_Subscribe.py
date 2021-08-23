# test_RStrategy_Subscribe     订阅策略    /as_trade/api/strategy/v1/subscribe
import json

import allure
import pytest

from Common.getTestLoginToken import gettestLoginToken
from Common.sign import get_sign

from Common.requests_library import Requests

from glo import http, JSON_dev


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_订阅策略')
class TestRStrategySubscribe():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_RStrategy_Subscribe(self):
        url = http + "/as_trade/api/strategy/v1/list"
        url1 = http + "/as_trade/api/strategy/v1/subscribe"
        url2 = http + "/as_trade/api/strategy/v1/un_subscribe"
        # 拼装参数
        headers = {}
        headers.update(JSON_dev)

        headers1 = {}
        token = {"token": gettestLoginToken()}
        headers1.update(headers)
        headers1.update(token)  # 将token更新到headers
        # print(headers)
        paylo5 = {}
        sign1 = {"sign": get_sign(paylo5)}  # 把参数签名后通过sign1传出来
        payload7 = {}
        payload7.update(paylo5)
        payload7.update(sign1)

        payload4 = json.dumps(dict(payload7))

        r_list = Requests(self.session).post(
            url=url, headers=headers1, data=payload4, title="R智投列表"
        )

        k_list = r_list.json()
        # print(k_list)
        combinationNo = k_list.get("data")[0].get("combinationNo")
        paylo = {
            "combinationNo": combinationNo
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url1, headers=headers1, data=payload, title="订阅策略"
        )

        k = r.json()
        # print(k)

        r1 = Requests(self.session).post(
            url=url2, headers=headers1, data=payload, title="取消订阅策略"
        )

        R = r1.json()

        assert r.status_code == 200
        if k.get("code") == "000000":
            assert k.get("code") == "000000"
            assert k.get("msg") == "ok"
        else:
            raise AssertionError(k)
