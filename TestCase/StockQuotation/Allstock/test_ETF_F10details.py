# test_ETF_F10details
import json
import logging
import random

import allure
import pytest
import requests

from Common.login import login
from Common.show_sql import showsql

from Common.sign import get_sign
from Common.tools.read_write_json import get_json, write_json

from Common.tools.read_write_yaml import yamltoken
from glo import HTTP, JSON, BASE_DIR


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
        # pass
        url = HTTP + "/as_market/api/etf/f10/v1/details"
        headers = {}
        headers.update(JSON)

        # 拼装参数
        # paylo = {}
        paylo = info
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        # 调用登录接口通过token传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        # print(token)
        # print(type(token))

        token1 = yamltoken()
        token = {"token": token1}
        headers.update(token)
        # print(headers)
        payload = json.dumps(dict(payload1))
        # time.sleep(1)
        r = requests.post(url=url, headers=headers, data=payload)
        # 断言
        j = r.json()
        # print(j)

        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        if "data" in j:
            if len(j.get("data")) != 0:
                # for i in range(len( j.get("data"))):
                assert "name" in j.get("data")
                assert "publisher" in j.get("data")
                assert "publishDate" in j.get("data")
                assert "equity" in j.get("data")
                assert "equityDate" in j.get("data")
                assert "dividendsUrl" in j.get("data")
                if "currency" in j.get("data"):
                    assert "currency" in j.get("data")
                if j.get("data").get("dividends") != None:
                    if paylo.get("ts") == "US" and "dividends" in j.get("data"):
                        for i in range(len(j.get("data").get("dividends"))):
                            # if "engName" in j.get("data").get("dividends")[i]:
                            #     assert "engName" in j.get("data").get("dividends")[i]
                            # if "rate" in j.get("data").get("dividends")[i]:
                            #     assert "rate" in j.get("data").get("dividends")[i]
                            assert "exDividendDate" in j.get("data").get("dividends")[i]
                            # if "lever" in j.get("data").get("dividends")[i]:
                            #     assert "lever" in j.get("data").get("dividends")[i]
                            # if "direction" in j.get("data").get("dividends")[i]:
                            #     assert "direction" in j.get("data").get("dividends")[i]
                            assert "allocationScheme" in j.get("data").get("dividends")[i]
                            assert "每股分配" in j.get("data").get("dividends")[i].get("allocationScheme")
                            if j.get("data").get("dividends")[i].get("direction") == 1:
                                logging.info("做多")
                            elif j.get("data").get("dividends")[i].get("direction") == 1:
                                logging.info("做空")
                            else:
                                logging.info("direction为空")
                    elif paylo.get("ts") == "HK":
                        if j.get("data").get("currency") == "港币":
                            assert j.get("data").get("currency") == "港币"
                        else:
                            logging.info(f'{j.get("data").get("currency")}')
                        if j.get("data").get("adminFinanceUnit") == "HKD":
                            assert j.get("data").get("adminFinanceUnit") == "HKD"
                        else:
                            logging.info(f'{j.get("data").get("adminFinanceUnit")}')
                        assert "trackingIndex" in j.get("data")
                        assert "issueNumber" in j.get("data")
                        assert "adminFinance" in j.get("data")
                        assert "adminFinanceUnit" in j.get("data")
                        if "dividendPolicy" in j.get("data"):
                            assert "dividendPolicy" in j.get("data")
                        if "dividends" in j.get("data"):
                            if len(j.get("data").get("dividends")) != 0:
                                # pass
                                assert "dividendDate" in j.get("data").get("dividends")[0]
                                assert "exDividendDate" in j.get("data").get("dividends")[0]
                                assert "allocationScheme" in j.get("data").get("dividends")[0]
                                assert "每股分配" in j.get("data").get("dividends")[0].get("allocationScheme")
                            else:
                                assert j.get("data").get("dividends") == []
                                logging.info("dividends为空的list")

                        else:
                            logging.info("dividends不在data中")

                    else:
                        raise AssertionError("typeerror")

                else:
                    assert j.get("data").get("dividends") == None

            else:
                logging.info("data为空，无数据")

        else:
            logging.info("无data字段")
