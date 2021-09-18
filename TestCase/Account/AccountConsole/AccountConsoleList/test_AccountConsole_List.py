# test_AccountConsole_List    审核列表    /api/con_open/v1/list
"""
@File  ：test_AccountConsole_List.py
@Author: yishouquan
@Time  : 2021/9/14
@Desc  :  审核列表
"""
import json


import allure
import pytest

from Common.getConsoleLogin import getConsoleLogin_token

from Common.sign import get_sign

from Common.requests_library import Requests

from glo import console_JSON, console_HTTP, loginAccount_phone


# @pytest.mark.skip(reason="废弃")
@allure.feature('开户console_审核列表')
class TestAccountConsoleList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_AccountConsoleList(self):
        url = console_HTTP + "/api/con_open/v1/list"

        # 拼装参数
        headers = console_JSON
        headers = headers
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        phone = loginAccount_phone

        # paylo = {
        #     "phone": phone
        # }
        paylo = {}
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="审核列表"
        )

        j = r.json()
        # print(j)

        assert r.status_code == 200
        if j.get("code") == "000000":
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
            if "data" in j:
                assert "list" in j.get("data")
                for i in range(len(j.get("data").get("list"))):
                    assert "userId" in j.get("data").get("list")[i]
                    assert "openOrderId" in j.get("data").get("list")[i]
                    assert "submitOpenId" in j.get("data").get("list")[i]
                    assert "updateTime" in j.get("data").get("list")[i]
                    assert "cnOpenDTO" in j.get("data").get("list")[i]
                    assert "userAccountDTO" in j.get("data").get("list")[i]
                    assert "openOrderDTO" in j.get("data").get("list")[i]
                    assert "status" in j.get("data").get("list")[i]
                    assert "total" in j.get("data")
                    assert "pageSize" in j.get("data")
                    assert "currentPage" in j.get("data")
                    assert "openStatus" in j.get("data").get("list")[i].get("cnOpenDTO")
                    assert "overseasOpenMode" in j.get("data").get("list")[i].get("cnOpenDTO")
                    assert "nationality" in j.get("data").get("list")[i].get("cnOpenDTO")
                    assert "zrNo" in j.get("data").get("list")[i].get("userAccountDTO")
                    assert "phone" in j.get("data").get("list")[i].get("userAccountDTO")
                    assert "nickname" in j.get("data").get("list")[i].get("userAccountDTO")
                    # assert "firstSubmitTime" in j.get("data").get("list")[i].get("openOrderDTO")
                    # assert "latestSubmitTime" in j.get("data").get("list")[i].get("openOrderDTO")
                    # assert "firstSubmitDuration" in j.get("data").get("list")[i].get("openOrderDTO")
                    # assert "userAccountDTO" in j.get("data").get("list")[i].get("cnOpenDTO")

        else:
            raise AssertionError(j)