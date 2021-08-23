# test_HSOrder_EntrustWithdraw          撤单            /as_trade/api/order/v1/entrust_withdraw
import json

import allure

from Common.Accountcommon.accountAuth import AccountAuth

from Common.sign import get_sign

from Common.requests_library import Requests


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_撤单')
class TestHSOrderEntrustWithdraw():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        cls.http = list(AccountAuth())[-1]
        cls.url = cls.http + "/as_trade/api/order/v1/entrust_enter"
        cls.url1 = cls.http + "/as_market/api/stock_price/v1/get_prices"
        cls.url2 = cls.http + "/as_trade/api/order/v1/entrust_withdraw"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_HSOrder_EntEntrustWithdraw(self):
        # 拼装参数
        headers = list(AccountAuth())[1]  # 将柜台token赋值到headers
        # print(headers)

        ts = "HK"  # 市场
        code = "00700"  # 股票代码
        type1 = 2  # 这里写死证券类型 2：股票
        entrustProp = "ELO"  # 委托属性，港股支持 LO,ELO 美股和A股支持LO AO("AO", "竞价单"),
        # LO("LO", "限价单"),MO("MO","市价单"),ALO("ALO", "竞价限价单"),
        # ELO("ELO", "增强限价单"),SLO("SLO", "特别限价单"),ODD("ODD", "碎股交易"),

        paylo9 = {
            "stockVos": [{
                "code": code,
                "ts": ts,
                "type": type1
            }]
        }
        sign1 = {"sign": get_sign(paylo9)}  # 把参数签名后通过sign1传出来
        payload8 = {}
        payload8.update(paylo9)
        payload8.update(sign1)

        payload9 = json.dumps(dict(payload8))

        r_price = Requests(self.session).post(
            url=self.url1, headers=headers, data=payload9, title="查询股票价格数据"
        )

        k_price = r_price.json()
        # print(k_price)

        entrustPrice = k_price.get("data")[0].get("last")  # 价格
        entrustAmount = 100  # 数量(这里写死1手)
        entrustBs = "1"  # 买卖方向(1-买；2-卖)
        paylo = {
            "ts": ts,
            "code": code,
            "entrustProp": entrustProp,
            "entrustPrice": entrustPrice,
            "entrustAmount": entrustAmount,
            "entrustBs": entrustBs
        }

        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload2 = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=self.url, headers=headers, data=payload2, title="下单"
        )

        k_order = r.json()
        # print(k_order)

        orderTxnReference = k_order.get("data").get("orderTxnReference")
        paylo5 = {
            "orderTxnReference": orderTxnReference
        }
        sign1 = {"sign": get_sign(paylo5)}  # 把参数签名后通过sign1传出来
        payload6 = {}
        payload6.update(paylo5)
        payload6.update(sign1)

        payload7 = json.dumps(dict(payload6))

        r_data = Requests(self.session).post(
            url=self.url2, headers=headers, data=payload7, title="撤单"
        )

        j = r_data.json()
        # print(j)
        assert r_data.status_code == 200
        try:
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
        except:
            assert j.get("code") == "932112"
            assert j.get("msg") == "当前状态不允许撤单"
        else:
            raise AssertionError(
                f"\n请求地址：{self.url2}"
                f"\nbody参数：{payload7}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}"
            )
