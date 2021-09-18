# test_AccountConsole_GetOpenAudit     查询当前用户的审核数据  /api/con_open/v1/get_open_audit
import json

import allure
import pytest

from Common.Accountcommon.getAccountConsoleList import getAccountConsoleList, getAccountConsoleDetail

from Common.getConsoleLogin import getConsoleLogin_token

from Common.sign import get_sign

from Common.requests_library import Requests

from glo import console_JSON, console_HTTP, loginAccount_phone


# @pytest.mark.skip(reason="开发中")
@allure.feature('开户console_查询当前用户的审核数据')
class TestAccountConsoleGetOpenAudit():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_AccountConsole_GetOpenAudit(self):
        url = console_HTTP + "/api/con_open/v1/get_open_audit"

        # 拼装参数
        headers = console_JSON
        headers = headers
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        phone = loginAccount_phone
        identityTypes = [1]  # 身份类型 1-大陆居民 2-我是港澳地区居民 3-我是其他地区居民 海外居民，传入2,3
        status = 3  # 状态，为空时查询所有数据 1、待客户修改 2、初审列表 3、终审列表 4、已通过 5、已拒绝
        # print(getAccountConsoleList(headers, identityTypes, status))
        openOrderId = getAccountConsoleList(headers, identityTypes).get("data").get("list")[0].get(
            "openOrderDTO").get("openOrderId")
        # print(openOrderId)
        userId = getAccountConsoleDetail(headers, openOrderId).get("data").get("openInfoDTO").get("userId")
        # print(userId)
        paylo = {
            "userId": userId
        }
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="查询当前用户的审核数据"
        )

        j = r.json()
        # print(f"\n返回数据结果：{j}")
        assert r.status_code == 200

        try:
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
            if "data" in j:
                assert j.get("data").get("userId") == paylo.get("userId")
                assert "auditId" in j.get("data")
                assert "remark" in j.get("data")
                assert "createTime" in j.get("data")
                assert "openAuditItemAuditDTOList" in j.get("data")
        except:
            raise AssertionError(
                f"\n请求地址：{url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}")
