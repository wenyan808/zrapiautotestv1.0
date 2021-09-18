# test_AccountConsole_ApplyCa               申请ca认证         /api/con_cn_open/v1/apply_ca
import json


import allure
import pytest

from Business.IdentityInformation import identityTypes
from Common.Accountcommon.getAccountConsoleList import getAccountConsoleList, getAccountConsoleDetail
from Common.getConsoleLogin import getConsoleLogin_token

from Common.show_sql import showsql

from Common.sign import get_sign

from Common.requests_library import Requests

from glo import console_JSON, console_HTTP, loginAccount_phone


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('开户console终审_申请ca认证')
class TestAccountConsoleApplyCa():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_AccountConsole_ApplyCa(self):
        url2 = console_HTTP + "/api/con_open/v1/end_audit_list"
        url1 = console_HTTP + "/api/con_open/v1/end_audit_back"
        url = console_HTTP + "/api/con_cn_open/v1/apply_ca"
        # 拼装参数
        headers = console_JSON
        headers1 = {}
        token = {"token": getConsoleLogin_token()}
        headers1.update(headers)
        headers1.update(token)  # 将token更新到headers
        # print(headers)
        phone = loginAccount_phone
        status = 3  # 状态，为空时查询所有数据 1、待客户修改 2、初审列表 3、终审列表 4、已通过 5、已拒绝
        # print(getAccountConsoleList(headers, identityTypes, status, phone))
        # 获取开户console列表
        get_openOrderId = getAccountConsoleList(headers1, identityTypes)
        # print(get_openOrderId)
        if len(get_openOrderId.get("data").get("list")) != 0:
            openOrderId = get_openOrderId.get("data").get("list")[0].get("openOrderDTO").get("openOrderId")
            # print(openOrderId)
        else:
            openOrderId = getAccountConsoleList(headers1, identityTypes).get("data").get("list")[0].get(
                "openOrderDTO").get("openOrderId")
        # print(getAccountConsoleDetail(headers1, openOrderId))
        openId = getAccountConsoleDetail(headers1, openOrderId).get("data").get("openInfoDTO").get("openId")  # 开户id
        # 申请ca时，需要判断是否为大陆开户，大陆开户才需要ca
        if identityTypes == [1]:

            paylo = {
                "openId": openId
            }

            sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
            payload1 = {}
            payload1.update(paylo)
            payload1.update(sign1)

            payload = json.dumps(dict(payload1))

            r = Requests(self.session).post(
                url=url, headers=headers1, data=payload, title="申请ca认证"
            )

            j = r.json()
            # print(j)
            assert r.status_code == 200
            try:
                assert j.get("code") == "570705"
                assert j.get("msg") == "粤港互认验证_通过"
            except:
                raise AssertionError(j)
            # paylo = {
            #     "userId": f"{userId}",
            #     "auditFails": ["0101"]
            # }
            #
            # sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
            # payload1 = {}
            # payload1.update(paylo)
            # payload1.update(sign1)
            #
            # payload = json.dumps(dict(payload1))
            #
            # r1 = Requests(self.session).post(
            #     url=url1, headers=headers1, data=payload, title="打回初审"
            # )
            #
            # k = r1.json()
            # # print(k)
