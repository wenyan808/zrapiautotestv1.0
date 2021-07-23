# test_RStrategy_GetCombinationHoldList   恒生3.0-查用户的策略持仓      /as_trade/api/order/v1/get_combination_hold_list
import json

import allure
import pytest

from Common.Accountcommon.accountAuth import AccountAuth

from Common.sign import get_sign

from Common.requests_library import Requests


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_恒生3.0-查用户的策略持仓')
class TestRStrategyGetCombinationHoldList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_RStrategy_GetCombinationHoldList(self):
        http = list(AccountAuth())[-1]
        url = http + "/as_trade/api/strategy/v1/list"
        url1 = http + "/as_trade/api/order/v1/get_combination_hold_list"
        headers = list(AccountAuth())[1]
        # print(headers)
        paylo5 = {}
        sign1 = {"sign": get_sign(paylo5)}  # 把参数签名后通过sign1传出来
        payload7 = {}
        payload7.update(paylo5)
        payload7.update(sign1)

        payload4 = json.dumps(dict(payload7))

        r_list = Requests(self.session).post(
            url=url, headers=headers, data=payload4, title="R智投列表"
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
            url=url1, headers=headers, data=payload3, title="恒生3.0-查用户的策略持仓"
        )

        k = r.json()
        # print(k)

        assert r.status_code == 200
        if k.get("code") == "000000":
            assert k.get("code") == "000000"
            assert k.get("msg") == "ok"
        else:
            raise AssertionError(k)
