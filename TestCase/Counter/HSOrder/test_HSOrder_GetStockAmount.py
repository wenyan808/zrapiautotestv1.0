# test_HSOrder_GetStockAmount    获取可卖数量            /as_trade/api/order/v1/get_stock_amount
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
class TestHSOrderGetStockAmount():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR +
                                      r"/TestData/Counterdata/HSOrderdata/"
                                      r"test_HSOrder_GetStockAmountdata.json"))
    def test_HSOrder_GetStockAmount(self, info):
        http = list(AccountAuth())[-1]
        url = http + "/as_trade/api/order/v1/get_stock_amount"

        # 拼装参数
        headers = list(AccountAuth())[1]  # 将柜台token赋值到headers
        # print(headers)

        ts = info.get("ts")  # 市场类别
        code = info.get("code")  # 证券code
        entrustProp = info.get("entrustProp")  # # 委托属性，港股支持 LO,ELO 美股和A股支持LO AO("AO", "竞价单"),
        # LO("LO", "限价单"),MO("MO","市价单"),ALO("ALO", "竞价限价单"),
        # ELO("ELO", "增强限价单"),SLO("SLO", "特别限价单"),ODD("ODD", "碎股交易"),

        paylo = {
            "ts": ts,
            "code": code,
            "entrustProp": entrustProp
        }

        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload2 = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload2, title="获取可卖数量"
        )

        k = r.json()
        # print(k)
        assert r.status_code == 200
        if k.get("code") == "000000":

            assert k.get("msg") == "ok"
        elif k.get("code") == "935006":
            assert k.get("msg") == "证券代码信息不存在"
        else:
            raise AssertionError(k)
