# test_Community_UserForbidList
import json
import logging
import random

import allure
import pytest

from Common.getConsoleLogin import getConsoleLogin_token

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_JSON, console_HTTP, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('社区console_禁用列表')
class TestCommunityUserForbidList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/testCommunityData/test_Community_UserForbidList.json"))
    def test_Community_UserForbidList(self, info):
        url = console_HTTP + "/api/con_user_forbid/v1/list"
        header = console_JSON

        # 拼装参数
        # paylo = {}
        paylo = info
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)
        headers = {}
        headers.update(header)
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
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        if "data" in j:
            if len(j.get("data")) != 0:
                assert "list" in j.get("data")
                assert "total" in j.get("data")
                assert "pageSize" in j.get("data")
                assert "currentPage" in j.get("data")
                for i in range(len(j.get("data").get("list"))):
                    assert "userId" in j.get("data").get("list")[i]
                    assert "zrNo" in j.get("data").get("list")[i]
                    assert "nickname" in j.get("data").get("list")[i]
                    assert "phoneArea" in j.get("data").get("list")[i]
                    assert "phone" in j.get("data").get("list")[i]
                    assert "reportNum" in j.get("data").get("list")[i]
                    assert "shieldNum" in j.get("data").get("list")[i]
                    assert "behaviors" in j.get("data").get("list")[i]
                    assert "realName" in j.get("data").get("list")[i]
                    assert "forbid" in j.get("data").get("list")[i]
                    assert "forbidEndTime" in j.get("data").get("list")[i]
                    assert "forbidStartTime" in j.get("data").get("list")[i]
                    assert "reportBehavior" in j.get("data").get("list")[i]
                    assert "limitFlowBehavior" in j.get("data").get("list")[i]
                    assert "duplicateBehavior" in j.get("data").get("list")[i]
                    assert "blockBehavior" in j.get("data").get("list")[i]
            else:
                logging.info("list为空list")
        else:
            logging.info("data不在j中")
