import logging
import random
import allure
import pytest
from Common.guide import zhuorui
from Common.login import login
from Common.show_sql import showsql
from Common.tools.read_write_json import write_json, get_json
from glo import BASE_DIR

# test_getStockjump
# @pytest.mark.skip(reason="调试中，返回的结果是404")
@allure.feature('拆合股')
class TestgetStockjump:
    @classmethod
    def setup_class(cls) -> None:
        login()
        ts_code = showsql(
            '192.168.1.237', 'root', '123456', 'stock_market',
            "select ts,code from t_stock_search where ts='HK' or ts='US';"
            )
        random_stock = random.sample(ts_code, 500)
        ts_code_data = list(map(lambda code: {"ts": code[0], "code": code[1]}, random_stock))
        write_json(BASE_DIR + r"/TestData/AllStockData/getStockjump.json", ts_code_data)
        # print(ts_code_data)

    @allure.story('股票跳转信息adr&拆合股')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/AllStockData/getStockjump.json"))
    def test_getStockjump_adrandStocksplits(self,info):
        response = zhuorui("Allstock", "股票跳转信息adr&拆合股", info)
        assert response.status_code == 200
        assert response.json().get("code") == "000000"
        assert response.json().get("msg") == "ok"
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                pass
                # assert "splits" in response.json().get("data") or "adr" in response.json().get("data")

            else:
                logging.info("data是空的集合")

        else:
            logging.info("无data数据")
