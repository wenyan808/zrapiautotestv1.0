# test_IM_AnnounceList
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

from glo import BASE_DIR, HTTP, JSON


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('资讯app_查询公告列表（个股,自选）')
class TestIMAnnounceList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/testIMData/test_IM_AnnounceList.json"))
    def test_IM_AnnounceList(self, info):
        url = HTTP + "/as_stock_information/api/announcement/v1/list"
        header = {}
        header.update(JSON)

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
            url=url, headers=headers, data=payload, title="查询公告列表（个股,自选）"
        )

        j = r.json()
        # print(
        #     f"\n请求地址：{url}"
        #     f"\nbody参数：{payload}"
        #     f"\n请求头部参数：{headers}"
        #     f"\n返回数据结果：{j}"
        # )
        assert r.status_code == 200
        try:
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
            if "data" in j:
                if len(j.get("data")) != 0:
                    for i in range(len(j.get("data"))):
                        assert "id" in j.get("data")[i]
                        assert "lineId" in j.get("data")[i]
                        assert "announceName" in j.get("data")[i]
                        assert "pubDate" in j.get("data")[i]
                        if "announceContent" in j.get("data")[i]:
                            assert "announceContent" in j.get("data")[i]
                        assert "code" in j.get("data")[i]
                        assert "market" in j.get("data")[i]
                        if "ts" in j.get("data")[i]:
                            assert "ts" in j.get("data")[i]
                        if "stockNameVo" in j.get("data")[i]:
                            assert "ts" in j.get("data")[i].get("stockNameVo")
                            assert "code" in j.get("data")[i].get("stockNameVo")
                            assert "type" in j.get("data")[i].get("stockNameVo")
                            assert "name" in j.get("data")[i].get("stockNameVo")
                        else:
                            logging.info("stockNameVo不在data中")
                        assert "url" in j.get("data")[i]

                else:
                    logging.info("data为空")
            else:
                logging.info("data不在j中")
        except:
            assert j.get("code") == "000103"
            assert j.get("msg") == "参数校验不通过"
        # finally:
        #     raise AssertionError(
        #         f"\n请求地址：{url}"
        #         f"\nbody参数：{payload}"
        #         f"\n请求头部参数：{headers}"
        #         f"\n返回数据结果：{j}")
