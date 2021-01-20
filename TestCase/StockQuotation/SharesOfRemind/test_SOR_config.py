# test_SOR_config
import json
import random

import allure
import pytest
import requests

from Common.login import login
from Common.show_sql import showsql

from Common.sign import get_sign
from Common.tools.read_write_json import get_json, write_json

from Common.tools.read_yaml import yamltoken
from glo import HTTP, JSON, BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('股价提醒')
class TestSORconfig:
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

    @allure.story('股价提醒配置')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/test_SOR_config.json"))
    def test_SOR_config(self, info):
        # pass
        url = HTTP + "/as_market/api/price_notify/v1/config"
        headers = JSON

        # 拼装参数
        # paylo = {}
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