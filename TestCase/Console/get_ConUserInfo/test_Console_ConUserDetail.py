# test_Console_ConUserDetail      查看详情    /api/con_user/v1/detail
import json
import logging
import random

import allure
import pytest

from Common.Consolecommon.get_ConsoleUserId import get_consoleuserId
from Common.getConsoleLogin import getConsoleLogin_token

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import BASE_DIR, console_HTTP, console_JSON


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('Console_查看详情')
class TestConsoleConUserDetail():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/Consoledate/test_Console_ConUserDetail.json"))
    def test_Console_ConUserDetail(self, info):
        url = console_HTTP + "/api/con_user/v1/detail"
        header = console_JSON
        header = header
        headers = {}
        headers.update(header)
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        userId = get_consoleuserId(headers, 0)
        paylo1 = info

        paylo = {
            "userId": userId
        }
        paylo.update(paylo1)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="查看详情"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
