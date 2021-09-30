# test_GetSameIndustryCompare   同行业对比  /as_market/api/same_industry_compare/v1/get
import json

import allure
import pytest

from Common.getTestLoginToken import gettestLoginToken
from Common.get_payload_headers import get_headers, get_payload

from Common.requests_library import Requests
from Common.tools.read_json import get_json

from glo import JSON_dev, http, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('股票&行业对比_同行业对比')
class TestGetSameIndustryCompare():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        cls.url = http + "/as_market/api/same_industry_compare/v1/get"
        cls.url1 = http + "/as_market/api/stock_plate/v1/plate_by_code"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/AllStockData/test_GetSameIndustryCompare.json"))
    def test_GetSameIndustryCompare(self, info):
        token = {"token": gettestLoginToken()}
        headers = get_headers(JSON_dev, token)
        plateType = info.get("plateType")
        ts = info.get("ts")
        code = info.get("code")
        payload_code = {
            "plateType": plateType,
            "ts": ts,
            "code": code
        }
        payload = get_payload(payload_code)
        result = Requests(self.session).post(
            url=self.url1, headers=headers, json=payload, title="根据ts和code获取板块信息"
        )
        # print(result.json())
        industryCode = result.json().get("data").get("plateCode")
        if info.get("metric") == "null":
            metric = 1
        else:
            metric = info.get("metric")
        if info.get("timeRange") == "null":
            timeRange = 1
        else:
            timeRange = info.get("timeRange")
        if info.get("stockCode") == "null":
            stockCode = 1
        else:
            stockCode = info.get("stockCode")
        paylo = {
            "ts": ts,
            "industryCode": industryCode,
            "metric": metric,
            "timeRange": timeRange,
            "stockCode": stockCode
        }
        # paylo1 = info
        # paylo.update(paylo1)
        payload1 = get_payload(paylo)
        # print(payload1)
        r = Requests(self.session).post(
            url=self.url, headers=headers, json=payload1, title="同行业对比"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
        except:
            raise AssertionError(j)
