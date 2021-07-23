# test_HSAccountAnalysis_HoldPreference            持仓偏好        /as_trade/api/analysis/v1/hold_preference
import json

import allure

import pytest

from Common.Accountcommon.accountAuth import AccountAuth


from Common.sign import get_sign

from Common.requests_library import Requests

from Common.tools.read_write_json import get_json

from glo import BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_持仓偏好')
class TestHSAccountAnalysisIncomeCurve():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(
                                 BASE_DIR + r"/TestData/HSAccountAnalysis/test_HSAccountAnalysis_HoldPreference.json"))
    def test_HSAccountAnalysis_HoldPreference(self, info):
        http = list(AccountAuth())[-1]
        url = http + "/as_trade/api/analysis/v1/hold_preference"
        # 拼装参数
        headers = list(AccountAuth())[1]

        market = info.get("market")  # 市场类型，（1-港 2-美 3-A，不传查询综合账户分析）

        paylo = {
            "market": market
        }

        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload2 = json.dumps(dict(payload1))

        r_info = Requests(self.session).post(
            url=url, headers=headers, data=payload2, title="持仓偏好"
        )

        j = r_info.json()
        # print(j)
        assert r_info.status_code == 200

        assert j.get("code") == "000000"
        assert j.get("msg") == 'ok'
