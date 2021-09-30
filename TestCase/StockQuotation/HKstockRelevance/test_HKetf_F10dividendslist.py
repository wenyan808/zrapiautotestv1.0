# test_HKetf_F10dividendslist
import json
import logging
import allure
import pytest
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
from Common.tools.read_write_json import get_json
from glo import BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('港股相关')
class TestHKetfF10dividendslist:
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

    @allure.story('港股ETF分红派息列表')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/HKstockData/test_HKetf_F10dividendslist.json"))
    def test_HKetf_F10dividendslist(self, info):

        response = zhuorui("Allstock", "港股ETF分红派息列表", info)
        assert_data(response, '000000', 'ok')


        assert response.status_code == 200
        assert response.json().get("code") == "000000"
        assert response.json().get("msg") == "ok"
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                # for i in range(len( response.json().get("data"))):
                assert "list" in response.json().get("data")
                assert "total" in response.json().get("data")
                assert "pageSize" in response.json().get("data")
                if "pageSize" in info:
                    assert response.json().get("data").get("pageSize") == info.get("pageSize")
                assert "currentPage" in response.json().get("data")
                if "currentPage" in info:
                    assert response.json().get("data").get("currentPage") == info.get("currentPage")
                if "list" in response.json().get("data"):
                    if len(response.json().get("data").get("list")) != 0:
                        # pass
                        assert "dividendDate" in response.json().get("data").get("list")[0]
                        assert "exDividendDate" in response.json().get("data").get("list")[0]
                        assert "allocationScheme" in response.json().get("data").get("list")[0]
                        assert "每股分配" in response.json().get("data").get("list")[0].get("allocationScheme")
                    else:
                        assert response.json().get("data").get("list") == []
                        logging.info("list为空的list")

                else:
                    logging.info("list不在data中")



            else:
                logging.info("data为空list，无数据")

        else:
            logging.info("无data字段")