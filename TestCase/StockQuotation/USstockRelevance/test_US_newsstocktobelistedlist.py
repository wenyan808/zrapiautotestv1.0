# test_US_newsstocktobelistedlist
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
class TestUSNewsstocktobelistedlist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('新股日历获取待上市列表')
    def test_US_newsstocktobelistedlist(self):
        # pass
        url = HTTP + "/as_market/api/us/new_stock/v1/to_be_listed/list"
        headers = JSON

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
                for i in range(len(j.get("data"))):
                    assert "ts" in j.get("data")[i]
                    assert "code" in j.get("data")[i]
                    assert "type" in j.get("data")[i]
                    assert "name" in j.get("data")[i]
                    assert "ipoDate" in j.get("data")[i]
                    assert "ipoPriceLow" in j.get("data")[i]
                    assert "ipoPriceHigh" in j.get("data")[i]
                    assert "shares" in j.get("data")[i]
            else:
                logging.info("data为空，无数据")

        else:
            logging.info("无data字段")