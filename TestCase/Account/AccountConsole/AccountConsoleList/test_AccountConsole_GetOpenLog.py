# test_AccountConsole_GetOpenLog    操作记录    /api/con_open/v1/get_open_log
"""
@File  ：test_AccountConsole_GetOpenLog.py
@Author: yishouquan
@Time  : 2020/8/11
@Desc  :  操作记录
"""
import json
import time

import allure
import pytest

from Common.Accountcommon.getAccountConsoleList import getAccountConsoleList
from Common.getConsoleLogin import getConsoleLogin_token


from Common.sign import get_sign

from Common.requests_library import Requests


from glo import console_HTTP, console_JSON, BASE_DIR, loginAccount_phone


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('操作记录')
class TestAccountConsoleGetOpenLog():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        # login()  # 调用登录接口通过token传出来
        cls.url = console_HTTP + "/api/con_open/v1/get_open_log"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_AccountConsole_GetOpenLog(self):

        headers = {}
        headers.update(console_JSON)

        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)

        phone = loginAccount_phone
        identityTypes = [1]  # 身份类型 1-大陆居民 2-我是港澳地区居民 3-我是其他地区居民 海外居民，传入2,3
        status = 3  # 状态，为空时查询所有数据 1、待客户修改 2、初审列表 3、终审列表 4、已通过 5、已拒绝
        # print(getAccountConsoleList(headers, identityTypes, status, phone))

        openOrderId = getAccountConsoleList(headers, identityTypes, status).get("data").get("list")[0].get(
            "openOrderDTO").get("openOrderId")
        # print(openOrderId)

        paylo = {
            "openOrderId": openOrderId
        }
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=self.url, headers=headers, data=payload, title="操作记录"
        )
        j = r.json()
        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("msg") == "ok"
            assert j.get("code") == "000000"
            if "data" in j:
                for i in range(len(j.get("data"))):
                    assert "creator" in j.get("data")[i]
                    assert "createTime" in j.get("data")[i]
                    assert "logId" in j.get("data")[i]
                    assert "userId" in j.get("data")[i]
                    assert "openId" in j.get("data")[i]
                    assert "openOrderId" in j.get("data")[i]
                    assert "operationNode" in j.get("data")[i]
                    assert "operationType" in j.get("data")[i]
                    assert "operationReason" in j.get("data")[i]
                    assert "operationRemark" in j.get("data")[i]
                    assert "creatorType" in j.get("data")[i]
                    assert "creatorId" in j.get("data")[i]

        except:
            raise AssertionError(
                f"\n请求地址：{self.url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}")
