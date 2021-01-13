# test_US_newstocklistedpage
import json
import logging

import allure
import pytest
import requests

from Common.login import login

from Common.sign import get_sign

from Common.tools.read_yaml import yamltoken
from glo import HTTP, JSON


# @pytest.mark.skip(reason="调试中")
@allure.feature('美股相关')
class TestUSNewsstocklistedpage:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('新股日历分页获取已上市列表')
    def test_US_newsstocklistedpage(self):
        # pass
        url = HTTP + "/as_market/api/us/new_stock/v1/listed/page"
        headers = JSON

        # 拼装参数
        paylo = {
            "currentPage": 1,
            "pageSize": 15,
            "order": 1,
            "asc": "false"
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
                assert "list" in (j.get("data"))
                for i in range(len(j.get("data").get("list"))):
                    assert "ts" in j.get("data").get("list")[i]
                    assert "code" in j.get("data").get("list")[i]
                    assert "type" in j.get("data").get("list")[i]
                    assert "name" in j.get("data").get("list")[i]
                    assert "listingTime" in j.get("data").get("list")[i]
                    assert "issuePrice" in j.get("data").get("list")[i]
                    assert "last" in j.get("data").get("list")[i]
                    assert "delay" in j.get("data").get("list")[i]
                assert "total" in j.get("data")
                assert j.get("data").get("pageSize") == paylo.get("pageSize")
                assert j.get("data").get("currentPage") == 1
            else:
                logging.info("data为空，无数据")

        else:
            logging.info("无data字段")
