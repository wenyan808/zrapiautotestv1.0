# test_IM_NewsFastList
import json
import logging

import allure
import pytest

from Common.getConsoleLogin import getConsoleLogin_token


from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import BASE_DIR, HTTP, JSON


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('资讯app_查询快讯资讯分类')
class TestIMNewsFastList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/testIMData/test_IM_NewsFastList.json"))
    def test_IM_NewsFastList(self, info):
        url = HTTP + "/as_stock_information/api/news/v1/fast_list"
        header = JSON

        # 拼装参数
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
        # print(headers)
        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="查询快讯资讯分类"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        if "data" in j:
            if len(j.get("data")) != 0:
                for i in range(len(j.get("data"))):
                    assert "newsId" in j.get("data")[i]
                    assert "title" in j.get("data")[i]
                    assert "content" in j.get("data")[i]
                    assert "source" in j.get("data")[i]
                    assert "pubTime" in j.get("data")[i]
                    assert "readCount" in j.get("data")[i]
                    assert "important" in j.get("data")[i]

            else:
                logging.info("data为空")
        else:
            logging.info("data不在j中")
