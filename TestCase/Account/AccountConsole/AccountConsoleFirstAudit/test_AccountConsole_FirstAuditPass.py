# test_AccountConsole_FirstAuditPass
import json

import allure

from Business.IdentityInformation import identityTypes
from Common.Accountcommon.AuditReject import apply_ca

from Common.Accountcommon.getAccountConsoleList import getAccountConsoleDetail, getAccountConsoleList
from Common.getConsoleLogin import getConsoleLogin_token
from Common.show_sql import showsql

from Common.sign import get_sign

from Common.requests_library import Requests

from glo import console_HTTP, testphone, console_JSON


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('开户console初审_初审列表')
class TestAccountConsoleEndAuditPass():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_AccountConsole_EndAuditPass(self, remark=None):
        url = console_HTTP + "/api/con_open/v1/first_audit_pass"
        headers = console_JSON
        headers = headers
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        status = 2  # 状态，为空时查询所有数据 1、待客户修改 2、初审列表 3、终审列表 4、已通过 5、已拒绝
        # print(getAccountConsoleList(headers, identityTypes, status, phone))
        # 获取开户console列表
        get_openOrderId = getAccountConsoleList(headers, identityTypes, status)
        # print(get_openOrderId)
        if len(get_openOrderId.get("data").get("list")) != 0:
            openOrderId = get_openOrderId.get("data").get("list")[0].get("openOrderDTO").get("openOrderId")
            # print(openOrderId)
        else:
            openOrderId = getAccountConsoleList(headers, identityTypes).get("data").get("list")[0].get(
                "openOrderDTO").get("openOrderId")
        # print(getAccountConsoleDetail(headers, openOrderId))
        openId = getAccountConsoleDetail(headers, openOrderId).get("data").get("openInfoDTO").get("openId")  # 开户id

        # print(userId)
        # apply_ca(openId, headers)
        paylo = {
            "openId": openId,
            "remark": remark
        }

        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="初审通过"
        )

        j = r.json()
        # print(j)

        assert r.status_code == 200
        if j.get("code") == "000000":

            assert j.get("msg") == "ok"

        else:
            raise AssertionError(j)
