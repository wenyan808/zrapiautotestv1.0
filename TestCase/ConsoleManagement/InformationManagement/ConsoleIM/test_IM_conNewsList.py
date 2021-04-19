# test_IM_conNewsList
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
@allure.feature('资讯console_查询资讯列表')
class TestIMConNewsList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/testIMData/test_IM_conNewsList.json"))
    def test_IM_conNewsList(self, info):
        url = console_HTTP + "/api/con_news/v1/list"
        header = console_JSON
        header = header

        # 拼装参数
        # paylo = {
        #     "startTime":20,
        #     "endTime":1
        # }
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
            url=url, headers=headers, data=payload, title="查询资讯列表"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        if "data" in j:
            if len(j.get("data")) != 0:
                assert "list" in j.get("data")
                if "list" in j.get("data"):
                    if j.get("data").get("list") != None:
                        for i in range(len(j.get("data").get("list"))):
                            assert "newsId" in j.get("data").get("list")[i]
                            assert "title" in j.get("data").get("list")[i]
                            assert "content" in j.get("data").get("list")[i]
                            assert "source" in j.get("data").get("list")[i]
                            assert "ts" in j.get("data").get("list")[i]
                            assert "themeImg" in j.get("data").get("list")[i]
                            assert "pubTime" in j.get("data").get("list")[i]
                            assert "updateTime" in j.get("data").get("list")[i]
                            assert "readCount" in j.get("data").get("list")[i]
                            assert "provider" in j.get("data").get("list")[i]
                            assert "status" in j.get("data").get("list")[i]
                            assert "types" in j.get("data").get("list")[i]
                            assert "codes" in j.get("data").get("list")[i]
                            assert "stockNameVos" in j.get("data").get("list")[i]
                            assert "important" in j.get("data").get("list")[i]
                            assert "url" in j.get("data").get("list")[i]
                    else:
                        logging.info("list为空")
                else:
                    logging.info("list不在data中")
            else:
                logging.info("data为空")
        else:
            logging.info("data不在j中")
