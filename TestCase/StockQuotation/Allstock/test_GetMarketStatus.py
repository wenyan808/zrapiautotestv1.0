# test_GetMarketStatus
import json
import logging

import allure
import pytest
import requests

from Common.get_time_stamp import TimeTostamp
from Common.login import login

from Common.sign import get_sign
from Common.tools.read_write_json import get_json

from Common.tools.read_write_yaml import yamltoken
from glo import HTTP, JSON, BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('公共分类')
class TestGetMarketStatus:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('查询市场交易状态')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/AllStockData/test_GetMarketStatus.json"))
    def test_GetMarketStatus(self, info):
        # pass
        url = HTTP + "/as_market/api/market_trade_status/v1/get_market_status"
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
        if j.get("code") == "000000":
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
            if "data" in j:
                if type(j.get("data")) == list:
                    for i in range(len(j.get("data"))):
                        assert "market" in j.get("data")[i]
                        assert "nowDate" in j.get("data")[i]
                        assert "statusCode" in j.get("data")[i]
                        assert "delay" in j.get("data")[i]
                        if j.get("data")[i].get("delay") == False:
                            logging.info("实时数据")
                        else:
                            logging.info("延时数据")
                        if "desc" in j.get("data")[i]:
                            assert "desc" in j.get("data")[i]
                        if "starStatusCode" in j.get("data")[i]:
                            assert "starStatusCode" in j.get("data")[i]
                        if "starNowDate" in j.get("data")[i]:
                            assert "starNowDate" in j.get("data")[i]
                elif type(j.get("data")) == dict:
                    assert "market" in j.get("data")
                    assert "nowDate" in j.get("data")
                    assert "statusCode" in j.get("data")
                    assert "delay" in j.get("data")
                    if j.get("data").get("delay") == False:
                        logging.info("实时数据")
                    else:
                        logging.info("延时数据")
                else:
                    raise TypeError(print(type(j.get("data"))))
