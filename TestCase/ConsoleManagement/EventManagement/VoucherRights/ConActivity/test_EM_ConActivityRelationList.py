# test_EM_ConActivityRelationList    活动关联母卡券列表    /api/con_activity/v1/relation_list
import json
import logging
import random

import allure
import pytest

from Common.ConsoleEventManagement.ConParentCardList import get_activityId, get_ConParentCardId

from Common.getConsoleLogin import getConsoleLogin_token
from Common.get_time_stamp import getTimeTostamp

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_JSON, console_HTTP, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('活动管理console_活动关联母卡券列表')
class TestEMConActivityRelationList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(
                                 BASE_DIR + r"/TestData/test_EventManagementdata/test_EM_ConActivityRelationList.json"))
    def test_EM_ConActivityRelationList(self, info):
        url = console_HTTP + "/api/con_activity/v1/update"
        header = console_JSON

        headers = {}
        headers.update(header)
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        activityName = int(getTimeTostamp(10))
        parentCardName = int(getTimeTostamp(40))
        virtual = info.get("virtual")

        activityId = get_activityId(headers, 0)  # 活动id
        pageSize = info.get("pageSize")

        currentPage = info.get("currentPage")
        paylo = {
            "activityId": activityId,
            "activityName": activityName,
            "parentCardName": parentCardName,
            "virtual": virtual,
            "currentPage": currentPage,
            "pageSize": pageSize}

        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="活动关联母卡券列表"
        )

        j = r.json()
        print(j)
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
