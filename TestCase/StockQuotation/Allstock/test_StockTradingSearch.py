# test_StockTradingSearch
import json
import logging
import random

import allure
import pytest
import requests

from Common.get_time_stamp import TimeTostamp
from Common.login import login
from Common.show_sql import showsql

from Common.sign import get_sign
from Common.tools.read_write_json import write_json, get_json

from Common.tools.read_write_yaml import yamltoken
from glo import HTTP, JSON, BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('公共分类')
class TestNowSrverinfo:
    @classmethod
    def setup_class(cls) -> None:
        login()
        ts_code = showsql(
            '192.168.1.237', 'root', '123456', 'stock_market',
            "select ts,code,name from t_stock_search;"
        )
        random_stock = random.sample(ts_code, 500)
        stock_data = list(map(lambda code: {"ts": code[0], "code": code[1]}, random_stock))
        write_json(BASE_DIR + r"/TestData/AllStockData/test_StockTradingSearch.json", stock_data)

    @allure.story('交易时的股票搜索')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/AllStockData/test_StockTradingSearch.json"))
    def test_nowSrverinfo(self, info):
        # pass
        url = HTTP + "/as_market/api/stock/view/v1/trading_search"
        headers = JSON

        # 拼装参数
        paylo = {
            "ts": info.get("ts"),
            "keyWord": info.get("code")
        }
        # paylo = info
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        # 调用登录接口通过token传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)
        headers = headers
        # print(token)
        # print(type(token))

        token1 = yamltoken()
        token = {"token": token1}
        headers.update(token)
        # print(headers)
        payload = json.dumps(dict(payload1))
        # time.sleep(1)
        r = requests.post(url=url, headers=headers, data=payload)
        # 断言
        j = r.json()
        # print(j)
        assert r.status_code == 200
        if j.get("code") == "000000":
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
            if "data" in j:
                if len(j.get("data")) != 0:
                    for i in range(len(j.get("data"))):
                        assert "id" in j.get("data")[i]
                        assert "type" in j.get("data")[i]
                        assert j.get("data")[i].get("ts") == paylo.get("ts")
                        assert "code" in j.get("data")[i]
                        assert "name" in j.get("data")[i]
                        assert "suspension" in j.get("data")[i]
