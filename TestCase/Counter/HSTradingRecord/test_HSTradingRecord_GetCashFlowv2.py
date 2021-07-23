import json

import allure
import pytest

from Common.Accountcommon.accountAuth import AccountAuth
from Common.get_time_stamp import TimeTostamp, get_time_stamp13

from Common.sign import get_sign

from Common.requests_library import Requests

from Common.tools.read_write_json import get_json
from glo import BASE_DIR


# @pytest.mark.skip(reason="废弃")
@allure.feature('柜台app_交易流水v2')
class TestHSTradingRecordGetCashFlow():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR +
                                      r"/TestData/Counterdata/HSTradingRecorddata/"
                                      r"test_HSTradingRecord_GetCashFlowv2data.json"))
    def test_HSTradingRecord_GetCashFlow(self, info):
        # 拼装参数
        http = list(AccountAuth())[-1]

        headers = list(AccountAuth())[1]  # 将柜台token赋值到headers

        url = http + "/as_trade/api/cash_flow/v2/get_cash_flow"
        moneyType = info.get("moneyType")
        businessFlag = info.get("businessFlag")  # 业务类型：1-入金，2-出金，3-证券买入，4-证券卖出，5-换汇、6-ipo
        startDate = TimeTostamp()  # 开始时间，时间戳
        endDate = get_time_stamp13()  # 截止时间，时间戳
        market = info.get("market")  # 市场：1-港 2-美 3-沪深
        paylo = {
            "moneyType": moneyType,
            "businessFlag": businessFlag,
            "startDate": startDate,
            "endDate": endDate,
            "market": market
        }

        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload2 = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload2, title="交易流水v2"
        )

        k = r.json()
        # print(k)
        assert r.status_code == 200
        if k.get("code") == "000000":
            assert k.get("code") == "000000"
            assert k.get("msg") == "ok"
        else:
            raise AssertionError(k)
