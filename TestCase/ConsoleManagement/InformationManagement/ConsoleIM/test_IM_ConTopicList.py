# test_IM_ConTopicList      查询专题列表(可根据分类id查询专题)     /api/con_topic/v1/list
import json
import logging
import random

import allure
import pytest

from Common.ConTopic_common.Deletes import delete_ConTopicID
from Common.getConsoleLogin import getConsoleLogin_token

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_JSON, console_HTTP, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('资讯console_查询专题列表(可根据分类id查询专题)')
class TestIMConTopicList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    # @pytest.mark.parametrize('info',
    #                          get_json(BASE_DIR + r"/TestData/testIMData/test_IM_conNewsList.json"))
    def test_IM_ConTopicList(self):
        url = console_HTTP + "/api/con_topic/v1/list"
        header = console_JSON
        header = header

        headers = {}
        headers.update(header)

        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        currentPage = 1
        pageSize = 20
        # {"name": name,
        #  "category_id": category_id,
        #  "isHot": isHot}
        paylo = {
            "currentPage": currentPage,
            "pageSize": pageSize

        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)
        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="查询专题列表(可根据分类id查询专题)"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        if "data" in j:
            assert "list" in j.get("data")
            if len(j.get("data").get("list")) != 0:
                for i in range(len(j.get("data").get("list"))):
                    assert "id" in j.get("data").get("list")[i]
                    assert "categoryId" in j.get("data").get("list")[i]
                    assert "name" in j.get("data").get("list")[i]
                    assert "description" in j.get("data").get("list")[i]
                    assert "categoryName" in j.get("data").get("list")[i]
                    assert "sort" in j.get("data").get("list")[i]
                    assert "type" in j.get("data").get("list")[i]
                    assert "headImg" in j.get("data").get("list")[i]
                    assert "backgroundImg" in j.get("data").get("list")[i]
                    if j.get("data").get("list")[i].get("name") == "自动化测试专题":
                        id = j.get("data").get("list")[i].get("id")
                        delete_ConTopicID(id)
                    elif j.get("data").get("list")[i].get("name") == "自动化测试专题01":
                        id = j.get("data").get("list")[i].get("id")
                        delete_ConTopicID(id)
