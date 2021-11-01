# test_Community_ConsolePostList     帖子列表         /api/con_post/v1/list
import json
import logging
import random

import allure
import pytest

from Business.Community_URlPath import URlPath_conPostList
from Common.getConsoleLogin import getConsoleLogin_token
from Common.get_payload_headers import get_headers, get_payload

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_JSON, console_HTTP, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('帖子管理(console)_帖子列表')
class TestCommunityConsolePostList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/testCommunityData/test_Community_ConsolePostList.json"))
    def test_Community_ConsolePostList(self, info):
        url = console_HTTP + URlPath_conPostList
        token = {"token": getConsoleLogin_token()}
        headers = get_headers(console_JSON, token)
        paylo = info
        payload = get_payload(paylo)

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="帖子列表"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        if j.get("code") == "000000":
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
