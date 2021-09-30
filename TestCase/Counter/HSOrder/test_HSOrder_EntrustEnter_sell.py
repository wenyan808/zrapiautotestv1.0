# test_HSOrder_EntrustEnter     下单     /as_trade/api/order/v1/entrust_enter
import json

import allure
import pytest

from Common.Accountcommon.accountAuth import AccountAuth
from Common.get_payload_headers import get_payload

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('柜台app_下单(卖)')
class TestHSOrderEntrustEntersell():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        # stock = showsql(
        #     "192.168.1.237", "root", "123456", "stock_market",
        #     "select ts,code,type from t_stock_search where type= 2 and ts ='SH' or ts='SZ';"
        # )
        # random_stock = random.sample(stock, 10)
        # stock_data = list(map(lambda code: {"ts": code[0], "code": code[1], "type": code[2]}, random_stock))
        # write_json(BASE_DIR + r"/TestData/Counterdata/HSOrderdata/test_HSOrder_EntrustEnterdata.json", stock_data)
        # # print(ts_code_data)

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(
                                 BASE_DIR + r"/TestData/Counterdata/HSOrderdata/test_HSOrder_EntrustEnter_sell.json"))
    def test_HSOrder_EntrustEnter_sell(self, info):
        http = list(AccountAuth())[-1]
        url = http + "/as_trade/api/order/v1/entrust_enter"
        url1 = http + "/as_market/api/stock_price/v1/get_prices"
        url_get_hold_list = http + "/as_trade/api/order/v1/get_hold_list"
        # 拼装参数
        headers = list(AccountAuth())[1]  # 将柜台token更新到headers
        # print(headers)
        ts = info.get("ts")  # 市场
        # ts = "HK"
        code = info.get("code")  # 股票代码
        # code = "00700"
        type1 = info.get("type")  # 1:指数 2：股票  3：基金
        # type1 = 2
        paylo9 = {
            "stockVos": [{
                "code": code,
                "ts": ts,
                "type": type1
            }]
        }
        payload9 = get_payload(paylo9)

        r_price = Requests(self.session).post(
            url=url1, headers=headers, json=payload9, title="查询股票价格数据"
        )

        k_price = r_price.json()
        # print(k_price)
        market = info.get("market")

        paylo1 = {"market": market}

        payload0 = get_payload(paylo1)

        r_get_hold_list = Requests(self.session).post(
            url=url_get_hold_list, headers=headers, json=payload0, title="持仓列表"
        )

        k_get_hold_list = r_get_hold_list.json()
        # print(k_get_hold_list)

        entrustPrice = round(k_price.get("data")[0].get("last"),
                             3)  # 价格,保留小数点后三位  舍入运算，使用内置的 round(value, ndigits) 函数
        # print(entrustPrice)

        entrustProp = "ODD"  # 委托属性，港股支持 LO,ELO 美股和A股支持LO AO("AO", "竞价单"),
        # LO("LO", "限价单"),MO("MO","市价单"),ALO("ALO", "竞价限价单"),
        # ELO("ELO", "增强限价单"),SLO("SLO", "特别限价单"),ODD("ODD", "碎股交易"),

        entrustAmount = 1  # 数量(这里写死1)
        entrustBs = "2"  # 买卖方向(1-买；2-卖)
        paylo = {
            "ts": ts,
            "code": code,
            "entrustPrice": entrustPrice,
            "entrustProp": entrustProp,
            "entrustAmount": entrustAmount,
            "entrustBs": entrustBs
        }

        payload2 = get_payload(paylo)
        # print(payload2)

        r = Requests(self.session).post(
            url=url, headers=headers, json=payload2, title="下单(卖)"
        )

        k = r.json()
        # print(k)
        assert r.status_code == 200
        try:
            assert k.get("msg") == "ok"
            assert k.get("code") == "000000"
        except:
            raise AssertionError(f"\n请求地址：{url}"
                                 f"\nbody参数：{payload2}"
                                 f"\n请求头部参数：{headers}"
                                 f"\n返回数据结果：{k}")
