# test_AccountConsole_GetAuditItem         查询审核项             /api/con_open/v1/get_audit_item
import json

import allure
import pytest

from Common.getConsoleLogin import getConsoleLogin_token

from Common.sign import get_sign

from Common.requests_library import Requests

from glo import console_JSON, console_HTTP


# @pytest.mark.skip(reason="开发中")
@allure.feature('开户console_查询审核项')
class TestAccountConsoleGetOpenAudit():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_AccountConsole_GetOpenAudit(self):
        url = console_HTTP + "/api/con_open/v1/get_audit_item"

        # 拼装参数
        headers = console_JSON
        headers = headers
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        paylo = {}
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="查询审核项"
        )

        j = r.json()
        # print(f"\n返回数据结果：{j}")
        assert r.status_code == 200

        try:
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
            if "data" in j:
                for i in range(len(j.get("data"))):
                    assert "auditItemId" in j.get("data")[i]
                    assert "dataModule" in j.get("data")[i]
                    assert "overseasOpenModes" in j.get("data")[i]
                    assert "content" in j.get("data")[i]
                    assert "sort" in j.get("data")[i]
                    assert "cnPage" in j.get("data")[i]
                    assert "owPage" in j.get("data")[i]
                    assert "cardSide" in j.get("data")[i]
        except:
            raise AssertionError(
                f"\n请求地址：{url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}")
