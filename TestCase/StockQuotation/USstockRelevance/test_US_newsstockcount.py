# test_US_newsstockcount
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
class TestUSNewsstockcount:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('美股F10财报')
    def test_US_newsstockcount(self):
        # pass
        url = HTTP + "/as_market/api/us/new_stock/v1/count"
        headers = {}
        headers.update(JSON)

        # 拼装参数
        paylo = {
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
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        if "data" in j:
            if len(j.get("data")) != 0:
                assert "toBeListed" in j.get("data")
                assert "listed" in j.get("data")
            else:
                logging.info("data为空，无数据")

        else:
            logging.info("无data字段")