# test_StockCompareRemove   股票对比-删除    /as_market/api/stock/compare/v1/remove
import json

import allure
import pytest

from Common.getTestLoginToken import gettestLoginToken
from Common.get_payload_headers import get_headers, get_payload

from Common.requests_library import Requests
from Common.tools.read_json import get_json

from glo import JSON_dev, http, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('股票&行业对比_股票对比-删除')
class TestStockCompareRemove():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        cls.url = http + "/as_market/api/stock/compare/v1/remove"
        cls.url2 = http + "/as_market/api/same_industry_compare/v1/get"
        cls.url1 = http + "/as_market/api/stock_plate/v1/plate_by_code"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_StockCompareRemove(self):
        token = {"token": gettestLoginToken()}
        headers = get_headers(JSON_dev, token)
        ts = "HK"
        code = "00700"
        payload_code = {
            "plateType": 1,
            "ts": ts,
            "code": code
        }
        payload = get_payload(payload_code)
        result = Requests(self.session).post(
            url=self.url1, headers=headers, json=payload, title="根据ts和code获取板块信息"
        )
        # print(result.json())
        industryCode = result.json().get("data").get("plateCode")

        paylo = {
            "ts": ts,
            "industryCode": industryCode,
            "metric": 1,
            "timeRange": 1,
            "stockCode": code
        }
        # paylo1 = info
        # paylo.update(paylo1)
        payload1 = get_payload(paylo)
        # print(payload1)
        r = Requests(self.session).post(
            url=self.url2, headers=headers, json=payload1, title="同行业对比"
        )

        j = r.json()
        # print(j)

        paylo = {
            "ts": ts,
            "code": code
        }
        payload1 = get_payload(paylo)

        r_remove = Requests(self.session).post(
            url=self.url, headers=headers, json=payload1, title="股票对比-删除"
        )

        j_remove = r_remove.json()
        # print(j)
        assert r_remove.status_code == 200
        try:
            assert j_remove.get("code") == "000000"
            assert j_remove.get("msg") == "ok"
        except:
            raise AssertionError(j_remove)
