# test_HSGT_hsgtstocklist
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
class TestHSGThsgtstocklist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('沪股通/深股通/港股通(沪)/港股通(深)-成分股列表')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/test_HSGTData/test_HSGT_hsgtstocklist.json"))
    def test_HSGT_hsgtstocklist(self, info):
        # pass
        url = HTTP + "/as_market/api/hsgt/v1/stock/list"
        headers = JSON

        # 拼装参数
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
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        if "data" in j:
            for i in range(len(j.get("data"))):
                assert "ts" in j.get("data")[i]
                assert "code" in j.get("data")[i]
                assert "type" in j.get("data")[i]
                assert "name" in j.get("data")[i]
                assert "delay" in j.get("data")[i]
                assert "last" in j.get("data")[i]
                if "diffRate" in j.get("data")[i]:
                    assert "diffRate" in j.get("data")[i]
                if "turnover" in j.get("data")[i]:
                    assert "turnover" in j.get("data")[i]
                assert "preClose" in j.get("data")[i]
                if "diffPrice" in j.get("data")[i]:
                    assert "diffPrice" in j.get("data")[i]
                if "turnoverRate" in j.get("data")[i]:
                    assert "turnoverRate" in j.get("data")[i]
                if "totalMarkValue" in j.get("data")[i]:
                    assert "totalMarkValue" in j.get("data")[i]
                if "peRatioStatic" in j.get("data")[i]:
                    assert "peRatioStatic" in j.get("data")[i]
                if "comparison" in j.get("data")[i]:
                    assert "comparison" in j.get("data")[i]
                if "sharestraded" in j.get("data")[i]:
                    assert "sharestraded" in j.get("data")[i]
                if "amplitude" in j.get("data")[i]:
                    assert "amplitude" in j.get("data")[i]
                if "volumeRatio" in j.get("data")[i]:
                    assert "volumeRatio" in j.get("data")[i]
                if j.get("data")[i].get("delay") == False:
                    logging.info("实时数据")
                else:
                    logging.info("延时数据")
