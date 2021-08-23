# test_ETF_F10details

import logging
import allure
import pytest
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
from Common.tools.read_write_json import get_json
from glo import BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('ETF相关')
class TestETFF10details:
    @classmethod
    def setup_class(cls) -> None:
        login()
        # ts_code = showsql(
        #     "192.168.1.234", "zhuorui", "123456", "stock_market",
        #     "select ts,code from t_stock_search where etf_flag='Y';"
        # )
        # random_stock = random.sample(ts_code, 500)
        # ts_code_data = list(map(lambda code: {"ts": code[0], "code": code[1]}, random_stock))
        # write_json(BASE_DIR + r" /TestData/AllStockData/test_ETF_F10details.json", ts_code_data)

    @allure.story('港美股etf简况F10')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/AllStockData/test_ETF_F10details.json"))
    def test_ETF_F10details(self, info):

        response = zhuorui("Allstock", "港美股etf简况F10", info)
        assert_data(response, '000000', 'ok')

        # r = requests.post(url=url, headers=headers, data=payload)
        # # 断言
        # j = r.json()
        #

        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                # for i in range(len( response.json().get("data"))):
                assert "name" in response.json().get("data")
                assert "publisher" in response.json().get("data")
                assert "publishDate" in response.json().get("data")
                assert "equity" in response.json().get("data")
                assert "equityDate" in response.json().get("data")
                assert "dividendsUrl" in response.json().get("data")
                if "currency" in response.json().get("data"):
                    assert "currency" in response.json().get("data")
                if response.json().get("data").get("dividends") != None:
                    if info.get("ts") == "US" and "dividends" in response.json().get("data"):
                        for i in range(len(response.json().get("data").get("dividends"))):
                            # if "engName" in response.json().get("data").get("dividends")[i]:
                            #     assert "engName" in response.json().get("data").get("dividends")[i]
                            # if "rate" in response.json().get("data").get("dividends")[i]:
                            #     assert "rate" in response.json().get("data").get("dividends")[i]
                            assert "exDividendDate" in response.json().get("data").get("dividends")[i]
                            # if "lever" in response.json().get("data").get("dividends")[i]:
                            #     assert "lever" in response.json().get("data").get("dividends")[i]
                            # if "direction" in response.json().get("data").get("dividends")[i]:
                            #     assert "direction" in response.json().get("data").get("dividends")[i]
                            assert "allocationScheme" in response.json().get("data").get("dividends")[i]
                            assert "每股分配" in response.json().get("data").get("dividends")[i].get("allocationScheme")
                            if response.json().get("data").get("dividends")[i].get("direction") == 1:
                                logging.info("做多")
                            elif response.json().get("data").get("dividends")[i].get("direction") == 1:
                                logging.info("做空")
                            else:
                                logging.info("direction为空")
                    elif info.get("ts") == "HK":
                        if response.json().get("data").get("currency") == "港币":
                            assert response.json().get("data").get("currency") == "港币"
                        else:
                            logging.info(f'{response.json().get("data").get("currency")}')
                        if response.json().get("data").get("adminFinanceUnit") == "HKD":
                            assert response.json().get("data").get("adminFinanceUnit") == "HKD"
                        else:
                            logging.info(f'{response.json().get("data").get("adminFinanceUnit")}')
                        assert "trackingIndex" in response.json().get("data")
                        assert "issueNumber" in response.json().get("data")
                        assert "adminFinance" in response.json().get("data")
                        assert "adminFinanceUnit" in response.json().get("data")
                        if "dividendPolicy" in response.json().get("data"):
                            assert "dividendPolicy" in response.json().get("data")
                        if "dividends" in response.json().get("data"):
                            if len(response.json().get("data").get("dividends")) != 0:
                                # pass
                                assert "dividendDate" in response.json().get("data").get("dividends")[0]
                                assert "exDividendDate" in response.json().get("data").get("dividends")[0]
                                assert "allocationScheme" in response.json().get("data").get("dividends")[0]
                                assert "每股分配" in response.json().get("data").get("dividends")[0].get("allocationScheme")
                            else:
                                assert response.json().get("data").get("dividends") == []
                                logging.info("dividends为空的list")

                        else:
                            logging.info("dividends不在data中")

                    else:
                        raise AssertionError("typeerror")

                else:
                    assert response.json().get("data").get("dividends") == None

            else:
                logging.info("data为空，无数据")

        else:
            logging.info("无data字段")
