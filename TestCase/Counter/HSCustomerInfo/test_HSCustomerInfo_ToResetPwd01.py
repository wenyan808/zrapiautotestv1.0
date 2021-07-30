# test_HSCustomerInfo_ToResetPwd01   重置交易密码-步骤一    /as_trade/api/account/v1/to_reset_pwd
import json

import allure
from jsonschema import validate, draft7_format_checker, SchemaError, ValidationError

from Common.Accountcommon.accountAuth import UserLoginAuth
from Common.assertapi import assert_data, jsonschema_assert

from Common.sign import get_sign

from Common.requests_library import Requests

from TestAssertions.CounterJsonSchemadata.HSCustomerInfo.ToResetPwd01Schema import ToResetPwd01Schema

from glo import phone3, pwd3, phoneArea, user_password


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_忘记交易密码-步骤一')
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
            url=url2, headers=headers, data=payload2, title="忘记交易密码-步骤一"
        )

        k = r.json()
        # print(k)

        assert r.status_code == 200
        try:
            # assert k.get("code") == "000000"
            jsonschema_assert(k.get("code"), k.get("msg"), k, ToResetPwd01Schema)

        except:
            raise AssertionError(f"\n请求地址：{url2}"
                                 f"\nbody参数：{payload2}"
                                 f"\n请求头部参数：{headers}"
                                 f"\n返回数据结果：{k}")
