# test_HSCustomerInfo_AccountValidation          账户验证          /as_trade/api/account/v1/validation
import json

import allure
from jsonschema import validate, draft7_format_checker, SchemaError, ValidationError

from Common.Accountcommon.accountAuth import AccountAuth
from Common.assertapi import assert_data, jsonschema_assert

from Common.sign import get_sign

from Common.requests_library import Requests

from TestAssertions.CounterJsonSchemadata.HSCustomerInfo.AccountValidationSchema import AccountValidationSchema


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_账户验证')
class TestHSCustomerInfoAccountValidation():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        cls.http = list(AccountAuth())[-1]
        cls.url2 = cls.http + "/as_trade/api/account/v1/validation"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_HSCustomerInfo_AccountValidation(self):
        # 拼装参数
        headers = list(AccountAuth())[1]  # 将柜台token赋值到headers


        type = 1
        paylo = {
            "type": type
        }

        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload2 = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=self.url2, headers=headers, data=payload2, title="账户验证"
        )

        k = r.json()
        # print(k)

        assert r.status_code == 200
        if k.get("code") == "000000":
            jsonschema_assert(k.get("code"), k.get("msg"), k, AccountValidationSchema)
        else:
            raise AssertionError(k)
