# test_HSOrder_GetAllEntrust        查询所有委托           /as_trade/api/order/v1/get_all_entrust
import json

import allure

from Common.Accountcommon.accountAuth import AccountAuth
from Common.get_time_stamp import TimeTostamp, get_time_stamp13

from Common.sign import get_sign

from Common.requests_library import Requests


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_查询所有委托')
class TestHSOrderGetAllEntrust():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        cls.http = list(AccountAuth())[-1]
        cls.url = cls.http + "/as_trade/api/order/v1/get_all_entrust"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_HSOrder_GetAllEntrust(self):


        # 拼装参数
        headers = list(AccountAuth())[1]  # 将柜台token赋值到headers
        # print(headers)

        startDate = TimeTostamp()
        endDate = get_time_stamp13()
        paylo5 = {
            "startDate": startDate,
            "endDate": endDate
        }
        sign1 = {"sign": get_sign(paylo5)}  # 把参数签名后通过sign1传出来
        payload6 = {}
        payload6.update(paylo5)
        payload6.update(sign1)

        payload7 = json.dumps(dict(payload6))

        r_data = Requests(self.session).post(
            url=self.url, headers=headers, data=payload7, title="查询所有委托"
        )
        # print(j)
        assert r_data.status_code == 200
        if j.get("code") == "000000":
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
        else:
            raise AssertionError(j)
