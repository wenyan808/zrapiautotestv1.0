# test_USetf_constituentstock
import json
import logging

import allure
import pytest
import requests

from Common.login import login

from Common.sign import get_sign

from Common.tools.read_write_yaml import yamltoken
from glo import HTTP, JSON


# @pytest.mark.skip(reason="调试中")
@allure.feature('美股相关')
class TestUSetfConstituentstock:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('美股etf成分股组合（十大成分股+持仓构成）')
    def test_USetf_constituentstock(self):
        # pass
        url = HTTP + "/as_market/api/us/etf/v1/constituent/stock"
        headers = JSON

        # 拼装参数
        paylo = {
            "ts": "US",
            "code": "QQQ"
        }
        # paylo = info
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
            if len(j.get("data")) != 0:
                assert "tenStocks" in j.get("data")
                for i in range(len(j.get("data").get("tenStocks"))):
                    assert "ts" in j.get("data").get("tenStocks")[i]
                    assert "code" in j.get("data").get("tenStocks")[i]
                    assert "type" in j.get("data").get("tenStocks")[i]
                    assert "name" in j.get("data").get("tenStocks")[i]
                    assert "rate" in j.get("data").get("tenStocks")[i]
                assert "position" in j.get("data")
                assert "num" in j.get("data").get("position")
                assert "industry" in j.get("data").get("position")
                for i in range(len(j.get("data").get("position").get("industry"))):
                    assert "code" in j.get("data").get("position").get("industry")[i]
                    assert "name" in j.get("data").get("position").get("industry")[i]
                    assert "rate" in j.get("data").get("position").get("industry")[i]

            else:
                logging.info("data为空，无数据")

        else:
            logging.info("无data字段")
