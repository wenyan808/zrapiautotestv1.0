# test_Community_AddSensitiveWord
import json
import random

import allure
import pytest

from Common.getConsoleLogin import getConsoleLogin_token
from Common.login import login

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_JSON, console_HTTP, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('社区console_修改敏感词')
class TestCommunityAddSensitiveWord():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        login()  # 调用登录接口通过token传出来

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/test_Community_AddSensitiveWord.json"))
    def test_Community_AddSensitiveWord(self, info):
        url = console_HTTP + "/api/con_sensitive_word/v1/add"
        headers = console_JSON

        # 拼装参数
        # paylo = {
        #     "name": "中国共产党",
        #     "type": 1,
        #     "sensitiveType": 2
        # }
        paylo = info
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)
        headers = headers
        # print(token)
        # print(type(token))
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        payload = json.dumps(dict(payload1))
        # time.sleep(60.01)

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="修改敏感词"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        if j.get("code") == "000000":
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
        elif j.get("code") == "460406":
            assert j.get("code") == "460406"
            assert j.get("msg") == "已达敏感词上限200词"
        else:
            raise AssertionError(print(j))
