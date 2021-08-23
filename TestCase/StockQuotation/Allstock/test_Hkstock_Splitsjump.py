import logging
import random
import allure
import pytest
from Common.guide import zhuorui
from Common.login import login
from Common.show_sql import showsql
from Common.tools.read_write_json import write_json, get_json
from glo import BASE_DIR


# test_Hkstock_Splitsjump
# @pytest.mark.skip(reason="调试中")
@allure.feature('港股')
class TestHkstockSplitsjump:
    @classmethod
    def setup_class(cls) -> None:
        login()
        ts_code = showsql(
            '192.168.1.237', 'root', '123456', 'stock_market',
            "select ts,code from t_stock_search where ts='HK';"
        )

        random_stock = random.sample(ts_code, 500)
        ts_code_data = list(map(lambda code: {"ts": code[0], "code": code[1]}, random_stock))
        write_json(BASE_DIR + r"/TestData/AllStockData/HkstockSplitsjump.json", ts_code_data)

    @allure.story('拆合股-横幅(跳转)')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/AllStockData/HkstockSplitsjump.json"))
    def test_Hkstock_Splitsjumpp(self, info):
        response = zhuorui("Allstock", "拆合股-横幅(跳转)", info)


        assert response.status_code == 200
        assert response.json().get("code") == "000000"
        assert response.json().get("msg") == "ok"
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                assert "ts" in response.json().get("data")
                assert "code" in response.json().get("data")
                assert "type" in response.json().get("data")
                if "name" in response.json().get("data"):
                    assert "name" in response.json().get("data")
                assert "content" in response.json().get("data")
            else:
                logging.info("data是空的集合")

        else:
            logging.info("无data数据")

