import json
import logging
import random

import allure
import pytest
import requests

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
from Common.show_sql import showsql
from Common.sign import get_sign
from Common.tools.read_write_json import get_json, write_json
from Common.tools.read_write_yaml import yamltoken
from glo import HTTP, JSON, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")

@allure.feature('陆股通')
class TestHSGTIfhsgtis_lgt:
    @classmethod
    def setup_class(cls) -> None:
        login()
        # ts_code = showsql(
        #     "192.168.1.237", "root", "123456", "stock_market",
        #     "select ts,code from t_stock_search where ts='HK' or ts='SH' or ts='SZ';"
        # )
        # random_stock = random.sample(ts_code, 2)
        # cls.ts_code_data = json.dumps(list(map(lambda code: {"ts": code[0], "code": code[1]}, random_stock)))
        # print(cls.ts_code_data)
        # write_json(BASE_DIR + r"/TestData/hsgtis_lgt.json", cls.ts_code_data)

        ts_code = showsql(
            "192.168.1.237", "root", "123456", "stock_market",
            "select ts,code from t_stock_search where ts='HK' or ts='SH' or ts='SZ';"
        )
        # print(ts_code)
        random_stock = random.sample(ts_code, 500)
        ts_code_data = list(map(lambda code: {"ts": code[0], "code": code[1]}, random_stock))
        write_json(BASE_DIR + r"/TestData/test_HSGTData/hsgtis_lgt.json", ts_code_data)

    @allure.story('判断股票是否是陆股通')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/test_HSGTData/hsgtis_lgt.json"))
    def test_HSGT_Ifhsgtis_lgt(self, info):

        response = zhuorui('Allstock', '判断股票是否是陆股通', info)
        assert_data(response, '000000', 'ok')

        assert response.status_code == 200
        assert response.json().get("code") == "000000"
        assert response.json().get("msg") == "ok"

        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                if response.json().get("data").get("luStockConnect") == True:
                    logging.info(f"{info}是陆股通")

                elif response.json().get("data").get("luStockConnect") == False:
                    logging.info(f"{info}不是陆股通")
                else:
                    TypeError("超出判断范围，请正确输入code")
