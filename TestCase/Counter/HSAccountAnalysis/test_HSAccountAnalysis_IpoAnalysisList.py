# test_HSAccountAnalysis_IpoAnalysisList            新股盈亏明细               /as_trade/api/ipo_analysis/v1/list
import json

import allure
import pytest
from Common.sign import get_sign
from Common.requests_library import Requests
from Common.Accountcommon.accountAuth import AccountAuth


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_新股盈亏明细')
class TestHSAccountAnalysisIpoAnalysisList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    # @pytest.mark.parametrize('info',
    #                          get_json(
    #                              BASE_DIR +
    #                              r"/TestData/HSAccountAnalysis/test_HSAccountAnalysis_IpoAnalysisProfit.json"))
    def test_HSAccountAnalysis_IpoAnalysisList(self):
        http = list(AccountAuth())[-1]
        url = http + "/as_trade/api/ipo_analysis/v1/profit"
        # 拼装参数
        headers = list(AccountAuth())[1]

        paylo = {}

        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload2 = json.dumps(dict(payload1))

        r_info = Requests(self.session).post(
            url=url, headers=headers, data=payload2, title="新股盈亏明细"
        )

        j = r_info.json()
        # print(j)
        assert r_info.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == 'ok'
