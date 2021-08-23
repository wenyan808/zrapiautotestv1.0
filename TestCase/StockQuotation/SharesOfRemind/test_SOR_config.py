# test_SOR_config
import allure
import pytest
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
from Common.tools.read_write_json import get_json
from glo import BASE_DIR

# @pytest.mark.skip(reason="调试中")
@allure.feature('股价提醒')
class TestSORconfig:
    @classmethod
    def setup_class(cls) -> None:
        login()
        # ts_code = showsql(
        #     "192.168.1.234", "zhuorui", "123456", "stock_market",
        #     "select ts,code from t_stock_search where etf_flag='Y';"
        # )
        # random_stock = random.sample(ts_code, 500)
        # ts_code_data = list(map(lambda code: {"ts": code[0], "code": code[1]}, random_stock))
        # write_json(BASE_DIR + r" /TestData/test_ETF_F10details.json", ts_code_data)

    @allure.story('股价提醒配置')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/test_SOR_config.json"))
    def test_SOR_config(self, info):
        # pass
        response = zhuorui('Allstock', '股价提醒配置', info)
        assert_data(response, '000000', 'ok')