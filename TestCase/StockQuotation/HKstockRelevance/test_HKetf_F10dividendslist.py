# test_HKetf_F10dividendslist
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
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/test_HKetf_F10dividendslist.json"))
    def test_HKetf_F10dividendslist(self, info):
        # pass
        url = HTTP + "/as_market/api/etf/f10/v1/dividends/list"
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
                assert "list" in j.get("data")
                assert "total" in j.get("data")
                assert "pageSize" in j.get("data")
                if "pageSize" in info:
                    assert j.get("data").get("pageSize") == info.get("pageSize")
                assert "currentPage" in j.get("data")
                if "currentPage" in info:
                    assert j.get("data").get("currentPage") == info.get("currentPage")
                if "list" in j.get("data"):
                    if len(j.get("data").get("list")) != 0:
                        # pass
                        assert "dividendDate" in j.get("data").get("list")[0]
                        assert "exDividendDate" in j.get("data").get("list")[0]
                        assert "allocationScheme" in j.get("data").get("list")[0]
                        assert "每股分配" in j.get("data").get("list")[0].get("allocationScheme")
                    else:
                        assert j.get("data").get("list") == []
                        logging.info("list为空的list")

                else:
                    logging.info("list不在data中")



            else:
                logging.info("data为空list，无数据")

        else:
            logging.info("无data字段")