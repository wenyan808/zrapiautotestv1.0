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


# test_HSGT_getNetCapitalFlow
# @pytest.mark.skip(reason="调试中，返回的结果是404")
@allure.feature('沪深港通')
class TestgetNetCapitalFlow:
    @classmethod
    def setup_class(cls) -> None:
        login()
        ts_code = showsql(
            "192.168.1.237", "root", "123456", "stock_market",
            "select ts,code from t_stock_search where ts='HK' or ts='SH' or ts='SZ';"
        )
        random_stock = random.sample(ts_code, 500)
        ts_code_data = list(map(lambda code: {"ts": code[0], "code": code[1]}, random_stock))
        write_json(BASE_DIR + r"/TestData/test_HSGTData/getNetCapitalFlow.json", ts_code_data)
        # print(ts_code_data)

    @allure.story('沪深港通单只证券累计资金净流向')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/test_HSGTData/getNetCapitalFlow.json"))
    def test_HSGT_getNetCapitalFlow(self, info):

        response = zhuorui('Allstock', '沪深港通单只证券累计资金净流向', info)
        assert_data(response, '000000', 'ok')

        assert response.status_code == 200
        assert response.json().get("code") == "000000"
        assert response.json().get("msg") == "ok"
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                # pass
                assert "date" in response.json().get("data")
                assert "list" in response.json().get("data")
                if len(response.json().get("data").get("list")) != 0:
                    for i in range(len(response.json().get("data").get("list"))):
                        # pass
                        assert "day" in response.json().get("data").get("list")[i]
                        assert "netStockVolume" in response.json().get("data").get("list")[i]
                        assert "netCapitalFlow" in response.json().get("data").get("list")[i]
                        assert "flowStockRatio" in response.json().get("data").get("list")[i]

            else:
                logging.info("data是空的集合")

        else:
            logging.info("无data数据")