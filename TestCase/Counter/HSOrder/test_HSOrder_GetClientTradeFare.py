# test_HSOrder_GetClientTradeFare    获取客户交易费用           /as_trade/api/fare/v1/get_client_trade_fare
import json

import allure

from Common.Accountcommon.accountAuth import AccountAuth
from Common.get_payload_headers import get_payload
from Common.get_time_stamp import TimeTostamp, get_time_stamp13

from Common.sign import get_sign

from Common.requests_library import Requests


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_获取客户交易费用')
class TestHSOrderGetClientTradeFare():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        cls.http = list(AccountAuth())[-1]
        cls.url = cls.http + "/as_trade/api/fare/v1/get_client_trade_fare"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_HSOrder_GetClientTradeFare(self):

        # 拼装参数
        headers = list(AccountAuth())[1]  # 将柜台token赋值到headers
        # print(headers)

        ts = "HK"

        paylo5 = {
            "ts": ts
        }

        payload7 = get_payload(paylo5)

        r_data = Requests(self.session).post(
            url=self.url, headers=headers, data=payload7, title="获取客户交易费用"
        )
        # print(j)
        j = r_data.json()
        assert r_data.status_code == 200
        try:
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
        except:
            raise AssertionError(j)
