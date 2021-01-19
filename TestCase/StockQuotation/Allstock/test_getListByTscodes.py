# test_getListByTscodes
import json
import logging
import random

import allure
import pytest
import requests

from Common.login import login
from Common.show_sql import showsql

from Common.sign import get_sign
from Common.tools.read_write_json import write_json, get_json

from Common.tools.read_yaml import yamltoken
from glo import HTTP, JSON, BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('公共分类')
class TestGetListByTscodes:
    @classmethod
    def setup_class(cls) -> None:
        login()
        ts_code = showsql(
            '192.168.1.237', 'root', '123456', 'stock_market',
            "select ts,code,name from t_stock_search where ts='HK';"
        )
        random_stock = random.sample(ts_code, 100)
        stock_data = list(map(lambda code: {"ts": code[0], "code": code[1]}, random_stock))
        write_json(BASE_DIR + r"/TestData/test_getListByTscodes.json", stock_data)

    @allure.story('获取多支股票详情')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/test_getListByTscodes.json"))
    def test_getListByTscodes(self, info):
        # pass
        url = HTTP + "/as_market/api/stock_basic/v1/get_list_by_tscodes"
        headers = JSON

        # 拼装参数
        paylo = {
            "requstList": [
                {
                    "ts": info.get("ts"),
                    "code": info.get("code")
                }
            ]
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
        # print(payload)
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
                        assert "name" in j.get("data")[i]
                        assert j.get("data")[i].get("ts") == paylo.get("requstList")[0].get("ts")
                        assert "hands" in j.get("data")[i]
                        assert "last" in j.get("data")[i]
                        assert j.get("data")[i].get("code") == paylo.get("requstList")[0].get("code")
                        assert "type" in j.get("data")[i]
                        assert "suspension" in j.get("data")[i]
                else:
                    logging.info("data参数存在但data为空list")
            else:
                logging.info("无data参数")
