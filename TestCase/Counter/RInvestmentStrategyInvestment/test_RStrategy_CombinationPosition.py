# test_RStrategy_CombinationPosition     一键跟投-组合仓位   /as_trade/api/strategy/v1/combination_position
import json

import allure
import pytest

from Common.getTestLoginToken import gettestLoginToken
from Common.sign import get_sign

from Common.requests_library import Requests

from glo import http, JSON_dev


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_一键跟投-组合仓位')
class TestRStrategyStrategyDetai():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_RStrategy_StrategyDetai(self):
        url = http + "/as_trade/api/strategy/v1/list"
        url1 = http + "/as_trade/api/strategy/v1/combination_position"
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
        payloa = {
            "combinationNo": combinationNo
        }
        sign1 = {"sign": get_sign(payloa)}  # 把参数签名后通过sign1传出来
        payload2 = {}
        payload2.update(payloa)
        payload2.update(sign1)

        payload3 = json.dumps(dict(payload2))

        r = Requests(self.session).post(
            url=url1, headers=headers1, data=payload3, title="一键跟投-组合仓位"
        )

        k = r.json()
        # print(k)

        assert r.status_code == 200
        if k.get("code") == "000000":
            assert k.get("code") == "000000"
            assert k.get("msg") == "ok"
        else:
            raise AssertionError(k)

