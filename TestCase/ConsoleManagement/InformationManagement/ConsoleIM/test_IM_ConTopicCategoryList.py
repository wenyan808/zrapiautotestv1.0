# test_IM_ConTopicCategoryList          查询所有专题分类     /api/con_topic/v1/category_list
import json
import logging
import random

import allure
import pytest

from Common.ConTopic_common.Deletes import delete_ConTopiccategory
from Common.getConsoleLogin import getConsoleLogin_token

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_JSON, console_HTTP, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('资讯console_查询所有专题分类')
class TestIMConTopicCategoryList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    # @pytest.mark.parametrize('info',
    #                          get_json(BASE_DIR + r"/TestData/testIMData/test_IM_conNewsList.json"))
    def test_IM_ConTopicCategoryList(self):
        url = console_HTTP + "/api/con_topic/v1/category_list"

        header = console_JSON


        headers = {}
        headers.update(header)

        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers

        paylo = {}
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)
        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="查询所有专题分类"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        if "data" in j:
            for i in range(len(j.get("data"))):
                assert "categoryId" in j.get("data")[i]
                assert "name" in j.get("data")[i]
                if j.get("data")[i].get("name") == "自动化测试专题分类":
                    categoryId = j.get("data")[i].get("categoryId")
                    delete_ConTopiccategory(categoryId)
