# test_Community_UerBehaviorList
import json
import random

import allure
import pytest

from Common.getConsoleLogin import getConsoleLogin_token


from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_JSON, console_HTTP, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('社区console_查询可疑行为')
class TestCommunityUerBehaviorList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/test_Community_UerBehaviorList.json"))
    def test_Community_UerBehaviorList(self, info):
        url = console_HTTP + "/api/con_user_forbid/v1/list"
        headers = console_JSON

        # 拼装参数
        paylo = {}
        # paylo = info
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
            url=url, headers=headers, data=payload, title="禁用列表"
        )

        j = r.json()
        url_list = console_HTTP + "/api/con_user_behavior/v1/list"

        # 拼装参数
        paylo_list = {
            "userId": f"{j.get('data').get('list')[info.get('type')].get('userId')}"
        }
        paylolist = info
        # print(paylo)
        sign1 = {"sign": get_sign(paylo_list)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo_list)
        payload1.update(paylolist)
        payload1.update(sign1)
        headers = headers
        payload = json.dumps(dict(payload1))

        r_list = Requests(self.session).post(
            url=url_list, headers=headers, data=payload, title="查询可疑行为"
        )

        j_list = r_list.json()
        # print(j)
        assert r_list.status_code == 200
        assert j_list.get("code") == "000000"
        assert j_list.get("msg") == "ok"
