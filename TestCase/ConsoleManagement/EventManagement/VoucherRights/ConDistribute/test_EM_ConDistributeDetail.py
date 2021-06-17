# test_EM_ConDistributeDetail     定向派发基础信息（二期）    /api/con_distribute/v1/detail
import json
import logging
import random

import allure
import pytest

from Common.ConsoleEventManagement.ConParentCardList import get_distributeIdlist

from Common.getConsoleLogin import getConsoleLogin_token


from Common.sign import get_sign

from Common.requests_library import Requests

from glo import console_JSON, console_HTTP


# @pytest.mark.skip(reason="调试中")
@allure.feature('活动管理console_定向派发基础信息（二期）')
class TestEMConDistributeDetail():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_EM_ConDistributeDetail(self):
        url = console_HTTP + "/api/con_distribute/v1/detail"
        header = console_JSON
        headers = {}
        headers.update(header)
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers

        distributeId = get_distributeIdlist(headers, 0)
        paylo = {
            "distributeId": distributeId
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="定向派发基础信息（二期）"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
