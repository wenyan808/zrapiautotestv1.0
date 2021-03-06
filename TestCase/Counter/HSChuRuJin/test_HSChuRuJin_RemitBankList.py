# test_HSChuRuJin_RemitBankList
import json

import allure
import pytest

from Common.Accountcommon.accountAuth import AccountAuth
from Common.getTestLoginToken import gettestLoginToken
from Common.sign import get_sign

from Common.requests_library import Requests

from glo import JSON_dev


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_交易入金汇款银行查询')
class TestHSChuRuJinRemitBankList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_HSChuRuJinRemitBankList(self):
        http = list(AccountAuth())[-1]
        url = http + "/as_trade/api/remit_bank/v1/list"
        # 拼装参数
        headers = {}
        headers.update(JSON_dev)

        headers1 = {}
        token = {"token": gettestLoginToken()}
        headers1.update(headers)
        headers1.update(token)  # 将token更新到headers
        # print(headers)
        paylo = {}

        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload2 = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers1, data=payload2, title="交易入金汇款银行查询"
        )

        j = r.json()

        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("msg") == 'ok'
            assert j.get("code") == "000000"
        except:
            raise AssertionError(j)
