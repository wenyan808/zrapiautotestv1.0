# test_ETF_planklist
import json
import logging

import allure
import pytest
import requests

from Common.login import login

from Common.sign import get_sign
from Common.tools.read_write_json import get_json

from Common.tools.read_yaml import yamltoken
from glo import HTTP, JSON, BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('ETF相关')
class TestETFplanklist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('etf板块成分股')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/AllStockData/test_ETF_planklist.json"))
    def test_ETF_planklist(self, info):
        # pass
        url = HTTP + "/as_market/api/etf_plank/v1/list"
        headers = JSON

        # 拼装参数
        paylo = {"market":1}
        paylo = info
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        # 调用登录接口通过token传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)
        headers = headers
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
                if len(j.get("data")) != 0:
                    for i in range(len(j.get("data"))):
                        assert "ts" in j.get("data")[i]
                        assert "code" in j.get("data")[i]
                        assert "type" in j.get("data")[i]
                        assert "delay" in j.get("data")[i]
                        assert "name" in j.get("data")[i]
                        # assert "last" in j.get("data")[i]
                        if "preClose" in j.get("data")[i]:
                            assert "preClose" in j.get("data")[i]
                        elif "turnover" in j.get("data")[i]:
                            assert "turnover" in j.get("data")[i]
                        elif "sharestraded" in j.get("data")[i]:
                            assert "sharestraded" in j.get("data")[i]
                        elif "volumeRatio" in j.get("data")[i]:
                            assert "volumeRatio" in j.get("data")[i]
                        elif "amplitude" in j.get("data")[i]:
                            assert "amplitude" in j.get("data")[i]
                        elif "diffRate" in j.get("data")[i]:
                            assert "diffRate" in j.get("data")[i]
                        elif "diffPrice" in j.get("data")[i]:
                            assert "diffPrice" in j.get("data")[i]
                        elif "comparison" in j.get("data")[i]:
                            assert "comparison" in j.get("data")[i]
                        # assert "totalMarkValue" in j.get("data")[i]
                        if info.get("market") == 2 and "direction" in j.get("data")[i]:
                            assert "direction" in j.get("data")[i]
                            assert "lever" in j.get("data")[i]
                        elif info.get("market") == 1:
                            assert "totalCapitalStock" in j.get("data")[i]

                        elif str(j.get("data")[i].get("delay")) == "true":
                            logging.info("实时数据")
                        else:
                            logging.info("延时数据")

                else:
                    logging.info("data为空，无数据")

            else:
                logging.info("无data字段")

        elif j.get("code") == "000103":
            assert j.get("code") == "000103"
            assert j.get("msg") == "sortItem out of range"

        else:
            raise AssertionError("其他错误")
