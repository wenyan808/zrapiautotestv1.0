# test_HSCustomerInfo_GetFundsInfo        获取账户资产信息       /as_trade/api/funds/v1/info
import json

import allure
from jsonschema import validate, draft7_format_checker, SchemaError, ValidationError

from Common.Accountcommon.accountAuth import AccountAuth
from Common.assertapi import assert_data, jsonschema_assert

from Common.sign import get_sign

from Common.requests_library import Requests

from TestAssertions.CounterJsonSchemadata.HSCustomerInfo.GetFundsInfoSchema import GetFundsInfoSchema


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_获取账户资产信息')
class TestHSCustomerInfoGetFundsInfo():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_HSCustomerInfo_GetFundsInfo(self):
        http = list(AccountAuth())[-1]
        # 拼装参数 headers
        headers = list(AccountAuth())[1]  # 将柜台token赋值到headers
        # 获取账户资产信息接口的url
        url2 = http + "/as_trade/api/funds/v1/info"

        payloa = {}

        sign1 = {"sign": get_sign(payloa)}  # 把参数签名后通过sign1传出来
        payload3 = {}
        payload3.update(payloa)
        payload3.update(sign1)

        payload4 = json.dumps(dict(payload3))

        r = Requests(self.session).post(
            url=url2, headers=headers, data=payload4, title="获取账户资产信息"
        )

        k = r.json()
        # print(k)
        assert r.status_code == 200
        if k.get("code") == "000000":
            jsonschema_assert(k.get("code"), k.get("msg"), k, GetFundsInfoSchema)
        else:
            raise AssertionError(k)
