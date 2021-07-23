# test_HSIPO_PurRecordList      IPO申购记录列表     /as_trade/api/ipo/v1/pur_record_list
import json

import allure
from jsonschema import validate, draft7_format_checker, SchemaError, ValidationError

from Common.Accountcommon.accountAuth import AccountAuth
from Common.assertapi import assert_data, jsonschema_assert

from Common.sign import get_sign

from Common.requests_library import Requests

from TestAssertions.CounterJsonSchemadata.HSIPORelevantSchema.PurRecordListSchema import PurRecordListSchema


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_IPO申购记录列表')
class TestHSIPOPurRecordList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        cls.http = list(AccountAuth())[-1]
        cls.url = cls.http + "/as_trade/api/ipo/v1/pur_record_list"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_HSIPO_PurRecordList(self):
        # 拼装参数
        headers = list(AccountAuth())[1]  # 将柜台token赋值到headers
        # print(headers)

        paylo = {}

        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=self.url, headers=headers, data=payload, title="IPO申购记录列表"
        )

        k = r.json()
        # print(k)
        assert r.status_code == 200
        if k.get("code") == "000000":
            jsonschema_assert(k.get("code"), k.get("msg"), k, PurRecordListSchema)
        else:
            raise AssertionError(k)
