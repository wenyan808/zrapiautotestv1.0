import json
import allure
from Common.assertapi import assert_data
from Common.login import login, login_all
from Common.sign import get_sign
from Common.requests_library import Requests
from Common.tools.read_write_yaml import yamltoken, yamlconfig, write_yaml
from TestAssertions.CounterJsonSchemadata.HSCustomerInfo.GetFundsInfoSchema import GetFundsInfoSchema

# @pytest.mark.skip(reason="调试中 ")
import glo


@allure.feature('修改交易密码')
class TestHSCustomerInfoChangeTradePwd():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        http = glo.HTTP
        url = http + "/as_user/api/user_account/v1/user_login_pwd"
        login_all("phone", "15816263996", "zr123456", url, "/TestData/token")
        cls.url = http + "/as_trade/api/account/v1/change_trade_pwd"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_HSCustomerInfo_GetFundsInfo(self):
        header = glo.JSON
        headers = {}
        headers.update(header)
        token = {"token": yamltoken()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        # if yamlconfig("flag"):
        #     newPassword = "111111"
        #     oldPassword = "123456"
        #     write_yaml("flag", "")
        # else:
        #     oldPassword = "111111"
        #     newPassword = "123456"
        #     write_yaml("flag", "1")
        payloa = {
            "newPassword": "111111",
            "oldPassword": "123456"
        }
        paylo = {
            "newPassword": "123456",
            "oldPassword": "111111"
        }
        # print(payloa)
        sign = {"sign": get_sign(payloa)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(payloa)
        payload1.update(sign)
        payload = json.dumps(dict(payload1))
        sign1 = {"sign": get_sign(paylo)}
        payloa = {}
        payloa.update(paylo)
        payloa.update(sign1)
        payloa1 = json.dumps(dict(payloa))
        # 把参数签名后通过sign1传出来
        r = Requests(self.session).post(
            url=self.url, headers=headers, data=payload, title="修改交易密码"
        )
        # k = r.json()
        # print(k)
        r1 = Requests(self.session).post(
            url=self.url, headers=headers, data=payloa1, title="修改交易密码"
        )
        # k1 = r1.json()
        # print(k1)
        # print(f"\n请求地址：{self.url}"
        #       f"\nbody参数：{payload}"
        #       f"\n请求头部参数：{headers}")
        assert r.status_code == 200
        assert_data(r, "000000", "ok")
