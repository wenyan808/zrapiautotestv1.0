# test_HSChuRuJin_FundProcedureFee    手续费计算    /as_trade/api/fund/v1/procedure_fee
import json

import allure
import pytest


from Common.Accountcommon.accountAuth import AccountAuth

from Common.assertapi import jsonschema_assert

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_json import get_json
from TestAssertions.CounterJsonSchemadata.HSChuRuJin.FundProcedureFeeSchema import FundProcedureFeeSchema

from glo import BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_手续费计算')
class TestHSChuRuJinFundProcedureFee():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/HSChurujindata/test_HSChuRuJinFundProcedureFee.json"))
    def test_HSChuRuJin_FundProcedureFee(self, info):
        login_list = list(AccountAuth())
        http = login_list[-1]
        headers = login_list[1]

        url = http + "/as_trade/api/fund/v1/procedure_fee"

        occurBalance = info.get("occurBalance")  # 提款金额
        moneyType = info.get("moneyType")  # 货币类型 HKD/USD/CNY
        paylo = {
            "occurBalance": occurBalance,
            "moneyType": moneyType
        }

        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload2 = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload2, title="手续费计算"
        )

        j = r.json()

        # print(j)
        assert r.status_code == 200
        try:
            jsonschema_assert(j.get("code"), j.get("msg"), j, FundProcedureFeeSchema)
        except:
            raise AssertionError(j)