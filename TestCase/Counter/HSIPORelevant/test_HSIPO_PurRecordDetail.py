# test_HSIPO_PurRecordDetail    IPO申购记录详情    /as_trade/api/ipo/v1/pur_record_detail
import json

import allure
from jsonschema import validate, draft7_format_checker, SchemaError, ValidationError

from Common.Accountcommon.accountAuth import AccountAuth
from Common.assertapi import assert_data, jsonschema_assert

from Common.sign import get_sign

from Common.requests_library import Requests

from TestAssertions.CounterJsonSchemadata.HSIPORelevantSchema.PurRecordDetailSchema import PurRecordDetailSchema


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_IPO申购记录详情')
class TestHSIPOPurRecordDetail():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        cls.http = list(AccountAuth())[-1]
        cls.url1 = cls.http + "/as_trade/api/ipo/v1/pur_record_detail"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_HSIPO_PurRecordDetail(self):
        # 拼装参数
        headers = list(AccountAuth())[1]  # 将柜台token赋值到headers
        # print(headers)
        body = {
            "ts": "HK",
            "code": "09982"
        }

        sign1 = {"sign": get_sign(body)}  # 把参数签名后通过sign1传出来
        body1 = {}
        body1.update(body)
        body1.update(sign1)

        payload = json.dumps(dict(body1))

        getinfo = Requests(self.session).post(
            url=self.url1, headers=headers, data=payload, title="IPO申购记录详情"
        )

        j = getinfo.json()
        # print(j)
        assert getinfo.status_code == 200
        if j.get("code") == "000000":

            assert j.get("data").get("ts") == body.get("ts")
            assert j.get("data").get("code") == body.get("code")
            jsonschema_assert(j.get("code"), j.get("msg"), j, PurRecordDetailSchema)
        else:
            raise AssertionError(j)





