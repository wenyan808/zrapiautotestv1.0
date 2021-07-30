# test_SOR_getbystock
import json
import random

import allure
import pytest
import requests

from Common.login import login
from Common.show_sql import showsql

from Common.sign import get_sign
from Common.tools.read_write_json import get_json, write_json

from Common.tools.read_write_yaml import yamltoken
from glo import HTTP, JSON, BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('股价提醒')
class TestSOGetbystock:
    @classmethod
    def setup_class(cls) -> None:
        login()
        # ts_code = showsql(
        #     "192.168.1.234", "zhuorui", "123456", "stock_market",
        #     "select ts,code from t_stock_search where etf_flag='Y';"
        # )
        # random_stock = random.sample(ts_code, 500)
        # ts_code_data = list(map(lambda code: {"ts": code[0], "code": code[1]}, random_stock))
        # write_json(BASE_DIR + r" /TestData/test_ETF_F10details.json", ts_code_data)

    @allure.story('查用户对某个股票的涨跌提醒配置')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/test_SOR_getbystock.json"))
    def test_SOR_getbystock(self, info):
        # pass
        url = HTTP + "/as_market/api/price_notify/v1/get_by_stock"
        headers = JSON

        # 拼装参数
        # paylo = {
        #     "ts": "US",
        #     "code": "AAPL",
        #     "type": 2
        # }
        paylo = info
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        # 调用登录接口通过token传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)
        headers = headers
        # print(token)

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
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        if "data" in j:
            if len(j.get("data")) != 0:
                assert "ts" in j.get("data")
                assert j.get("data").get("ts") == info.get("ts")
                assert "code" in j.get("data")
                assert j.get("data").get("code") == info.get("code")
                assert "type" in j.get("data")
                assert j.get("data").get("type") == info.get("type")
                assert "name" in j.get("data")
                assert "notifyRate" in j.get("data")
                assert "updateTime" in j.get("data")
                assert "list" in j.get("data")
                for i in range(len(j.get("data").get("list"))):
                    assert "compareType" in j.get("data").get("list")[i]
                    assert "threshold" in j.get("data").get("list")[i]
                    assert "status" in j.get("data").get("list")[i]
