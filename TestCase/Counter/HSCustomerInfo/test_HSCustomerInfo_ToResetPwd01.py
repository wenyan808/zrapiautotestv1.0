# test_HSCustomerInfo_ToResetPwd01   重置交易密码-步骤一    /as_trade/api/account/v1/to_reset_pwd
import json

import allure
from jsonschema import validate, draft7_format_checker, SchemaError, ValidationError

from Common.Accountcommon.accountAuth import UserLoginAuth

from Common.sign import get_sign

from Common.requests_library import Requests

from TestAssertions.CounterJsonSchemadata.HSCustomerInfo.ToResetPwd01Schema import ToResetPwd01Schema

from glo import phone3, pwd3, phoneArea, user_password


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_重置交易密码-步骤一')
class TestHSCustomerInfoToResetPwd01():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_HSCustomerInfo_ToResetPwd01(self):
        user_pwd = pwd3
        a = UserLoginAuth(phone3, user_pwd, phoneArea, user_password)
        http = list(a)[-1]
        headers = list(a)[1]  # 将柜台token赋值到headers

        url2 = http + "/as_trade/api/account/v1/to_reset_pwd"
        mailbox = "15989434843@163.com"  # 邮箱
        cardNo = "500234199312083890"  # 身份证号
        paylo = {
            "mailbox": mailbox,
            "cardNo": cardNo
        }

        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload2 = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url2, headers=headers, data=payload2, title="重置交易密码-步骤一"
        )

        k = r.json()
        # print(k)

        assert r.status_code == 200
        if k.get("code") == "000000":
            assert k.get("code") == "000000"
            assert k.get("msg") == "ok"

            schema = k
            try:
                validate(instance=ToResetPwd01Schema, schema=schema, format_checker=draft7_format_checker)
            except SchemaError as e:
                return 1, f"验证模式schema出错：\n出错位置：{'--> '.join([i for i in e.path])}\n提示信息：{e.message}"
            except ValidationError as e:
                return 1, f"json数据不符合schema规定：\n出错字段：{'-->'.join([i for i in e.path])}\n提示信息：{e.message}"
            else:
                return 0, "success!"

        else:
            raise AssertionError(k)
