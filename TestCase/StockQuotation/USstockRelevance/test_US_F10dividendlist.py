# test_US_F10dividendlist
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
class TestUSF10dividendlist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('分红派息-查看详情_all')
    def test_US_F10dividendlist_all(self):
        # pass
        url = HTTP + "/as_market/api/us/f10/v1/dividend/list"
        headers = JSON

        # 拼装参数
        paylo = {
            "ts": "US",
            "code": "BABA",
            "currentPage": 1,
            "pageSize": 15
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
                assert "pageSize" in j.get("data")
                assert "pageSize" in j.get("data")
                assert "currentPage" in j.get("data")
                # assert "list" in j.get("data")
                assert j.get("data").get("total") == 0
                assert j.get("data").get("pageSize") == 15
                assert j.get("data").get("currentPage") == 1


            else:
                logging.info("data为空，无数据")

        else:
            logging.info("无data字段")

    @allure.story('分红派息-查看详情_必传值')
    def test_US_F10dividendlist_tscode(self):
        # pass
        url = HTTP + "/as_market/api/us/f10/v1/dividend/list"
        headers = JSON

        # 拼装参数
        paylo = {
            "ts": "US",
            "code": "JD"
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
                assert "pageSize" in j.get("data")
                assert "pageSize" in j.get("data")
                assert "currentPage" in j.get("data")
                # assert "list" in j.get("data")
                assert j.get("data").get("total") == 0
                assert j.get("data").get("pageSize") == 15
                assert j.get("data").get("currentPage") == 1


            else:
                logging.info("data为空，无数据")

        else:
            logging.info("无data字段")
