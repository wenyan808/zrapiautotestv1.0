# test_HSGT_AHstocklist
import json
import logging

import allure
import pytest
import requests

from Common.login import login

from Common.sign import get_sign
from Common.tools.read_write_json import get_json

from Common.tools.read_write_yaml import yamltoken
from glo import HTTP, JSON, BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('沪深港通')
class TestHSGTAHstocklist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('沪深港通-AH股成分股列表')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/test_HSGT_AHstocklist.json"))
    def test_HSGT_AHstocklist(self, info):
        # pass
        url = HTTP + "/as_market/api/hsgt/ah/v1/stock/list"
        headers = {}
        headers.update(JSON)

        # 拼装参数
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
            for i in range(len(j.get("data"))):
                assert "ts" in j.get("data")[i]
                assert "code" in j.get("data")[i]
                assert "type" in j.get("data")[i]
                assert "name" in j.get("data")[i]
                assert "alast" in j.get("data")[i]
                assert "apreClose" in j.get("data")[i]
                assert "hlast" in j.get("data")[i]
                assert "hpreClose" in j.get("data")[i]
                assert "premium" in j.get("data")[i]
                assert "totalMarkValue" in j.get("data")[i]
                assert "peRatioStatic" in j.get("data")[i]
                assert "delay" in j.get("data")[i]
                if j.get("data")[i].get("delay") == False:
                    logging.info("实时数据")
                else:
                    logging.info("延时数据")






