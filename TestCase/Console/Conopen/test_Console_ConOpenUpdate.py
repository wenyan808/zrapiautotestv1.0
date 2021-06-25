# test_Console_ConOpenUpdate    修改客户开户资料（复审也会用到改接口）    /api/con_open/v1/update
import json
import logging
import random

import allure
import pytest

from Common.Consolecommon.get_ConsoleUserId import get_orderId
from Common.getConsoleLogin import getConsoleLogin_token
from Common.get_time_stamp import gettoday

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import BASE_DIR, console_HTTP, console_JSON


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('console_修改客户开户资料（复审也会用到改接口）')
class TestConsoleConOpenUpdate():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/Consoledate/test_Console_ConOpenUpdate.json"))
    def test_Console_ConOpenUpdate(self, info):
        url = console_HTTP + "/api/con_open/v1/update"
        header = console_JSON
        header = header
        headers = {}
        headers.update(header)
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        orderId = get_orderId(headers, 0)
        paylo1 = info

        paylo = {
            "orderId": orderId
        }
        paylo.update(paylo1)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="修改客户开户资料（复审也会用到改接口）"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
