# test_Community_conReportHandleWholeHistory
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
@allure.feature('社区console_(所有举报记录)处置历史')
class TestCommunityConReportHandle():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_Community_conReportHandle(self):
        url = console_HTTP + "/api/con_report/v1/handle_whole_history"
        headers = console_JSON

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
        headers = headers
        # print(token)
        # print(type(token))
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        payload = json.dumps(dict(payload1))
        # time.sleep(60.01)

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="(所有举报记录)处置历史"
        )

        j = r.json()
        # print(j)

        assert r.status_code == 200
        if j.get("code") == "000000":
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
            if "data" in j:
                assert j.get("data").get("pageSize") == paylo.get("pageSize")
                assert j.get("data").get("currentPage") == paylo.get("currentPage")
                assert "total" in j.get("data")
                if "list" in j.get("data"):
                    if len(j.get("data").get("list")) != 0:
                        for i in range(len(j.get("data").get("list"))):
                            assert "id" in j.get("data").get("list")[i]
                            assert "createTime" in j.get("data").get("list")[i]
                            assert "operator" in j.get("data").get("list")[i]
                            assert "handleStatus" in j.get("data").get("list")[i]
                            if "post" in j.get("data").get("list")[i]:
                                assert "articleType" in j.get("data").get("list")[i].get("post")
                                assert "title" in j.get("data").get("list")[i].get("post")
                                assert "content" in j.get("data").get("list")[i].get("post")
                                assert "products" in j.get("data").get("list")[i].get("post")
                                assert "content" in j.get("data").get("list")[i].get("post")
                            assert "reportedUser" in j.get("data").get("list")[i]
                            assert "reportedNickName" in j.get("data").get("list")[i]
                            assert "reportedUserType" in j.get("data").get("list")[i]
                            assert "reportedId" in j.get("data").get("list")[i]
                            assert "reportedUserId" in j.get("data").get("list")[i]

                    else:
                        logging.info("list为空list")


        else:
            raise AssertionError(print(j))
