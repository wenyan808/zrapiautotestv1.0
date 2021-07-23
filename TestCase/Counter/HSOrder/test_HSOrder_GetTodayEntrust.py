# test_HSOrder_GetTodayEntrust       查询当日委托           /as_trade/api/order/v1/get_today_entrust
import json

import allure

from Common.Accountcommon.accountAuth import AccountAuth

from Common.sign import get_sign

from Common.requests_library import Requests


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_查询当日委托')
class TestHSOrderGetTodayEntrust():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_HSOrder_GetTodayEntrust(self):
        http = list(AccountAuth())[-1]
        url = http + "/as_trade/api/order/v1/get_today_entrust"
        # 拼装参数
        headers = list(AccountAuth())[1]  # 将柜台token赋值到headers

        paylo5 = {}
        sign1 = {"sign": get_sign(paylo5)}  # 把参数签名后通过sign1传出来
        payload6 = {}
        payload6.update(paylo5)
        payload6.update(sign1)

        payload7 = json.dumps(dict(payload6))

        r_data = Requests(self.session).post(
            url=url, headers=headers, data=payload7, title="查询当日委托"
        )

        j = r_data.json()
        # print(j)
        assert r_data.status_code == 200
        if j.get("code") == "000000":
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
        else:
            raise AssertionError(j)
