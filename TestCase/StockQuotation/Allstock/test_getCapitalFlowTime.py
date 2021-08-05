# test_getCapitalFlowTime

import logging
import random
import allure
import pytest
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
from Common.show_sql import showsql
from Common.tools.read_write_json import write_json, get_json
from glo import BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('公共分类')
class TestGetCapitalFlowTime:
    @classmethod
    def setup_class(cls) -> None:
        login()
        ts_code = showsql(
            '192.168.1.237', 'root', '123456', 'stock_market',
            "select ts,code,name from t_stock_search;"
        )
        random_stock = random.sample(ts_code, 100)
        stock_data = list(map(lambda code: {
            "ts": code[0],
            "code": code[1],
            "dayCount": 3
        }, random_stock))
        write_json(BASE_DIR + r"/TestData/AllStockData/test_getCapitalFlowTime.json", stock_data)

    @allure.story('按时间查询资金统计数据')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/AllStockData/test_getCapitalFlowTime.json"))
    def test_getCapitalFlowTime(self, info):
        response = zhuorui("Allstock", "按时间查询资金统计数据", info)
        assert_data(response, '000000', 'ok')

        assert response.status_code == 200
        if response.json().get("code") == "000000":
            assert response.json().get("code") == "000000"
            assert response.json().get("msg") == "ok"
            if "data" in response.json():
                if len(response.json().get("data")) != 0:
                    for i in range(len(response.json().get("data"))):
                        assert "totalInflowAndOutflow" in response.json().get("data")[i]
                        assert "totalInflowAndOutflow" in response.json().get("data")[i]
                        if "ts" in response.json().get("data")[i]:
                            assert response.json().get("data")[i].get("ts") == info.get("ts")
                        else:
                            logging.info(f"{info.get('ts')}不存在")
                        if "code" in response.json().get("data")[i]:
                            assert response.json().get("data")[i].get("code") == info.get("code")
                        else:
                            logging.info(f"{info.get('code')}不存在")
                else:
                    logging.info("data参数存在但data为空list")
            else:
                logging.info("无data参数")