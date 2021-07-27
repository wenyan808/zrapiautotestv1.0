# test_Community_conReportHandle
"""
@File  ：test_Community_conReportHandle.py
@Author: yishouquan
@Time  : 2020/7/26
@Desc  :  社区console_举报处理
"""
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
@allure.feature('社区console_举报处理')
class TestCommunityConReportHandle():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/test_communitydata/test_Community_conReportHandle.json"))
    def test_Community_conReportHandle(self, info):
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
        # print(
        # f"\n请求地址：{url}"
        # f"\nbody参数：{payload}"
        # f"\n请求头部参数：{headers}"
        # f"\n返回数据结果：{j}")
        handleurl = console_HTTP + "/api/con_report/v1/handle"

        # 拼装参数
        paylohandle = {
            "reportedId": f"{j.get('data').get('list')[0].get('reportedId')}"
        }
        paylo1 = info
        # print(paylo)
        sign1 = {"sign": get_sign(paylohandle)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo1)
        payload1.update(paylohandle)
        payload1.update(sign1)
        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=handleurl, headers=headers, data=payload, title="举报处理"
        )

        jhandle = r.json()
        # print(jhandle)

        assert r.status_code == 200
        try:

            assert jhandle.get("code") == "000000"
            assert jhandle.get("msg") == "ok"
        except:

            assert jhandle.get("code") == "460603"
            assert jhandle.get("msg") == "内容已被处理"
