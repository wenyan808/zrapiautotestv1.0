# test_HSOrder_EntrustEnter     下单     /as_trade/api/order/v1/entrust_enter
import json

import allure
import pytest

from Common.Accountcommon.accountAuth import AccountAuth

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('柜台app_下单')
class TestHSOrderEntrustEnter():
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
                                 BASE_DIR + r"/TestData/Counterdata/HSOrderdata/test_HSOrder_EntrustEnterdata.json"))
    def test_HSOrder_EntrustEnter(self, info):
        http = list(AccountAuth())[-1]
        url = http + "/as_trade/api/order/v1/entrust_enter"
        url1 = http + "/as_market/api/stock_price/v1/get_prices"
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
        sign1 = {"sign": get_sign(paylo9)}  # 把参数签名后通过sign1传出来
        payload8 = {}
        payload8.update(paylo9)
        payload8.update(sign1)

        payload9 = json.dumps(dict(payload8))

        r_price = Requests(self.session).post(
            url=url1, headers=headers, data=payload9, title="查询股票价格数据"
        )

        k_price = r_price.json()
        # print(k_price)

        entrustPrice = round(k_price.get("data")[0].get("last") - 0.5,
                             3)  # 价格,保留小数点后三位  舍入运算，使用内置的 round(value, ndigits) 函数
        # print(entrustPrice)

        entrustProp = "LO"  # 委托属性，港股支持 LO,ELO 美股和A股支持LO AO("AO", "竞价单"),
        # LO("LO", "限价单"),MO("MO","市价单"),ALO("ALO", "竞价限价单"),
        # ELO("ELO", "增强限价单"),SLO("SLO", "特别限价单"),ODD("ODD", "碎股交易"),

        entrustAmount = 100  # 数量(这里写死1手)
        entrustBs = "1"  # 买卖方向(1-买；2-卖)
        paylo = {
            "ts": ts,
            "code": code,
            "entrustPrice": entrustPrice,
            "entrustProp": entrustProp,
            "entrustAmount": entrustAmount,
            "entrustBs": entrustBs
        }

        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload2 = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload2, title="下单"
        )

        k = r.json()
        # print(k)
        assert r.status_code == 200
        if info.get("assert_type") == "0":
            assert k.get("code") == "000000"
            assert k.get("msg") == "ok"

        elif info.get("assert_type") == "1":
            # print(k)
            assert k.get("msg") == "下单失败"
            assert k.get("code") == "350001"

        elif info.get("assert_type") == "2":
            # print(k)
            assert k.get("msg") == "客户存在创业板交易控制，不允许委托"
            assert k.get("code") == "932155"

        elif info.get("assert_type") == "3":
            # print(k)
            assert k.get("msg") == "价格信息不存在"
            assert k.get("code") == "935012"

        elif info.get("assert_type") == "4":
            # print(k)
            assert k.get("msg") == "证券代码信息不存在"
            assert k.get("code") == "935006"

        elif info.get("assert_type") == "5":
            # print(k)
            assert k.get("msg") == "该账户绑定的BCAN码状态不正确"
            assert k.get("code") == "932132"
        elif info.get("assert_type") == "6":
            # print(k)
            assert k.get("msg") == "该股票不属于陆股通标的范围"
            assert k.get("code") == "350405"
        # elif info.get("assert_type") == "1":
        #     assert k.get("code") == "932103"
        #     assert k.get("msg") == "当前时间不允许此类证券交易"

        else:
            raise AssertionError(k)