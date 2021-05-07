# test_IM_ConTopicDelete       删除专题     /api/con_topic/v1/delete

import json
import logging
import random

import allure
import pytest

from Common.ConTopic_common.get_ConTopicID import get_ConTopicID

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_HTTP, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('资讯console_删除专题')
class TestIMConTopicDelete():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    # @pytest.mark.parametrize('info',
    #                          get_json(BASE_DIR + r"/TestData/testIMData/test_IM_conNewsList.json"))
    def test_IM_ConTopicDelete(self):
        url = console_HTTP + "/api/con_topic/v1/delete"

        list1 = list(get_ConTopicID())
        headers = list1[1]
        id = list1[0]

        paylo = {
            "id": id
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)
        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="删除专题"
        )

        j = r.json()

        # print(j)
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        assert j.get("data") == True
