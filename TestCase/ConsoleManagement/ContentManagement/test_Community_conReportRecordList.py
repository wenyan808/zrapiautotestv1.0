# test_Community_conReportRecordList
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
@allure.feature('社区console_举报记录')
class TestCommunityConReportList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_Community_conReportList(self):
        url = console_HTTP + "/api/con_report/v1/list"
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
            url=url, headers=headers, data=payload, title="举报列表(帖子,评论,回复)"
        )

        j = r.json()
        # print(j)
        record_listurl = console_HTTP + "/api/con_report/v1/record_list"

        # 拼装参数
        record_listpaylo = {
            "currentPage": 20,
            "pageSize": 1,
            "reportedId": f"{j.get('data').get('list')[0].get('reportedId')}"
        }
        # paylo = info
        # print(paylo)
        sign1 = {"sign": get_sign(record_listpaylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(record_listpaylo)
        payload1.update(sign1)
        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=record_listurl, headers=headers, data=payload, title="举报记录"
        )

        j_list = r.json()
        # print(j_list)

        assert r.status_code == 200
        if j_list.get("code") == "000000":
            assert j_list.get("code") == "000000"
            assert j_list.get("msg") == "ok"
            if "data" in j_list:
                assert j_list.get("data").get("pageSize") == record_listpaylo.get("pageSize")
                assert j_list.get("data").get("currentPage") == record_listpaylo.get("currentPage")
                assert "total" in j_list.get("data")
                if "list" in j_list.get("data"):
                    if len(j_list.get("data").get("list")) != 0:
                        for i in range(len(j_list.get("data").get("list"))):
                            assert "reportUser" in j_list.get("data").get("list")[i]
                            assert "createTime" in j_list.get("data").get("list")[i]
                            assert "reportUserType" in j_list.get("data").get("list")[i]
                            assert "reportType" in j_list.get("data").get("list")[i]

                    else:
                        logging.info("list为空list")

        else:
            raise AssertionError(print(j_list))

