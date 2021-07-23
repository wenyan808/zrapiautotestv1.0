# test_HSConMoneyExchange_List      列表    /api/con_money_exchange/v1/list
import json


import allure
import pytest

from Common.getConsoleLogin import getConsoleLogin_token
from Common.get_time_stamp import TimeTostamp, get_time_stamp13


from Common.sign import get_sign

from Common.requests_library import Requests

from glo import console_JSON, console_HTTP


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('恒生3.0-货币兑换(console)_列表')
class TestHSConMoneyExchangeList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        cls.url = console_HTTP + "/api/con_money_exchange/v1/list"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_HSConMoneyExchange_List(self):
        # 拼装参数
        header = console_JSON
        header = header
        headers = {}
        headers.update(header)

        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        currentPage = 20  # 每页条数
        pageSize = 1  # 当前页码
        zrNo = ""  # 卓锐号
        cardName = ""  # 姓名
        moneyType = ""  # 源币种类别   HKD,USD,CNY
        status = 1  # 1、待审核（处理中） 2、已通过 3、已驳回
        toMoneyType = "HKD"  # 目标币种   HKD,USD,CNY
        createStartTime = TimeTostamp()  # 开始时间(时间戳)
        createEndTime = get_time_stamp13()  # 截止时间(时间戳)
        paylo = {
            "currentPage": currentPage,
            "pageSize": pageSize,
            "zrNo": zrNo,
            "cardName": cardName,
            "moneyType": moneyType,
            "status": status,
            "toMoneyType": toMoneyType,
            "createStartTime": createStartTime,
            "createEndTime": createEndTime
        }

        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=self.url, headers=headers, data=payload, title="列表"
        )

        j = r.json()

        # print(j)
        assert r.status_code == 200
        if j.get("code") == "000000":
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
        else:
            raise AssertionError(j)
