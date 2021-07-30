# test_IM_ANoticeDetails
import json
import logging
import random

import allure
import pytest

from Common.getConsoleLogin import getConsoleLogin_token
from Common.show_sql import showsql

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json, write_json

from glo import BASE_DIR, HTTP, JSON


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('资讯app_查询单个公告详情')
class TestIMANoticeDetails():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        # code = showsql(
        #     '192.168.1.237', 'root', '123456', 'stock_market',
        #     "select code from t_stock_search where ts='HK';"
        # )
        # random_stock = random.sample(code, 5)
        # code_data = list(map(lambda code: {"code": code[0]}, random_stock))
        # write_json(BASE_DIR + r"/TestData/testIMData/test_IM_ANoticeDetails.json", code_data)

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    # @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/testIMData/test_IM_ANoticeDetails.json"))
    def test_IM_ANoticeDetails(self):
        url = HTTP + "/as_stock_information/api/announcement/v1/list"
        header = {}
        header.update(JSON)

        code = "00700"
        paylo = {
            "code": code,
            "pageSize": 20,
            "market": 1}
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
            url=url, headers=headers, data=payload, title="查询公告列表（个股,自选）"
        )

        j_list = r.json()
        # print(j_list)
        url_details = HTTP + "/as_stock_information/api/announcement/v1/content"

        lineId = j_list.get('data')[0].get('lineId')
        paylo_details = {"lineId": lineId,
                         "market": 1}
        # print(paylo_details)
        sign1 = {"sign": get_sign(paylo_details)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo_details)
        payload1.update(sign1)
        payload = json.dumps(dict(payload1))

        r_details = Requests(self.session).post(
            url=url_details, headers=headers, data=payload, title="查询单个公告详情"
        )

        j = r_details.json()
        # print(j)
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        if "data" in j:
            if len(j.get("data")) != 0:
                for i in range(len(j.get("data"))):
                    # assert "annexId" in j.get("data")
                    # assert j.get("data").get("annexId") == int(paylo_details.get("id"))
                    assert "announceName" in j.get("data")[i]
                    assert "pubDate" in j.get("data")[i]
                    assert "announceContent" in j.get("data")[i]
                    assert "code" in j.get("data")[i]
                    assert "market" in j.get("data")[i]
                    assert j.get("data")[i].get("market") == paylo_details.get("market")
                    assert "ts" in j.get("data")[i]

            else:
                logging.info("data为空")
        else:
            logging.info("data不在j中")
