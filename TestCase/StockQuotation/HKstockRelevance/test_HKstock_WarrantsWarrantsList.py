# test_HKstock_WarrantsWarrantsList    全部轮证-窝轮牛熊列表    /as_market/api/hk/warrants/v1/warrants_list
import json

import allure
import pytest

from Common.getTestLoginToken import gettestLoginToken
from Common.get_payload_headers import get_headers, get_payload


from Common.requests_library import Requests
from Common.tools.read_json import get_json


from glo import JSON_dev, http, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('港股_全部轮证-窝轮牛熊列表')
class TestHKstockWarrantsWarrantsList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        cls.url = http + "/as_market/api/hk/warrants/v1/warrants_list"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/HKstockData/test_HKstock_WarrantsWarrantsList.json"))
    def test_HKstock_WarrantsWarrantsList(self,info):
        token = {"token": gettestLoginToken()}
        headers = get_headers(JSON_dev, token)
        # 将柜台token赋值到headers
        # print(headers)

        paylo = info
        payload1 = get_payload(paylo)

        r = Requests(self.session).post(
            url=self.url, headers=headers, json=payload1, title="全部轮证-界内证列表"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
        except:
            raise AssertionError(j)