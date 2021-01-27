# test_IM_GetNewInfoList    要闻-获取最新的数据
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


@pytest.mark.skip(reason="调试中 ")
@allure.feature('资讯console_要闻-获取最新的数据')
class TestIMGetNewInfoList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/testIMData/test_IM_GetNewInfoList.json"))
    def test_IM_GetNewInfoList(self, info):
        url = console_HTTP + "/as_stock_information/api/important_news/v1/all_info_list_new"
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
            url=url, headers=headers, data=payload, title="要闻-获取最新的数据"
        )

        j = r.json()
        print(url)
        print(headers)
        print(payload)
        print(j)
        # assert r.status_code == 200
        # assert j.get("code") == "000000"
        # assert j.get("msg") == "ok"
        # if "data" in j:
        #     if len(j.get("data")) != 0:
        #         assert "haveNextPage" in j.get("data")
        #         if "baseInformationDtoList" in j.get("data"):
        #             for i in range(len(j.get("data").get("baseInformationDtoList"))):
        #                 assert "uuid" in j.get("data").get("baseInformationDtoList")[i]
        #                 assert "id" in j.get("data").get("baseInformationDtoList")[i]
        #                 assert "title" in j.get("data").get("baseInformationDtoList")[i]
        #                 assert "source" in j.get("data").get("baseInformationDtoList")[i]
        #                 assert "pubTime" in j.get("data").get("baseInformationDtoList")[i]
        #                 assert "category" in j.get("data").get("baseInformationDtoList")[i]
        #                 assert "market" in j.get("data").get("baseInformationDtoList")[i]
        #                 assert "code" in j.get("data").get("baseInformationDtoList")[i]
        #                 assert "url" in j.get("data").get("baseInformationDtoList")[i]
        #
        #         else:
        #             logging.info("baseInformationDtoList不在data中")
        #     else:
        #         logging.info("data为空")
        # else:
        #     logging.info("data不在j中")
