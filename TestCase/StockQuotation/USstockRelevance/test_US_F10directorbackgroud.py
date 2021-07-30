# test_US_F10directorbackgroud
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
class TestUSF10directorlist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('获取公司高管-背景介绍')
    def test_US_F10directorlist(self):
        # pass
        url = HTTP + "/as_market/api/us/f10/v1/director/list"
        headers = JSON

        # 拼装参数

        paylo = {
            "ts": "US",
            "code": "TSLA",
            "pageSize": 15,
            "currentPage": 1
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
        # print(j.get("data").get("list"))
        url_backgroud = HTTP + "/as_market/api/us/f10/v1/director/backgroud"
        body = {
            "id": f'{j.get("data").get("list")[0].get("id")}'
        }
        # print(body)
        # body ={"id":"06NF4N-E"}
        sign1 = {"sign": get_sign(body)}  # 把参数签名后通过sign1传出来
        # 调用登录接口通过token传出来
        body1 = {}
        body1.update(body)
        body1.update(sign1)
        body = json.dumps(dict(body1))
        r = requests.post(url=url_backgroud, headers=headers, data=body)
        # print(r.json())
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        # if "data" in j:
        #     if len(j.get("data")) != 0:
        #         # assert "list" in j.get("data")
        #         # for i in range(len(j.get("data").get("list"))):
        #         #     # assert j.get("data").get("list")[i].get("id") == "美元"
        #         #     assert "id" in j.get("data").get("list")[i]
        #         #     assert "name" in j.get("data").get("list")[i]
        #         #     assert "job" in j.get("data").get("list")[i]
        #         #     assert "date" in j.get("data").get("list")[i]
        #         #     assert "active" in j.get("data").get("list")[i]
        #         assert j.get("data").get("total") == 0
        #         assert j.get("data").get("pageSize") == 15
        #         assert j.get("data").get("currentPage") == 1
        #         # print(j.get("data"))
        #
        #     else:
        #         logging.info("data是空的集合")
        #
        # else:
        #     logging.info("无data数据")
