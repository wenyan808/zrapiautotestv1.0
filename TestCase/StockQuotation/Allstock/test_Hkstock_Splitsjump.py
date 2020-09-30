import json
import logging
import random

import allure
import pytest
import requests

from Common.login import login

from Common.show_sql import OperationSql
from Common.sign import get_sign
from Common.tools.read_write_json import write_json, get_json
from Common.tools.read_yaml import yamltoken
from glo import BASE_DIR, HTTP, JSON


# test_Hkstock_Splitsjump
# @pytest.mark.skip(reason="调试中，返回的结果是404")

@allure.feature('港股')
class TestHkstockSplitsjump:
    @classmethod
    def setup_class(cls) -> None:
        login()
        q = OperationSql("192.168.1.237", "root", "123456", "stock_market")
        ts_code = q.show_sql("select ts,code from t_stock_search where ts='HK';")
        random_stock = random.sample(ts_code, 500)
        ts_code_data = list(map(lambda code: {"ts": code[0], "code": code[1]}, random_stock))
        write_json(BASE_DIR + r"/TestData/HkstockSplitsjump.json", ts_code_data)

    @allure.story('拆合股-横幅(跳转)')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/HkstockSplitsjump.json"))
    def test_Hkstock_Splitsjumpp(self, info):
        url = HTTP + "/as_market/api/hk/splits/v1/jump"
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
                assert "code" in j.get("data")
                assert "type" in j.get("data")
                assert "name" in j.get("data")
                assert "content" in j.get("data")


            else:
                logging.info("data是空的集合")

        else:
            logging.info("无data数据")

