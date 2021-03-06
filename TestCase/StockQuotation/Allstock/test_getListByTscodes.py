# test_getListByTscodes

import logging
import random
import allure
import pytest
from Common.guide import zhuorui
from Common.login import login
from Common.show_sql import showsql
from Common.tools.read_write_json import write_json, get_json
from glo import BASE_DIR


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
        stock_data = list(map(lambda code:{
            "requstList": [
                {
                    "ts": code[0],
                    "code": code[1]
                }
            ]
        } , random_stock))
        write_json(BASE_DIR + r"/TestData/AllStockData/test_getListByTscodes.json", stock_data)

    @allure.story('获取多支股票详情')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/AllStockData/test_getListByTscodes.json"))
    def test_getListByTscodes(self, info):
        response = zhuorui("Allstock", "获取多支股票详情", info)

        # 断言
        assert response.status_code == 200
        if response.json().get("code") == "000000":
            assert response.json().get("code") == "000000"
            assert response.json().get("msg") == "ok"
            if "data" in response.json():
                if len(response.json().get("data")) != 0:
                    for i in range(len(response.json().get("data"))):
                        assert "name" in response.json().get("data")[i]
                        # assert response.json().get("data")[i].get("ts") == paylo.get("requstList")[0].get("ts")
                        assert "hands" in response.json().get("data")[i]
                        # assert "last" in response.json().get("data")[i]
                        # assert response.json().get("data")[i].get("code") == paylo.get("requstList")[0].get("code")
                        assert "type" in response.json().get("data")[i]
                        assert "suspension" in response.json().get("data")[i]
                else:
                    logging.info("data参数存在但data为空list")
            else:
                logging.info("无data参数")