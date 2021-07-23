# test_HSChuRuJin_FundDw      资金存取     /as_trade/api/fund/v1/fund_dw
import json

import allure
import pytest

from Common.Accountcommon.accountAuth import AccountAuth
from Common.getTestLoginToken import gettestLoginToken
from Common.sign import get_sign

from Common.requests_library import Requests

from glo import JSON_dev


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_资金存取')
class TestHSChuRuJinFundDw():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_HSChuRuJinFundDw(self):
        http = list(AccountAuth())[-1]
        url = http + "/as_trade/api/remit_bank/v1/list"
        # 拼装参数
        headers = JSON_dev
        headers = headers
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

        r_info = Requests(self.session).post(
            url=url, headers=headers1, data=payload2, title="交易入金汇款银行查询"
        )

        k = r_info.json()
        # print(k)
        url1 = http + "/as_trade/api/fund/v1/fund_dw"
        businessType = "0"  # 业务类型： 0 -存   1-取（暂时不做）
        occurBalance = 10000  # 发生金额
        moneyType = "USD"  # 币种类别:HKD,CNY,USD
        bankId = k.get("data")[0].get("bankId")  # 银行id
        boby = {
            "businessType": businessType,
            "occurBalance": occurBalance,
            "moneyType": moneyType,
            "bankId": bankId
        }
        headers2 = list(AccountAuth())[1]
        sign1 = {"sign": get_sign(boby)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(boby)
        payload1.update(sign1)

        payload3 = json.dumps(dict(payload1))
        r = Requests(self.session).post(
            url=url1, headers=headers2, data=payload3, title="资金存取"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200

        assert j.get("code") == "000000"
        assert j.get("msg") == 'ok'
