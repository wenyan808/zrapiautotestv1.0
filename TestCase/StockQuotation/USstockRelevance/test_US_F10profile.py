import json
import logging
import random

import allure
import pytest
import requests

from Common.login import login
from Common.show_sql import OperationSql
from Common.sign import get_sign
from Common.tools.read_write_json import get_json, write_json
from Common.tools.read_yaml import yamltoken
from glo import HTTP, JSON, BASE_DIR


@pytest.mark.skip(reason="调试中 ")

@allure.feature('美股相关')
class test_USF10profile:
    @classmethod
    def setup_class(cls) -> None:
        login()
        q = OperationSql("192.168.1.237", "root", "123456", "stock_market")
        ts_code = q.show_sql("select ts,code from t_stock_search where ts='US';")
        # print(ts_code)
        random_stock = random.sample(ts_code, 1)
        ts_code_data = list(map(lambda code: {"ts": code[0], "code": code[1]}, random_stock))
        write_json(BASE_DIR + r"/TestData/US_F10profile.json", ts_code_data)

    @allure.story('F10简况')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/hsgtis_lgt.json"))
    def test_US_f10profile(self, info):
        url = HTTP + "/as_market/api/us/f10/v1/profile"
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