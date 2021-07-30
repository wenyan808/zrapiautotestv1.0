# test_IM_NewsContent
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
@allure.feature('资讯app_查询单个资讯详情')
class TestIMNewsContent():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_IM_NewsContent(self):
        url = HTTP + "/as_stock_information/api/news/v1/list"
        header = {}
        header.update(JSON)
        headers = {}
        headers.update(header)
        # print(token)
        # print(type(token))
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)

        # 拼装参数
        paylo = {
            "pageSize": 20,
            "type": 0
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)
        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="查询资讯信息（包含个股，自选股）"
        )

        j_list = r.json()
        # print(j_list)
        # print(j_list.get('data')[0].get('newsId'))
        url_content = HTTP + "/as_stock_information/api/news/v1/content"
        # 拼装参数
        paylo_content = {
            "newsId": f"{j_list.get('data')[0].get('newsId')}"
        }

        sign1 = {"sign": get_sign(paylo_content)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo_content)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url_content, headers=headers, data=payload, title="查询单个资讯详情"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        if "data" in j:
            if len(j.get("data")) != 0:
                assert "newsId" in j.get("data")
                assert "title" in j.get("data")
                assert "content" in j.get("data")
                assert "source" in j.get("data")
                assert "pubTime" in j.get("data")

            else:
                logging.info("data为空")
        else:
            logging.info("data不在j中")
