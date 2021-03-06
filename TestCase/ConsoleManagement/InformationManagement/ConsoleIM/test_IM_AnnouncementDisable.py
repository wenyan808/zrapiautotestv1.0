# test_IM_AnnouncementDisable
import json
import logging
import random

import allure
import pytest

from Common.getConsoleLogin import getConsoleLogin_token
from Common.get_time_stamp import get_time_stamp13, TimeTostamp

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_JSON, console_HTTP, BASE_DIR


@pytest.mark.skip(reason="调试中 ")
@allure.feature('资讯console_删除恢复公告')
class TestIMAnnouncementDisable():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/testIMData/test_IM_AnnouncementDisable.json"))
    def test_IM_AnnouncementDisable(self, info):
        url = console_HTTP + "/api/con_stock_announcement/v1/list"
        header = console_JSON

        headers = {}
        headers.update(header)
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        market = info.get("market")  # 股票市场(1, "港股"), (2, "美股"), (3, "沪深")
        code = info.get("code")
        # category = 1
        paylo = {
            "code": code,
            "pageSize": 20,
            "currentPage": 1,
            # "category":category,
            # "startTime": TimeTostamp(),
            # "endTime": get_time_stamp13(),
            "market": market
        }

        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        # payload1.update(paylo1)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r0 = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="查询资讯列表"
        )

        j = r0.json()

        # print(f"\n请求地址：{url}"
        #       f"\nbody参数：{payload}"
        #       f"\n请求头部参数：{headers}"
        #       f"\n返回数据结果：{j}")
        # print(j.get('data').get('list')[0].get('annexId'))
        url_disable = console_HTTP + "/api/con_stock_announcement/v1/disable"
        paylo_disable = {
            "annexId": f"{j.get('data').get('list')[0].get('annexId')}"
        }
        paylo_disable1 = {"status": info.get("status")}
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo_disable)
        payload1.update(paylo_disable1)
        payload1.update(sign1)
        payload2 = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url_disable, headers=headers, data=payload2, title="删除恢复公告"
        )
        # print(f"\n请求地址：{url}"
        #       f"\nbody参数：{payload}"
        #       f"\n请求头部参数：{headers}"
        #       f"\n返回数据结果：{r.json()}")
        assert r.status_code == 200
        assert r.json().get("code") == "000000"
        assert r.json().get("msg") == "ok"
        assert r.json().get("data") == True
