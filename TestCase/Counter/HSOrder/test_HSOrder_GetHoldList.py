# test_HSOrder_GetHoldList    持仓列表          /as_trade/api/order/v1/get_hold_list
import json

import allure
import pytest

from Common.Accountcommon.accountAuth import AccountAuth

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_持仓列表')
class TestHSOrderGetHoldList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR +
                                      r"/TestData/Counterdata/HSOrderdata/"
                                      r"test_HSOrder_GetHoldListdata.json"))
    def test_HSOrder_GetHoldList(self,info):
        http = list(AccountAuth())[-1]
        url = http + "/as_trade/api/order/v1/get_hold_list"

        headers = list(AccountAuth())[1]  # 将柜台token赋值到headers
        # print(headers)
        market = info.get("market")
        paylo = {"market":market}

        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload2 = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload2, title="持仓列表"
        )

        k = r.json()
        # print(k)
        assert r.status_code == 200
        if k.get("code") == "000000":
            assert k.get("code") == "000000"
            assert k.get("msg") == "ok"
        else:
            raise AssertionError(k)
