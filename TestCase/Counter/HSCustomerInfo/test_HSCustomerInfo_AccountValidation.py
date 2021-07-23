# test_HSCustomerInfo_AccountValidation          账户验证          /as_trade/api/account/v1/validation
import json

import allure
from jsonschema import validate, draft7_format_checker, SchemaError, ValidationError

from Common.Accountcommon.accountAuth import AccountAuth

from Common.sign import get_sign

from Common.requests_library import Requests

from TestAssertions.CounterJsonSchemadata.HSCustomerInfo.AccountValidationSchema import AccountValidationSchema


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_账户验证')
class TestHSCustomerInfoAccountValidation():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_HSCustomerInfo_AccountValidation(self):
        http = list(AccountAuth())[-1]
        # 拼装参数
        headers = list(AccountAuth())[1]  # 将柜台token赋值到headers

        url2 = http + "/as_trade/api/account/v1/validation"
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
            url=url2, headers=headers, data=payload2, title="账户验证"
        )

        k = r.json()
        # print(k)

        assert r.status_code == 200
        if k.get("code") == "000000":
            assert k.get("code") == "000000"
            assert k.get("msg") == "ok"

            schema = k
            try:
                validate(instance=AccountValidationSchema, schema=schema, format_checker=draft7_format_checker)
            except SchemaError as e:
                return 1, f"验证模式schema出错：\n出错位置：{'--> '.join([i for i in e.path])}\n提示信息：{e.message}"
            except ValidationError as e:
                return 1, f"json数据不符合schema规定：\n出错字段：{'-->'.join([i for i in e.path])}\n提示信息：{e.message}"
            else:
                return 0, "success!"
        else:
            raise AssertionError(k)
