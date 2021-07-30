# test_GetConnectBalance
import json


import allure
import pytest
import requests


from Common.login import login


from Common.sign import get_sign


from Common.tools.read_write_yaml import yamltoken
from glo import HTTP, JSON, BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('资金流向')
class TestGetConnectBalance:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('查询当天的北向最新资金')
    def test_GetConnectBalance(self):
        # pass
        url = HTTP + "/as_market/api/connect_balance/v1/get_connect_balance"
        headers = JSON

        # 拼装参数
        paylo = {
            "direction": "NB"
        }
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
            assert "direction" in j.get("data")
            assert j.get("data").get("direction") == paylo.get("direction")
            assert "curTime" in j.get("data")
            assert "curBalanceSH" in j.get("data")
            assert "curBalanceSZ" in j.get("data")

    @allure.story('查询当天的南向最新资金')
    def test_GetConnectBalance_SB(self):
        # pass
        url = HTTP + "/as_market/api/connect_balance/v1/get_connect_balance"
        headers = JSON

        # 拼装参数
        paylo = {
            "direction": "SB"
        }
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
                assert "direction" in j.get("data")
                assert "curTime" in j.get("data")
                assert "curBalanceSH" in j.get("data")
                assert "curBalanceSZ" in j.get("data")
        elif j.get("code") == "270403":
            assert j.get("code") == "270403"
            assert j.get("msg") == "只允许北向资金查询"
        else:
            raise AssertionError(print(j))
