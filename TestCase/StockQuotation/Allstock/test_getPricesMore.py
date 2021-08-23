
import logging
import random
import allure
import pytest
from Common.guide import zhuorui
from Common.login import login
from Common.show_sql import showsql
from Common.tools.read_write_json import get_json, write_json
from glo import BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('拆合股')
class TestgetPricesMore:
    @classmethod
    def setup_class(cls) -> None:
        login()
        ts_code = showsql(
            '192.168.1.237', 'root', '123456', 'stock_market',
            "select ts,code from t_stock_search where ts='HK' or ts='US';"
            )
        # print(ts_code)
        random_stock = random.sample(ts_code, 500)
        ts_code_data = list(map(lambda code: {
            "stockVos": [
                {
                    "ts": code[0],
                    "code": code[1]
                }
            ]
        } , random_stock))
        write_json(BASE_DIR + r"/TestData/AllStockData/getPricesMore.json", ts_code_data)



    @allure.story('查询更多股票信息')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/AllStockData/getPricesMore.json"))
    def test_getPricesMore_all(self,info):
        response = zhuorui("Allstock", "查询更多股票信息", info)
        assert response.status_code == 200
        assert response.json().get("code") == "000000"
        assert response.json().get("msg") == "ok"
        if "data" in response.json():
            if len(response.json().get("data")) !=  None:
                pass
                # for i in range(len(response.json().get("data"))):
                #     assert "content" in response.json().get("data")[i]
                #     assert "date" in response.json().get("data")[i]

            else:
                logging.info("data是空的集合")

        else:
            logging.info("无data数据")