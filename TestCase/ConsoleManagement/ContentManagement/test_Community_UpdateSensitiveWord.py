# test_Community_UpdateSensitiveWord
import json
import random

import allure
import pytest

from Common.getConsoleLogin import getConsoleLogin_token
from Common.get_time_stamp import TimeTostamp, get_time_stamp13

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_JSON, console_HTTP, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('社区console_修改敏感词')
class TestCommunityUpdateSensitiveWord():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info', get_json(
        BASE_DIR + r"/TestData/testCommunityData/test_Community_UpdateSensitiveWord.json"))
    def test_Community_UpdateSensitiveWord(self, info):
        url_list = console_HTTP + "/api/con_sensitive_word/v1/list"
        header = console_JSON
        headers = {}
        headers.update(header)
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        paylo_list = {
            "startTime": TimeTostamp(),
            "endTime": get_time_stamp13()
        }
        sign1 = {"sign": get_sign(paylo_list)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo_list)
        payload1.update(sign1)
        payload = json.dumps(dict(payload1))
        r_list = Requests(self.session).post(
            url=url_list, headers=headers, data=payload, title="敏感词列表"
        )
        j_list = r_list.json()
        # print(j_list)
        # print(j_list.get('data').get('list')[0].get(id))
        url = console_HTTP + "/api/con_sensitive_word/v1/update"

        # 拼装参数
        paylo = {
            "id": f"{j_list.get('data').get('list')[0].get(id)}"
        }
        paylo1 = info
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(paylo1)
        payload1.update(sign1)
        payload = json.dumps(dict(payload1))

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
