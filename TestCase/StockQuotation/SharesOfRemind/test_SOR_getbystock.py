# test_SOR_getbystock
import allure
import pytest
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
from Common.tools.read_write_json import get_json
from glo import  BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('股价提醒')
class TestSOGetbystock:
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

    @allure.story('查用户对某个股票的涨跌提醒配置')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/test_SOR_getbystock.json"))
    def test_SOR_getbystock(self, info):
        response = zhuorui('Allstock', '查用户对某个股票的涨跌提醒配置', info)
        assert_data(response, '000000', 'ok')

        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                assert "ts" in response.json().get("data")
                assert response.json().get("data").get("ts") == info.get("ts")
                assert "code" in response.json().get("data")
                assert response.json().get("data").get("code") == info.get("code")
                assert "type" in response.json().get("data")
                assert response.json().get("data").get("type") == info.get("type")
                assert "name" in response.json().get("data")
                assert "notifyRate" in response.json().get("data")
                assert "updateTime" in response.json().get("data")
                assert "list" in response.json().get("data")
                for i in range(len(response.json().get("data").get("list"))):
                    assert "compareType" in response.json().get("data").get("list")[i]
                    assert "threshold" in response.json().get("data").get("list")[i]
                    assert "status" in response.json().get("data").get("list")[i]
