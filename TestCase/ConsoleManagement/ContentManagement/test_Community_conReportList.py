# test_Community_conReportList
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
@allure.feature('社区console_举报列表(帖子,评论,回复))')
class TestCommunityConReportList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/testCommunityData/test_Community_conReportList.json"))
    def test_Community_conReportList(self, info):
        url = console_HTTP + "/api/con_community_report/v1/list"
        headers = console_JSON
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)

        currentPage = info.get("currentPage")
        pageSize = info.get("pageSize")
        contentType = info.get("contentType")
        sort = info.get("sort")
        paylo = {
            "currentPage": currentPage,
            "pageSize": pageSize,
            "contentType": contentType,
            ''"sort": sort
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="举报列表(帖子,评论,回复)"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
            if "data" in j:
                assert j.get("data").get("pageSize") == paylo.get("pageSize")
                assert j.get("data").get("currentPage") == paylo.get("currentPage")
                assert "total" in j.get("data")
                if "list" in j.get("data"):
                    if len(j.get("data").get("list")) != 0:
                        for i in range(len(j.get("data").get("list"))):
                            assert "reportId" in j.get("data").get("list")[i]
                            assert "contentId" in j.get("data").get("list")[i]
                            assert "contentType" in j.get("data").get("list")[i]
                            # if "postDetail" in j.get("data").get("list")[i]:
                            #     assert "postDetail" in j.get("data").get("list")[i]
                            # if "postId" in j.get("data").get("list")[i].get("postDetail"):
                            #     assert "postId" in j.get("data").get("list")[i].get("postDetail")
                            # assert "articleType" in j.get("data").get("list")[i].get("postDetail")
                            # if "images" in j.get("data").get("list")[i].get("postDetail"):
                            #     assert "images" in j.get("data").get("list")[i].get("postDetail")
                            # assert "publishTime" in j.get("data").get("list")[i].get("postDetail")
                            # assert "praiseNum" in j.get("data").get("list")[i].get("postDetail")
                            # assert "shareNum" in j.get("data").get("list")[i].get("postDetail")
                            # assert "commentNum" in j.get("data").get("list")[i].get("postDetail")
                            # assert "firstCommentNum" in j.get("data").get("list")[i].get("postDetail")
                            # # assert "products" in j.get("data").get("list")[i]
                            # # assert "hot" in j.get("data").get("list")[i]
                            # # assert "content" in j.get("data").get("list")[i]
                            # # assert "ts" in j.get("data").get("list")[i]
                            # # assert "status" in j.get("data").get("list")[i]
                            # # assert "code" in j.get("data").get("list")[i]
                            # # assert "creatorId" in j.get("data").get("list")[i]
                            # # assert "reportType" in j.get("data").get("list")[i]
                            # # assert "processedCount" in j.get("data").get("list")[i]
                            # # assert "reportTime" in j.get("data").get("list")[i]

                    else:
                        logging.info("list为空list")

        except:
            raise AssertionError(
                f"\n请求地址：{url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}")
