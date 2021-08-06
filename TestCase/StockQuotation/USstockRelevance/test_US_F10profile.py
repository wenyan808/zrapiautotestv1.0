
import random
import allure
import pytest
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
from Common.show_sql import showsql
from Common.tools.read_write_json import get_json, write_json
from glo import BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('美股相关')
class test_USF10profile:
    @classmethod
    def setup_class(cls) -> None:
        login()
        ts_code = showsql(
            "192.168.1.237", "root", "123456", "stock_market",
            "select ts,code from t_stock_search where ts='US';"
        )
        # print(ts_code)
        random_stock = random.sample(ts_code, 1)
        ts_code_data = list(map(lambda code: {"ts": code[0], "code": code[1]}, random_stock))
        write_json(BASE_DIR + r"/TestData/USStockData/US_F10profile.json", ts_code_data)

    @allure.story('F10简况')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/USStockData/US_F10profile.json"))
    def test_US_f10profile(self, info):

        response = zhuorui("Allstock", "F10简况", info)
        assert_data(response, '000000', 'ok')
