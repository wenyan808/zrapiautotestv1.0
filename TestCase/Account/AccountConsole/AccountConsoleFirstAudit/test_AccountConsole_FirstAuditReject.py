# test_AccountConsole_FirstAuditReject
import json

import allure

from Business.IdentityInformation import signatureUrl, identityTypes
from Common.Accountcommon.AuditReject import apply_ca

from Common.Accountcommon.getAccountConsoleList import getAccountConsoleList, getAccountConsoleDetail, get_AuditItem

from Common.Accountcommon.getLoginAccountToken import GetLoginAccountToken

from Common.Accountcommon.modify_submit_audit import modify_submit_audit
from Common.getConsoleLogin import getConsoleLogin_token

from Common.sign import get_sign

from Common.requests_library import Requests

from glo import console_HTTP, JSON, HTTP, console_JSON


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('开户console初审_初审驳回')
class TestAccountConsoleFirstAuditReject():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_AccountConsole_FirstAuditReject(self):
        url = console_HTTP + "/api/con_open/v1/first_audit_reject"
        headers = console_JSON
        headers = headers
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        status = 2  # 状态，为空时查询所有数据 1、待客户修改 2、初审列表 3、终审列表 4、已通过 5、已拒绝
        # userId = getAccountConsoleList(headers, identityTypes, status, phone).get("data").get("list")[0].get("userId")
        # print(userId)
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
        auditItemIds = list(get_AuditItem(headers).get("data")[0].get("auditItemId"))
        remark = "测试01"
        otherReasons = "测试初审驳回"
        apply_ca(openId, headers)

        paylo = {
            "openId": f"{openId}",
            "remark": remark,
            "otherReasons": otherReasons,
            "auditItemIds": auditItemIds
        }

        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r1 = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="初审驳回"
        )

        k = r1.json()
        # print(k)

        # url2 = HTTP + "/as_user/api/cn_open/v1/modify_signature"
        # headers1 = JSON
        #
        # # 拼装参数
        # paylo = {
        #     "signatureUrl": signatureUrl
        # }
        # # print(paylo)
        # sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        # payload1 = {}
        # payload1.update(paylo)
        # payload1.update(sign1)
        # headers0 = headers1
        # token = GetLoginAccountToken()
        # # print(type(token))
        # token = {"token": token}
        # headers0.update(token)  # 将token更新到headers
        # # print(headers)
        # payload = json.dumps(dict(payload1))
        #
        # r2 = Requests(self.session).post(
        #     url=url2, headers=headers0, data=payload, title="修改个人签名"
        # )
        #
        # j2 = r2.json()
        # # print(j2)
        # modify_submit_audit(headers0)
        assert r1.status_code == 200
        try:
            assert k.get("code") == "000000"
            assert k.get("msg") == "ok"

        except:
            raise AssertionError(
                f"\n请求地址：{url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{k}"
            )
