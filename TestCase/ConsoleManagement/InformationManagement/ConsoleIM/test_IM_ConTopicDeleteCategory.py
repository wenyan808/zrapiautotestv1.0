# test_IM_ConTopicDeleteCategory    删除专题分类     /api/con_topic/v1/delete_category
import json
import logging
import random

import allure
import pytest

from Common.ConTopic_common.add_contopic_category import add_category
from Common.ConTopic_common.get_ConTopicCategoryId import get_ConTopicCategoryId
from Common.getConsoleLogin import getConsoleLogin_token

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_HTTP, BASE_DIR, console_JSON


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('资讯console_移除专题分类')
class TestIMConTopicDeleteCategory():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    # @pytest.mark.parametrize('info',
    #                          get_json(BASE_DIR + r"/TestData/testIMData/test_IM_conNewsList.json"))
    def test_IM_ConTopicDeleteCategory(self):
        url = console_HTTP + "/api/con_topic/v1/delete_category"
        header = console_JSON


        headers = {}
        headers.update(header)

        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # list1 = list(get_ConTopicCategoryId())
        add_category(headers, "自动化测试分类移除")
        categoryId = get_ConTopicCategoryId(headers, 0)
        paylo = {
            "categoryId": categoryId
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)
        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="删除专题分类"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        assert j.get("data") == True
