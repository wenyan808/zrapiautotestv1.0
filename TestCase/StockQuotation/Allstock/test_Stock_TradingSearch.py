# test_Stock_TradingSearch   交易时的股票搜索    /as_market/api/stock/view/v1/trading_search
"""
@File  ：test_Stock_TradingSearch.py
@Author: yishouquan
@Time  : 2020/8/02
@Desc  :  股票行情_交易时的股票搜索
"""
import json
import time

import allure
import pytest

from Common.getTestLoginToken import gettestLoginToken

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import HTTP, JSON_dev, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('交易时的股票搜索')
class TestStockTradingSearch():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        # login()  # 调用登录接口通过token传出来
        cls.url = HTTP + "/as_market/api/stock/view/v1/trading_search"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/AllStockData/test_Stock_TradingSearch.json"))
    def test_Stock_TradingSearch(self, info):
        # login()  # 调用登录接口通过token传出来
        headers = {}
        headers.update(JSON_dev)

        token = {"token": gettestLoginToken()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        ts = info.get("ts")  # 市场
        keyWord = info.get("keyWord")  # 关键字
        paylo = {
            "ts": ts,
            "keyWord": keyWord,
        }
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=self.url, headers=headers, data=payload, title="交易时的股票搜索"
        )
        j = r.json()
        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("msg") == "ok"
            assert j.get("code") == "000000"
            if "data" in j:
                for i in range(len(j.get("data"))):
                    assert "code" in j.get("data")[i]
                    assert "name" in j.get("data")[i]
                    assert "id" in j.get("data")[i]
                    assert "type" in j.get("data")[i]
                    assert "suspension" in j.get("data")[i]  # suspension  股票状态：1-正常，2-停牌，3-复牌，4-待上市，5-美股暂停交易， 6-退市
                    assert j.get("data")[i].get("ts") == ts
        except:
            raise AssertionError(
                f"\n请求地址：{self.url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}")
