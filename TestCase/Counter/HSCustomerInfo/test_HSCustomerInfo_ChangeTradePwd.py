import json
import allure
from Common.assertapi import assert_data
from Common.login import login
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
        login()
        http = glo.HTTP
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
        if yamlconfig("flag"):
            newPassword = "111111"
            oldPassword = "123456"
            write_yaml("flag", "")
        else:
            oldPassword = "111111"
            newPassword = "123456"
            write_yaml("flag", "1")
        payloa = {
            "newPassword": newPassword,
            "oldPassword": oldPassword
        }
        # print(payloa)
        sign1 = {"sign": get_sign(payloa)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(payloa)
        payload1.update(sign1)
        payload = json.dumps(dict(payload1))
        # 把参数签名后通过sign1传出来
        r = Requests(self.session).post(
            url=self.url, headers=headers, data=payload, title="修改交易密码"
        )
        # k = r.json()
        # print(k)
        # print(f"\n请求地址：{self.url}"
        #       f"\nbody参数：{payload}"
        #       f"\n请求头部参数：{headers}")
        assert r.status_code == 200
        assert_data(r, "000000", "ok")
