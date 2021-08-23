# test_AccountConsole_GetAntiMoney    获取反洗钱信息    /api/con_open/v1/get_anti_money
"""
@File  ：test_AccountConsole_GetAntiMoney.py
@Author: yishouquan
@Time  : 2020/8/11
@Desc  :  获取反洗钱信息
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
@allure.feature('获取反洗钱信息')
class TestAccountConsoleGetAntiMoney():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        # login()  # 调用登录接口通过token传出来
        cls.url = console_HTTP + "/api/con_open/v1/get_anti_money"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_AccountConsole_GetAntiMoney(self):

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
            url=self.url, headers=headers, data=payload, title="获取反洗钱信息"
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
                    assert "amlId" in j.get("data")[i]
                    assert "userId" in j.get("data")[i]
                    assert "openId" in j.get("data")[i]
                    assert "openOrderId" in j.get("data")[i]
                    assert "supplierType" in j.get("data")[i]
                    assert "supplierOtherDesc" in j.get("data")[i]
                    assert "investigationTime" in j.get("data")[i]
                    assert "investigationResultType" in j.get("data")[i]
                    assert "investigationFiles" in j.get("data")[i]
                    assert "remark" in j.get("data")[i]
                    assert "remark" in j.get("data")[i]
                    assert "creatorId" in j.get("data")[i]
                    assert "operatorId" in j.get("data")[i]
                    assert "operator" in j.get("data")[i]
                    assert "updateTime" in j.get("data")[i]
                    # for y in range(len(j.get("data")[i].get("investigationFiles"))):
                    #     assert "name" in j.get("data")[i].get("investigationFiles")[y]
                    #     assert "url" in j.get("data")[i].get("investigationFiles")[y]

        except:
            raise AssertionError(
                f"\n请求地址：{self.url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}")

