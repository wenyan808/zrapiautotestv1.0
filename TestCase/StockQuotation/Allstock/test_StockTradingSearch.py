# test_StockTradingSearch
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
class TestNowSrverinfo:
    @classmethod
    def setup_class(cls) -> None:
        login()
        ts_code = showsql(
            # 目前该搜索仅会展示suspension=1的证券产品;当前支持搜索到是证券类型：正股、衍生品
            '192.168.1.237', 'root', '123456', 'stock_market',
            "select ts,code,name from t_stock_search where suspension=1;"
        )
        random_stock = random.sample(ts_code, 500)
        stock_data = list(map(lambda code: {"ts": code[0], "keyWord": code[1]}, random_stock))
        write_json(BASE_DIR + r"/TestData/AllStockData/test_StockTradingSearch.json", stock_data)

    @allure.story('交易时的股票搜索')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/AllStockData/test_StockTradingSearch.json"))
    def test_nowSrverinfo(self,info):
        response = zhuorui("Allstock", "交易时的股票搜索", info)
        assert response.status_code == 200
        if response.json().get("code") == "000000":
            assert response.json().get("code") == "000000"
            assert response.json().get("msg") == "ok"
            if "data" in response.json():
                if len(response.json().get("data")) != 0:
                    for i in range(len(response.json().get("data"))):
                        assert "id" in response.json().get("data")[i]
                        assert "type" in response.json().get("data")[i]
                        # assert response.json().get("data")[i].get("ts") == paylo.get("ts")
                        assert "code" in response.json().get("data")[i]
                        assert "name" in response.json().get("data")[i]
                        assert "suspension" in response.json().get("data")[i]
