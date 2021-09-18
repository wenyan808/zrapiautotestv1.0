# test_HSChuRuJin_FundRecord        资金记录          /as_trade/api/fund/v1/record
import json

import allure
import pytest

from Common.Accountcommon.accountAuth import AccountAuth
from Common.get_time_stamp import TimeToStamp13, gettoday

from Common.sign import get_sign

from Common.requests_library import Requests

# @pytest.mark.skip(reason="调试中 ")
from Common.tools.read_json import get_json
from glo import BASE_DIR


@allure.feature('柜台app_资金记录')
class TestHSChuRuJinFundRecord():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/HSChurujindata/test_HSChuRuJinFundRecord.json"))
    def test_HSChuRuJin_FundRecord(self, info):
        login_list = list(AccountAuth())
        http = login_list[-1]
        headers = login_list[1]

        url = http + "/as_trade/api/fund/v1/record"
        currentPage = info.get("currentPage")  # 当前页，默认1
        pageSize = info.get("pageSize")  # 每页显示条数,默认20
        fundType = info.get("fundType")  # 资金记录类型 0-存入记录 1-提款记录
        moneyType = info.get("moneyType")  # 币种类型 HKD/USD/CNY 不传查全部
        if info.get("createStartTime") == None:
            createStartTime = TimeToStamp13(str(gettoday()) + " 00:00:00")  # 开始时间，时间戳（当天的开始,yyyy-MM-dd 00:00:00 的时间戳）
        else:
            createStartTime = TimeToStamp13(info.get("createStartTime"))
        if info.get("createEndTime") == None:
            createEndTime = TimeToStamp13(str(gettoday()) + " 23:59:59")  # 截止时间，时间戳（（当天的结束,yyyy-MM-dd 23:59:59 的时间戳)
        else:
            createEndTime = TimeToStamp13(info.get("createEndTime"))
        status = info.get("status")  # 状态 1-已完成 2-处理中 3-已拒绝 默认查“所有币种&所有状态”，不传查所有状态
        paylo = {
            "currentPage": currentPage,
            "pageSize": pageSize,
            "fundType": fundType
        }
        paylo1 = {
            "moneyType": moneyType,
            "createStartTime": createStartTime,
            "createEndTime": createEndTime,
            "status": status
        }
        paylo.update(paylo1)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload2 = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload2, title="资金记录"
        )

        j = r.json()

        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("msg") == 'ok'
            assert j.get("code") == "000000"
        except:
            raise AssertionError(j)
