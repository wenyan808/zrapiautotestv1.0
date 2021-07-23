# test_HSConMoneyExchange_AuditPass        通过      /api/con_money_exchange/v1/audit_pass
import json

import allure
import pytest

from Common.getConsoleLogin import getConsoleLogin_token
from Common.get_time_stamp import TimeTostamp, get_time_stamp13


from Common.sign import get_sign

from Common.requests_library import Requests

from glo import console_JSON, console_HTTP


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('恒生3.0-货币兑换(console)_通过')
class TestHSConMoneyExchangeAuditPass():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        cls.url = console_HTTP + "/api/con_money_exchange/v1/list"
        cls.url1 = console_HTTP + "/api/con_money_exchange/v1/audit_pass"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_HSConMoneyExchange_AuditPass(self):

        # 拼装参数
        header = console_JSON
        header = header
        headers = {}
        headers.update(header)

        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)

        toMoneyType = "CNY"  # 目标币种   HKD,USD,CNY
        createStartTime = TimeTostamp()  # 开始时间(时间戳)
        createEndTime = get_time_stamp13()  # 截止时间(时间戳)
        paylo = {
            "toMoneyType": toMoneyType,
            "createStartTime": createStartTime,
            "createEndTime": createEndTime,
        }

        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r_data = Requests(self.session).post(
            url=self.url, headers=headers, data=payload, title="列表"
        )

        j = r_data.json()
        assert j.get("msg") == "ok"
        assert j.get("code") == "000000"
        if "data" in j:
            exchangeId = j.get("data").get("list")[0].get("exchangeId")
            body = {
                "exchangeId": exchangeId
            }
            sign1 = {"sign": get_sign(body)}  # 把参数签名后通过sign1传出来
            payload2 = {}
            payload2.update(body)
            payload2.update(sign1)

            payload3 = json.dumps(dict(payload2))
            r = Requests(self.session).post(
                url=self.url1, headers=headers, data=payload3, title="通过"
            )

            k = r.json()
            # print(k)
            assert r.status_code == 200
            if k.get("code") == "000000":
                assert k.get("code") == "000000"
                assert k.get("msg") == "ok"
            else:
                raise AssertionError(k)
        else:
            print("兑换列表为空")