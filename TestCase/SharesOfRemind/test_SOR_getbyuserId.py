# test_SOR_getbyuserId
import json
import random

import allure
import pytest
import requests

from Common.login import login

from Common.sign import get_sign

from Common.tools.read_yaml import yamltoken
from glo import HTTP, JSON


# @pytest.mark.skip(reason="调试中")
@allure.feature('股价提醒')
class TestSOGetbyuserId:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('查询用户设置的所有股价提醒的配置信息')
    def test_SOR_getbyuserId(self):
        # pass
        url = HTTP + "/as_market/api/price_notify/v1/get_by_userId"
        headers = JSON

        # 拼装参数
        paylo = {}
        # paylo = info
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        # 调用登录接口通过token传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)
        headers = headers
        # print(token)

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
                for h in range(len(j.get("data"))):
                    assert "ts" in j.get("data")[h]
                    assert "code" in j.get("data")[h]
                    assert "type" in j.get("data")[h]
                    assert "name" in j.get("data")[h]
                    assert "notifyRate" in j.get("data")[h]
                    assert "updateTime" in j.get("data")[h]
                    assert "list" in j.get("data")[h]
                    for i in range(len(j.get("data")[h].get("list"))):
                        assert "compareType" in j.get("data")[h].get("list")[i]
                        assert "threshold" in j.get("data")[h].get("list")[i]
                        assert "status" in j.get("data")[h].get("list")[i]
                    if j.get("data")[0].get("ts") == "SH" and j.get("data")[0].get("code") == "600887":
                        assert j.get("data")[0].get("ts") == "SH"
                        assert j.get("data")[0].get("code") == "600887"
                        assert j.get("data")[0].get("type") == 2
                        assert j.get("data")[0].get("name") == "伊利股份"
                        assert j.get("data")[0].get("notifyRate") == 3
