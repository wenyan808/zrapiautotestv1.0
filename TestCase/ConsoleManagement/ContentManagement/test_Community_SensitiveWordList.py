# test_Community_SensitiveWordList
import json


import allure
import pytest

from Common.getConsoleLogin import getConsoleLogin_token
from Common.get_time_stamp import TimeTostamp, get_time_stamp13


from Common.sign import get_sign

from Common.requests_library import Requests

from glo import console_JSON, console_HTTP


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('社区console_敏感词列表')
class TestCommunitySensitiveWordList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()


    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_Community_SensitiveWordList(self):
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
        assert j_list.get("code") == "000000"
        assert j_list.get("msg") == "ok"
