# test_IM_GetNewsTopicList     查询专题下的资讯     /as_stock_information/api/news/v1/topic_list
import json
import logging
import random

import allure
import pytest

from Common.getConsoleLogin import getConsoleLogin_token
from Common.get_time_stamp import stampToTime

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import BASE_DIR, HTTP, JSON


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('资讯app_查询专题下的资讯')
class TestIMNewsList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/testIMData/test_IM_NewsList.json"))
    def test_IM_NewsList(self, info):
        url = HTTP + "/as_stock_information/api/news/v1/topic_list"
        header = JSON
        header = header
        paylo = info
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)
        headers = {}
        headers.update(header)

        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="查询专题下的资讯"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
