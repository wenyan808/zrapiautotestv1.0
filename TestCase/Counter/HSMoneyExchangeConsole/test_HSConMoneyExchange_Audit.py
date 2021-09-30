# test_HSConMoneyExchange_Audit    货币兑换审核（初审、终审、拒绝、通过）四合一接口    /api/con_money_exchange/v1/audit
import json

import allure
import pytest

from Common.getConsoleLogin import getConsoleLogin_token
from Common.get_time_stamp import TimeTostamp, get_time_stamp13

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_json import get_json

from glo import console_JSON, console_HTTP, BASE_DIR


# @pytest.mark.skip(reason="废弃 ")
@allure.feature('恒生3.0-货币兑换(console)_货币兑换审核（初审、终审、拒绝、通过）四合一接口')
class TestHSConMoneyExchangeAudit():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        cls.url = console_HTTP + "/api/con_money_exchange/v1/list"
        cls.url1 = console_HTTP + "/api/con_money_exchange/v1/audit"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR +
                                      r"/TestData/Counterdata/HSConMoneyExchange/test_HSHSConMoneyExchange_audit.json"))
    def test_HSConMoneyExchange_Audit(self, info):

        # 拼装参数
        header = console_JSON

        headers = {}
        headers.update(header)

        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)

        currentPage = 1
        paylo = {
            "currentPage": currentPage,
            "pageSize": 20,
            "status": 1,
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
        initiateStatus = info.get("initiateStatus")
        if "data" in j and j.get("data").get("list"):
            exchangeId = j.get("data").get("list")[initiateStatus-1].get("exchangeId")
            body = {
                "exchangeId": exchangeId,
                "initiateStatus": initiateStatus
            }
            sign1 = {"sign": get_sign(body)}  # 把参数签名后通过sign1传出来
            payload2 = {}
            payload2.update(body)
            payload2.update(sign1)

            payload3 = json.dumps(dict(payload2))
            r = Requests(self.session).post(
                url=self.url1, headers=headers, data=payload3, title="货币兑换审核（初审、终审、拒绝、通过）四合一接口"
            )

            k = r.json()
            assert r.status_code == 200
            try:
                assert k.get("code") == "000000"
                assert k.get("msg") == "ok"
            except:
                raise AssertionError(
                    f"\n请求地址：{self.url}"
                    f"\nbody参数：{payload}"
                    f"\n请求头部参数：{headers}"
                    f"\n返回数据结果：{j}"
                )
        else:
            print("兑换列表为空")
