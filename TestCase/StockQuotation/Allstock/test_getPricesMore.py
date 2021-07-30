import json
import logging
import random

import allure
import pytest
import requests

from Common.login import login


from Common.show_sql import showsql
from Common.sign import get_sign
from Common.tools.read_write_json import get_json, write_json
from Common.tools.read_write_yaml import yamltoken
from glo import BASE_DIR, HTTP, JSON


# @pytest.mark.skip(reason="调试中")
@allure.feature('拆合股')
class TestgetPricesMore:
    @classmethod
    def setup_class(cls) -> None:
        login()
        ts_code = showsql(
            '192.168.1.237', 'root', '123456', 'stock_market',
            "select ts,code from t_stock_search where ts='HK' or ts='US';"
            )
        # print(ts_code)
        random_stock = random.sample(ts_code, 500)
        ts_code_data = list(map(lambda code: {"ts": code[0], "code": code[1]}, random_stock))
        write_json(BASE_DIR + r"/TestData/AllStockData/getPricesMore.json", ts_code_data)



    @allure.story('查询更多股票信息')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/AllStockData/getPricesMore.json"))
    def test_getPricesMore_all(self,info):
        # pass
        url = HTTP + "/as_market/api/stock_splits/v1/list"
        headers = {}
        headers.update(JSON)

        # 拼装参数

        paylo = info
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        # 调用登录接口通过token传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        # print(token)
        # print(type(token))

        token1 = yamltoken()
        token = {"token": token1}
        headers.update(token)
        # print(headers)
        payload = json.dumps(dict(payload1))

        r = requests.post(url=url, headers=headers, data=payload)
        # 断言
        j = r.json()
        # print(j)

        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        if "data" in j:
            if len(j.get("data")) != 0:
                # pass
                for i in range(len(j.get("data"))):
                    assert "content" in j.get("data")[i]
                    assert "date" in j.get("data")[i]

            else:
                logging.info("data是空的集合")

        else:
            logging.info("无data数据")