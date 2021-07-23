# test_RStrategy_GetRHoldList      恒生3.0-查询客户持仓组合列表     /as_trade/api/order/v1/get_r_hold_list
import json

import allure
import pytest

from Common.Accountcommon.accountAuth import AccountAuth
from Common.sign import get_sign

from Common.requests_library import Requests


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_恒生3.0-查询客户持仓组合列表')
class TestRStrategyGetRHoldList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_RStrategy_GetRHoldList(self):
        http = list(AccountAuth())[-1]
        url = http + "/as_trade/api/order/v1/get_r_hold_list"
        # 拼装参数
        headers = list(AccountAuth())[1]

        paylo5 = {}
        sign1 = {"sign": get_sign(paylo5)}  # 把参数签名后通过sign1传出来
        payload7 = {}
        payload7.update(paylo5)
        payload7.update(sign1)

        payload4 = json.dumps(dict(payload7))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload4, title="恒生3.0-查询客户持仓组合列表"
        )

        k = r.json()
        # print(k)

        assert r.status_code == 200
        if k.get("code") == "000000":
            assert k.get("code") == "000000"
            assert k.get("msg") == "ok"
        else:
            raise AssertionError(k)
