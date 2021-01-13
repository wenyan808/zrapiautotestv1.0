# test_US_F10assetsliabilitylist
import json
import logging

import allure
import pytest
import requests

from Common.login import login

from Common.sign import get_sign
from Common.tools.read_write_json import get_json

from Common.tools.read_yaml import yamltoken
from glo import HTTP, JSON, BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('美股相关')
class TestUSF10profitlist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('美股F10获取资产负债表详情页信息')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/test_US_F10assetsliabilitylist.json"))
    def test_US_F10assetsliabilitylist(self, info):
        # pass
        url = HTTP + "/as_market/api/us/f10/v1/assets_liability_list"
        headers = JSON

        # 拼装参数

        # paylo = {
        #     "ts": "US",
        #     "code": "GOOG",
        #     "type": 0,
        #     "pageSize": 15
        # }
        paylo = info
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
                assert "list" in j.get("data")
                for i in range(len(j.get("data").get("list"))):
                    assert j.get("data").get("list")[i].get("currency") == "USD"
                    assert j.get("data").get("list")[i].get("reportType") == str(info.get("type"))
                    assert "date" in j.get("data").get("list")[i]
                    assert "currency" in j.get("data").get("list")[i]
                    assert "reportType" in j.get("data").get("list")[i]
                    assert "totalAssets" in j.get("data").get("list")[i]
                    assert "cashAndCashEquivalents" in j.get("data").get("list")[i]
                    assert "accountsReceivable" in j.get("data").get("list")[i]
                    assert "stock" in j.get("data").get("list")[i]
                    assert "intangibleAssets" in j.get("data").get("list")[i]
                    assert "otherAssets" in j.get("data").get("list")[i]
                    assert "totalCurrentAssets" in j.get("data").get("list")[i]
                    assert "totalLiabilities" in j.get("data").get("list")[i]
                    assert "shortTermLoan" in j.get("data").get("list")[i]
                    assert "accountsPayable" in j.get("data").get("list")[i]
                    assert "totalCurrentLiabilities" in j.get("data").get("list")[i]
                    assert "longTermLiabilities" in j.get("data").get("list")[i]
                    assert "deferredTax" in j.get("data").get("list")[i]
                    assert "totalOwnerEquity" in j.get("data").get("list")[i]
                    assert "preferredStock" in j.get("data").get("list")[i]
                    assert "minorityInterest" in j.get("data").get("list")[i]
                assert "total" in j.get("data")
                assert j.get("data").get("pageSize") == 15
                assert j.get("data").get("currentPage") == 1
                # print(j.get("data"))

            else:
                logging.info("data是空的集合")

        else:
            logging.info("无data数据")