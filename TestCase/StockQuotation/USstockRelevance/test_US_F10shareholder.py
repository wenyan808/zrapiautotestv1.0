# test_US_F10shareholder
import json
import logging

import allure
import pytest
import requests

from Common.get_time_stamp import stampToTime
from Common.login import login

from Common.sign import get_sign

from Common.tools.read_write_yaml import yamltoken
from glo import HTTP, JSON


# @pytest.mark.skip(reason="调试中")
@allure.feature('美股相关')
class TestUSF10shareholder:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('获取股东数据-机构持有top10-基金持有top10')
    def test_US_F10shareholder(self):
        # pass
        url = HTTP + "/as_market/api/us/f10/v1/share_holder"
        headers = {}
        headers.update(JSON)

        # 拼装参数
        paylo = {
            "ts": "US",
            "code": "TEDU"
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
                assert "institutionHolders" in j.get("data")
                assert "fundHolders" in j.get("data")
                for i in range(len(j.get("data").get("institutionHolders"))):
                    assert "name" in j.get("data").get("institutionHolders")[i]
                    assert "ratio" in j.get("data").get("institutionHolders")[i]
                    assert "changeShare" in j.get("data").get("institutionHolders")[i]
                    assert "date" in j.get("data").get("institutionHolders")[i]
                    # print(stampToTime(j.get("data").get("institutionHolders")[i].get("date")))
                for i in range(len(j.get("data").get("fundHolders"))):
                    assert "name" in j.get("data").get("fundHolders")[i]
                    assert "ratio" in j.get("data").get("fundHolders")[i]
                    assert "changeShare" in j.get("data").get("fundHolders")[i]
                    assert "date" in j.get("data").get("fundHolders")[i]
            else:
                logging.info("data为空，无数据")

        else:
            logging.info("无data字段")
