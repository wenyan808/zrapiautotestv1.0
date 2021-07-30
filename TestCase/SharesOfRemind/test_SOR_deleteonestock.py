# test_SOR_deleteonestock
import json
import random

import allure
import pytest
import requests

from Common.login import login

from Common.sign import get_sign

from Common.tools.read_write_yaml import yamltoken
from glo import HTTP, JSON


# @pytest.mark.skip(reason="调试中")
@allure.feature('股价提醒')
class TestSORDeleteonestock:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('删除配置')
    def test_SOR_deleteonestock(self):
        # pass
        url = HTTP + "/as_market/api/price_notify/v1/delete_one_stock"
        headers = JSON

        # 拼装参数
        paylo = {
            "ts": "SH",
            "code": "600887"
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
        assert j.get("data") == True
