# test_PicksPoolConsole_StatusOut     股票调出           /api/con_stock_pool/v1/status_out
"""
@File  ：test_PicksPoolConsoleStatusOut.py
@Author: yishouquan
@Time  : 2020/8/06
@Desc  :  股票调出
"""
import json
import time

import allure
import pytest

from Common.getConsoleLogin import getConsoleLogin_token

from Common.get_time_stamp import TimeToStamp13
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_HTTP, console_JSON, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('股票调出')
class TestPicksPoolConsoleStatusOut():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

        cls.url = console_HTTP + "/api/con_stock_pool/v1/status_out"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info', get_json(BASE_DIR +
                                              r"/TestData/PicksPoolConsoleData/test_PicksPoolConsole_StatusOut.json"))
    def test_PicksPoolConsole_StatusOut(self, info):
        # login()  # 调用登录接口通过token传出来
        headers = {}
        headers.update(console_JSON)

        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        code = info.get("code")  # 股票代码
        ts = info.get("ts")  # 市场（HK/US/SH/SZ）
        reason = info.get("reason")  # 调出理由
        id = info.get("id")  # 主键id

        paylo = {
            "code": code,
            "ts": ts,
            "reason": reason,
            "id": id
        }

        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=self.url, headers=headers, data=payload, title="股票调出"
        )
        j = r.json()
        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("msg") == "ok"
            assert j.get("code") == "000000"

        except:
            raise AssertionError(
                f"\n请求地址：{self.url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}")
