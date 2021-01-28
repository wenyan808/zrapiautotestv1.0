# test_Community_conReportHandleHistory
import json
import logging
import random

import allure
import pytest

from Common.getConsoleLogin import getConsoleLogin_token


from Common.sign import get_sign

from Common.requests_library import Requests


from glo import console_JSON, console_HTTP


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('社区console_(举报管理)处置历史')
class TestCommunityConReportHandleHistory():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_Community_conReportHandleHistory(self):
        url = console_HTTP + "/api/con_report/v1/list"
        header = console_JSON

        # 拼装参数
        paylo = {
            "currentPage": 20,
            "pageSize": 1,
            "type": 1
        }
        # paylo = info
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
            url=url, headers=headers, data=payload, title="举报列表(帖子,评论,回复)"
        )

        j = r.json()
        # print(j)
        historyurl = console_HTTP + "/api/con_report/v1/handle_history"

        # 拼装参数
        paylohistory = {
            "currentPage": 20,
            "pageSize": 1,
            "reportedId": f"{j.get('data').get('list')[0].get('reportedId')}"
        }
        # paylo = info
        # print(paylo)
        sign1 = {"sign": get_sign(paylohistory)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylohistory)
        payload1.update(sign1)
        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=historyurl, headers=headers, data=payload, title="(举报管理)处置历史"
        )

        jhistory = r.json()
        # print(jhistory)

        assert r.status_code == 200
        if jhistory.get("code") == "000000":
            assert jhistory.get("code") == "000000"
            assert jhistory.get("msg") == "ok"
            if "data" in jhistory:
                assert jhistory.get("data").get("pageSize") == paylohistory.get("pageSize")
                assert jhistory.get("data").get("currentPage") == paylohistory.get("currentPage")
                assert "total" in jhistory.get("data")
                if "list" in jhistory.get("data"):
                    if len(jhistory.get("data").get("list")) != 0:
                        for i in range(len(jhistory.get("data").get("list"))):
                            assert "reportUser" in jhistory.get("data").get("list")[i]
                            assert "createTime" in jhistory.get("data").get("list")[i]
                            assert "reportUserType" in jhistory.get("data").get("list")[i]
                            assert "reportType" in jhistory.get("data").get("list")[i]

                    else:
                        logging.info("list为空list")

        else:
            raise AssertionError(print(jhistory))