# test_GetConnectBalanceTrend
import json
import logging

import allure
import pytest
import requests

from Common.get_time_stamp import TimeTostamp
from Common.login import login

from Common.sign import get_sign

from Common.tools.read_write_yaml import yamltoken
from glo import HTTP, JSON


# @pytest.mark.skip(reason="调试中")
@allure.feature('公共分类')
class TestNowSrverinfo:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('查询当天的北向最新资金流动趋势')
    def test_nowSrverinfo(self):
        # pass
        url = HTTP + "/as_market/api/connect_balance/v1/get_connect_balance_trend"
        headers = {}
        headers.update(JSON)

        # 拼装参数
        paylo = {
            "direction": "NB"
        }
        # paylo = info
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
                if len(j.get("data")) != 0:
                    for i in range(len(j.get("data"))):
                        assert "time" in j.get("data")[i]
                        assert "time" in j.get("data")[i]
                        assert j.get("data")[i].get("direction") == paylo.get("direction")
                        assert "balanceSZ" in j.get("data")[i]
                        assert "balanceSH" in j.get("data")[i]
