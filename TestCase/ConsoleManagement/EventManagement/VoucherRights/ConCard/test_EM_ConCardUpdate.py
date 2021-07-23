# test_EM_ConCardUpdate   子卡状态更改(二期)    /api/con_card/v1/update
import json
import logging
import random

import allure
import pytest

from Common.ConsoleEventManagement.ConParentCardList import getconCardid

from Common.getConsoleLogin import getConsoleLogin_token


from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_JSON, console_HTTP, BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('活动管理console_子卡状态更改(二期)')
class TestEMConCardUpdate():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(
                                 BASE_DIR +
                                 r"/TestData/test_EventManagementdata/test_EM_ConCardUpdate.json"))
    def test_EM_ConCardUpdate(self, info):
        url = console_HTTP + "/api/con_card/v1/update"
        header = console_JSON
        headers = {}
        headers.update(header)
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers

        cardId = getconCardid(headers, 1)  # 子卡券id
        status = info.get("status")
        paylo = {
            "cardId": cardId,
            "status": status
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="子卡状态更改(二期)"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"

        except:
            assert j.get("code") == "530503"
            assert j.get("msg") == "子卡券已结束"


        else:
            raise AssertionError(
                f"\n请求地址：{url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}")