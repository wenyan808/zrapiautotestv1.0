# test_Community_SensitiveWordMatch
import json

import allure
import pytest

from Common.getConsoleLogin import getConsoleLogin_token

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_JSON, console_HTTP, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('社区console_敏感词匹配(后台使用)')
class TestCommunitySensitiveWordMatch():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        # login()  # 调用登录接口通过token传出来

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/testCommunityData/test_Community_SensitiveWordMatch.json"))
    def test_Community_SensitiveWordMatch(self, info):
        url = "http://192.168.1.161:1230"
        url_Match = url + "/api/sensitive_word/v1/match"
        headers = {
            "Postman-Token": "<calculated when request is sent>",
            "Content-Type": "application/json;charset=UTF-8",
            "Connection": "keep-alive",
            "Content-Length": "<calculated when request is sent>",
            "Host": "<calculated when request is sent>",
            "Accept": "*/*",
            "User-Agent": "PostmanRuntime/7.26.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        payload = info

        r_Match = Requests(self.session).post(
            url=url_Match, headers=headers, json=payload, title="敏感词匹配(后台使用)"
        )
        j_Match = r_Match.json()
        # print(url_Match)
        # print(headers)
        # print(payload)
        # print(j_Match)
        assert j_Match.get("code") == "000000"
        assert j_Match.get("msg") == "ok"
