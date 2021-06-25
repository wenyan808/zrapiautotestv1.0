# test_Console_ConUserList   app用户信息列表查询   /api/con_user/v1/list
import json
import logging
import random

import allure
import pytest

from Common.getConsoleLogin import getConsoleLogin_token


from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import BASE_DIR, console_HTTP, console_JSON


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('Console_app用户信息列表查询')
class TestConsoleConUserList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/Consoledate/test_Console_ConUserList.json"))
    def test_Console_ConUserList(self, info):
        url = console_HTTP + "/api/con_user/v1/list"
        header = console_JSON
        header = header
        headers = {}
        headers.update(header)
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers

        paylo1 = info
        paylo = {
            "pageSize": 20,
            "currentPage": 1
        }
        paylo.update(paylo1)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="app用户信息列表查询"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
