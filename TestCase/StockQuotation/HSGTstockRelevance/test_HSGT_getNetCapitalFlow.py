import json
import logging
import random
# import time

import allure
import pytest
import requests

from Common.login import login
from Common.show_sql import showsql
from Common.sign import get_sign
from Common.tools.read_write_json import write_json, get_json
from Common.tools.read_yaml import yamltoken
from glo import BASE_DIR, HTTP, JSON


# test_HSGT_getNetCapitalFlow
# @pytest.mark.skip(reason="调试中，返回的结果是404")
@allure.feature('沪深港通')
class TestgetNetCapitalFlow:
    @classmethod
    def setup_class(cls) -> None:
        login()
        ts_code = showsql(
            "192.168.1.237", "root", "123456", "stock_market",
            "select ts,code from t_stock_search where ts='HK' or ts='SH' or ts='SZ';"
        )
        random_stock = random.sample(ts_code, 500)
        ts_code_data = list(map(lambda code: {"ts": code[0], "code": code[1]}, random_stock))
        write_json(BASE_DIR + r"/TestData/test_HSGTData/getNetCapitalFlow.json", ts_code_data)
        # print(ts_code_data)

    @allure.story('沪深港通单只证券累计资金净流向')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/test_HSGTData/getNetCapitalFlow.json"))
    def test_HSGT_getNetCapitalFlow(self, info):
        # pass
        url = HTTP + "/as_market/api/hsgt/v1/get_net_capital_flow"
        headers = JSON

        # 拼装参数

        paylo = info
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
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        if "data" in j:
            if len(j.get("data")) != 0:
                # pass
                assert "date" in j.get("data")
                assert "list" in j.get("data")
                if len(j.get("data").get("list")) != 0:
                    for i in range(len(j.get("data").get("list"))):
                        # pass
                        assert "day" in j.get("data").get("list")[i]
                        assert "netStockVolume" in j.get("data").get("list")[i]
                        assert "netCapitalFlow" in j.get("data").get("list")[i]
                        assert "flowStockRatio" in j.get("data").get("list")[i]

            else:
                logging.info("data是空的集合")

        else:
            logging.info("无data数据")
