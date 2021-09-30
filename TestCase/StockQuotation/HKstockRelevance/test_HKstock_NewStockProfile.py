# test_HKstock_NewStockProfile    新股可认购-简况   /as_market/api/hk/new_stock/v1/subscribed/profile
import json

import allure
import pytest
from jsonschema import validate, draft7_format_checker, SchemaError, ValidationError

from Common.Accountcommon.accountAuth import AccountAuth
from Common.assertapi import jsonschema_assert
from Common.getTestLoginToken import gettestLoginToken
from Common.get_payload_headers import get_headers, get_payload
from Common.sign import get_sign

from Common.requests_library import Requests
from TestAssertions.CounterJsonSchemadata.HSIPORelevantSchema.SubscribeListSchema import SubscribeListSchema

from glo import JSON_dev, http


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('港股_新股可认购-简况')
class TestHKstockNewStockProfile():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        cls.http = list(AccountAuth())[-1]
        cls.url1 = cls.http + "/as_trade/api/ipo/v1/subscribe_list"
        cls.url = cls.http + "/as_market/api/hk/new_stock/v1/subscribed/profile"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_HKstock_NewStockProfile(self):
        headers = list(AccountAuth())[1]  # 将柜台token赋值到headers
        # print(headers)

        paylo = {}
        payload1 = get_payload(paylo)

        r_data = Requests(self.session).post(
            url=self.url1, headers=headers, data=payload1, title="IPO可认购列表"
        )

        k = r_data.json()
        # print(k)
        if "data" in k:
            if k.get("data"):
                ts = k.get("data")[0].get("ts")
                code = k.get("data")[0].get("code")

                body = {
                    "ts": ts,
                    "code": code
                }

                payload = get_payload(body)

                r = Requests(self.session).post(
                    url=self.url, headers=headers, data=payload, title="新股可认购-简况"
                )

                j = r.json()
                # print(j)
                assert r.status_code == 200
                try:
                    assert j.get("code") == "000000"
                    assert j.get("msg") == "ok"
                except:
                    raise AssertionError(j)
            else:
                print("可认购列表为空")
        else:
            raise AssertionError(k)
