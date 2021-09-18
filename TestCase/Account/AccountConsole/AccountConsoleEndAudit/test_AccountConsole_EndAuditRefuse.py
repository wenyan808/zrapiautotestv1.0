# test_AccountConsole_EndAuditRefuse     终审拒绝             /api/con_open/v1/end_audit_refuse
import json

import allure

from Business.IdentityInformation import identityTypes
from Common.Accountcommon.getAccountConsoleList import getAccountConsoleList, getAccountConsoleDetail, get_AuditItem

from Common.getConsoleLogin import getConsoleLogin_token

from Common.sign import get_sign

from Common.requests_library import Requests

from glo import console_JSON, console_HTTP, loginAccount_phone, JSON, HTTP


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('开户console终审_终审拒绝')
class TestAccountConsoleEndAuditBack():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_AccountConsole_EndAuditBack(self):
        url1 = console_HTTP + "/api/con_open/v1/end_audit_refuse"
        # 拼装参数
        headers = console_JSON
        headers = headers
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        phone = loginAccount_phone

        # identityTypes = [1]  # 身份类型 1-大陆居民 2-我是港澳地区居民 3-我是其他地区居民 海外居民，传入2,3
        status = 3  # 状态，为空时查询所有数据 1、待客户修改 2、初审列表 3、终审列表 4、已通过 5、已拒绝
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
        auditItemIds = list(get_AuditItem(headers).get("data")[0].get("auditItemId"))
        remark = "测试终审拒绝"

        paylo = {
            "openId": openId,
            "remark": remark,
            "auditItemIds": auditItemIds
        }

        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r1 = Requests(self.session).post(
            url=url1, headers=headers, data=payload, title="终审拒绝"
        )

        k = r1.json()
        # print(k)
        assert r1.status_code == 200
        if k.get("code") == "000000":
            assert k.get("code") == "000000"
            assert k.get("msg") == "ok"

        else:
            raise AssertionError(
                f"\n请求地址：{url1}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{k}"
            )