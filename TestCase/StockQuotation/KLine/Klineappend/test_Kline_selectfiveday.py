# test_Kline_selectfiveday
import logging
import random
import allure
import pytest
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
from Common.show_sql import showsql
from Common.tools.read_write_json import get_json, write_json
from glo import BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('K线')
class TestKlineSelectfiveday:
    @classmethod
    def setup_class(cls) -> None:
        login()
        ts_code = showsql(
            "192.168.1.237", "root", "123456", "stock_market",
            "select ts,code from t_stock_search where ts='HK';"
        )  # 可以添加条件筛选：where ts='HK' or ts='SH' or ts='SZ' or ts='US'
        random_stock = random.sample(ts_code, 500)
        ts_code_data = list(map(lambda code: {"ts": code[0], "code": code[1]}, random_stock))
        write_json(BASE_DIR + r"/TestData/test_Kline_selectfiveday.json", ts_code_data)

    @allure.story('查询五日')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/test_Kline_selectfiveday.json"))
    def test_Kline_selectfiveday(self, info):

        response = zhuorui('Allstock', '查询五日', info)
        assert_data(response, '000000', 'ok')
        if response.json().get("code") == "000000":
            assert response.json().get("code") == "000000"
            assert response.json().get("msg") == "ok"
            if "data" in response.json():
                if len(response.json().get("data")) != 0:
                    assert "type" in response.json().get("data")
                    assert "ts" in response.json().get("data")
                    assert response.json().get("data").get("ts") == info.get("ts")
                    assert "code" in response.json().get("data")
                    assert response.json().get("data").get("code") == info.get("code")
                    if "preClose" in response.json().get("data"):
                        assert "preClose" in response.json().get("data")
                    # assert "adresponse.json()" in response.json().get("data")
                    # if "list" in response.json().get("data"):
                    #     for i in range(len(response.json().get("data").get("list"))):
                    #         assert "time" in response.json().get("data").get("list")[i]
                    #         if "close" in response.json().get("data").get("list")[i]:
                    #             assert "close" in response.json().get("data").get("list")[i]
                            # if "sharestraded" in response.json().get("data").get("list")[i]:
                            #     assert "sharestraded" in response.json().get("data").get("list")[i]
                            # if "turnover" in response.json().get("data").get("list")[i]:
                            #     assert "turnover" in response.json().get("data").get("list")[i]
                            # if "vwap" in response.json().get("data").get("list")[i]:
                            #     assert "vwap" in response.json().get("data").get("list")[i]
                else:
                    logging.info("data为空list")
            else:
                logging.info("data在response.json()不存在")
        else:
            # raise AssertionError(payload)
            raise AssertionError(response.json())
