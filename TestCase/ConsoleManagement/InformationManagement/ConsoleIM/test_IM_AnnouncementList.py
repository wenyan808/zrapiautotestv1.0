# test_IM_AnnouncementList
"""
@File  ：test_IM_AnnouncementList.py
@Author: yishouquan
@Time  : 2020/7/28
@Desc  :  资讯console_查询公告列表
"""
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

from glo import console_JSON, console_HTTP, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('资讯console_查询公告列表')
class TestIMAnnouncementList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/testIMData/test_IM_AnnouncementList.json"))
    def test_IM_AnnouncementList(self,info):
        url = console_HTTP + "/api/con_stock_announcement/v1/list"
        header = console_JSON
        header = header

        # 拼装参数
        # paylo = {
        #     "pageSize": 20,
        #     "currentPage": 1
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
            url=url, headers=headers, data=payload, title="查询公告列表"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
            if "data" in j:
                if len(j.get("data")) != 0:
                    assert "list" in j.get("data")
                    if "list" in j.get("data"):
                        if j.get("data").get("list") != None:
                            for i in range(len(j.get("data").get("list"))):
                                assert "annexId" in j.get("data").get("list")[i]
                                assert "announceId" in j.get("data").get("list")[i]
                                assert "announceName" in j.get("data").get("list")[i]
                                assert "pubDate" in j.get("data").get("list")[i]
                                assert "annexName" in j.get("data").get("list")[i]
                                assert "annexFormat" in j.get("data").get("list")[i]
                                assert "annexUrl" in j.get("data").get("list")[i]
                                assert "announceContent" in j.get("data").get("list")[i]
                                assert "code" in j.get("data").get("list")[i]
                                assert "category" in j.get("data").get("list")[i]
                                assert "market" in j.get("data").get("list")[i]
                                assert "status" in j.get("data").get("list")[i]
                                assert "url" in j.get("data").get("list")[i]
                                assert "stockNameVo" in j.get("data").get("list")[i]
                                assert "ts" in j.get("data").get("list")[i]

                        else:
                            logging.info("list为空")
                    else:
                        logging.info("list不在data中")
                else:
                    logging.info("data为空")
            else:
                logging.info("data不在j中")
        except:
            assert j.get("code") == "000103"
            assert j.get("msg") == "参数校验不通过"
        # else:
        #     raise AssertionError(
        #         f"\n请求地址：{url}"
        #         f"\nbody参数：{payload}"
        #         f"\n请求头部参数：{headers}"
        #         f"\n返回数据结果：{j}"
        #     )