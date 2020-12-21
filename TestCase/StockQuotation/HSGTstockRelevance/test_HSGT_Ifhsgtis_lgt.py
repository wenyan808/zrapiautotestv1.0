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


# @pytest.mark.skip(reason="调试中 ")

@allure.feature('陆股通')
class TestHSGTIfhsgtis_lgt:
    @classmethod
    def setup_class(cls) -> None:
        login()
        # q = OperationSql("192.168.1.237", "root", "123456", "stock_market")
        # ts_code = q.show_sql("select ts,code from t_stock_search where ts='SH' or ts='SZ';")
        # random_stock = random.sample(ts_code, 2)
        # cls.ts_code_data = json.dumps(list(map(lambda code: {"ts": code[0], "code": code[1]}, random_stock)))
        # print(cls.ts_code_data)
        # write_json(BASE_DIR + r"/TestData/hsgtis_lgt.json", cls.ts_code_data)

        q = OperationSql("192.168.1.237", "root", "123456", "stock_market")
        ts_code = q.show_sql("select ts,code from t_stock_search where ts='SH' or ts='SZ';")
        # print(ts_code)
        random_stock = random.sample(ts_code, 1)
        ts_code_data = list(map(lambda code: {"ts": code[0], "code": code[1]}, random_stock))
        write_json(BASE_DIR + r"/TestData/hsgtis_lgt.json", ts_code_data)

    @allure.story('判断股票是否是陆股通')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/hsgtis_lgt.json"))
    def test_HSGT_Ifhsgtis_lgt(self, info):
        url = HTTP + "/as_market/api/stock_market_data/v1/hsgt/is_lgt"
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
        # print(j)
        if "data" in j:
            if len(j.get("data")) != 0:
                if j.get("data").get("luStockConnect") == True:
                    logging.info(f"{paylo}是陆股通")

                elif j.get("data").get("luStockConnect") == False:
                    logging.info(f"{paylo}不是陆股通")
                else:
                    TypeError("超出判断范围，请正确输入code")
