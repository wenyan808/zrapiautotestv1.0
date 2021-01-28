# test_Community_AddUserForbid
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
@allure.feature('社区console_禁言用户')
class TestCommunityAddUserForbid():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/testCommunityData/test_Community_AddUserForbid.json"))
    def test_Community_AddUserForbid(self, info):
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
        # print(j)
        url_add = console_HTTP + "/api/con_user_forbid/v1/add"
        paylo_add = {
            "userId": f"{j.get('data').get('list')[info.get('type')].get('userId')}",
            "timeInterval": info.get("timeInterval")
        }
        sign1 = {"sign": get_sign(paylo_add)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo_add)
        payload1.update(sign1)
        payload = json.dumps(dict(payload1))
        r_add = Requests(self.session).post(
            url=url_add, headers=headers, data=payload, title="禁言用户"
        )
        # print(r_add.json())
        assert r_add.status_code == 200
        if r_add.json().get("code") == "000000":
            assert r_add.json().get("code") == "000000"
            assert r_add.json().get("msg") == "ok"
        elif r_add.json().get("code") == "460501":
            assert r_add.json().get("code") == "460501"
            assert r_add.json().get("msg") == "用户已禁言"
        else:
            raise AssertionError(print(r_add.json()))
        url_Cancel = console_HTTP + "/api/con_user_forbid/v1/cancel"
        paylo_Cancel = {
            "userId": f"{j.get('data').get('list')[info.get('type')].get('userId')}"
        }
        ign1 = {"sign": get_sign(paylo_Cancel)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo_Cancel)
        payload1.update(sign1)
        payload = json.dumps(dict(payload1))
        r_Cancel = Requests(self.session).post(
            url=url_Cancel, headers=headers, data=payload, title="取消禁言用户"
        )
        # print(r_Cancel.json())
        assert r_Cancel.status_code == 200
        if r_Cancel.json().get("code") == "000000":
            assert r_Cancel.json().get("msg") == "ok"

        else:
            raise AssertionError(r_Cancel.json())
