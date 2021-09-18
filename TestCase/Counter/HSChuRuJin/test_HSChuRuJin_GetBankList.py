# test_HSChuRuJin_GetBankList      用户绑定银行卡列表查询       /as_trade/api/bank/v1/list
import json

import allure
import pytest

from Common.Accountcommon.accountAuth import AccountAuth

from Common.sign import get_sign

from Common.requests_library import Requests


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_用户绑定银行卡列表查询')
class TestHSChuRuJinGetBankList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_HSChuRuJin_GetBankList(self):
        login_list = list(AccountAuth())
        http = login_list[-1]
        headers = login_list[1]

        url = http + "/as_trade/api/bank/v1/list"

        paylo = {}

        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload2 = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload2, title="用户绑定银行卡列表查询"
        )

        j = r.json()

        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("msg") == 'ok'
            assert j.get("code") == "000000"
        except:
            raise AssertionError(j)
