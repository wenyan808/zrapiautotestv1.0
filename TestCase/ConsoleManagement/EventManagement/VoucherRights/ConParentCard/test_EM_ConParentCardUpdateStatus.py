# test_EM_ConParentCardUpdateStatus      修改母卡券状态（二期）    /api/con_parent_card/v1/update_status
import json
import logging
import random

import allure
import pytest

from Common.ConsoleEventManagement.ConParentCardList import get_ConParentCardId
from Common.getConsoleLogin import getConsoleLogin_token

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_JSON, console_HTTP, BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('活动管理console_修改母卡券状态（二期）')
class TestEMConParentCardUpdateStatus():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(
                                 BASE_DIR + r"/TestData/test_EventManagementdata/test_EM_ConParentCardUpdateStatus.json"))
    def test_EM_ConParentCardUpdateStatus(self, info):
        url = console_HTTP + "/api/con_parent_card/v1/update_status"
        header = console_JSON
        headers = {}
        headers.update(header)
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        parentCardId = get_ConParentCardId(headers, 0)
        paylo = info
        paylo1 = {"parentCardId": parentCardId}
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo1)
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="修改母卡券状态（二期）"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"

        except:
            assert j.get("code") == "530100"
            assert j.get("msg") == "母卡券已停用"

        else:
            raise AssertionError(
                f"\n请求地址：{url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}")
