# test_AccountConsole_Detail   开户详情     /api/con_open/v1/detail
import json

import allure
import pytest

from Business.IdentityInformation import identityTypes
from Common.Accountcommon.getAccountConsoleList import getAccountConsoleList, getAccountConsoleDetail
from Common.getConsoleLogin import getConsoleLogin_token

from Common.sign import get_sign

from Common.requests_library import Requests

from glo import console_JSON, console_HTTP, loginAccount_phone


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('开户console_开户详情')
class TestAccountConsoleDetail():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_AccountConsole_Detail(self):
        url = console_HTTP + "/api/con_open/v1/detail"

        # 拼装参数
        headers = console_JSON
        headers = headers
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        phone = loginAccount_phone
        # identityTypes = [1]  # 身份类型 1-大陆居民 2-我是港澳地区居民 3-我是其他地区居民 海外居民，传入2,3
        status = 4  # 状态，为空时查询所有数据 1、待客户修改 2、初审列表 3、终审列表 4、已通过 5、已拒绝
        # print(getAccountConsoleList(headers, identityTypes, status))
        openOrderId = getAccountConsoleList(headers, identityTypes, status, phone).get("data").get("list")[0].get(
            "openOrderDTO").get("openOrderId")
        # print(openOrderId)
        # userId = getAccountConsoleDetail(headers, openOrderId).get("data").get("openInfoDTO").get("userId")
        # print(userId)
        paylo = {
            "openOrderId": openOrderId
        }
        # paylo = info
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="开户详情"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
            if "data" in j:
                assert j.get("data").get("openInfoDTO").get("openOrderId") == paylo.get("openOrderId")
                assert "openId" in j.get("data").get("openInfoDTO")
                assert "userId" in j.get("data").get("openInfoDTO")
                assert "openStatus" in j.get("data").get("openInfoDTO")
                assert "pageStatus" in j.get("data").get("openInfoDTO")
                assert "identityType" in j.get("data").get("openInfoDTO")
                assert "complianceInfos" in j.get("data").get("openInfoDTO")
                assert "derivative" in j.get("data").get("openInfoDTO")
                assert "cashAccounts" in j.get("data").get("openInfoDTO")
                assert "riskScore" in j.get("data").get("openInfoDTO")
                assert "cardNo" in j.get("data").get("openInfoDTO")
                assert "cardName" in j.get("data").get("openInfoDTO")
                assert "cardLastNamePinyin" in j.get("data").get("openInfoDTO")
                assert "cardNamePinyin" in j.get("data").get("openInfoDTO")
                assert "bankCardNo" in j.get("data").get("openInfoDTO")
                assert "bankCardName" in j.get("data").get("openInfoDTO")
                assert "bankCardUrl" in j.get("data").get("openInfoDTO")
                assert "bankCardPhone" in j.get("data").get("openInfoDTO")
                assert "mailbox" in j.get("data").get("openInfoDTO")
                assert "address" in j.get("data").get("openInfoDTO")
                assert "videoUrl" in j.get("data").get("openInfoDTO")
                assert "signatureUrl" in j.get("data").get("openInfoDTO")
                assert "createTime" in j.get("data").get("openInfoDTO")
                assert "updateTime" in j.get("data").get("openInfoDTO")
                assert "taxation" in j.get("data").get("openInfoDTO")
                assert "caId" in j.get("data").get("openInfoDTO")
                assert "auditId" in j.get("data").get("openInfoDTO")
                assert "ownerCardType" in j.get("data").get("openInfoDTO")
                assert "overseasOpenMode" in j.get("data").get("openInfoDTO")
                assert "nationality" in j.get("data").get("openInfoDTO")
                assert "userAccountDTO" in j.get("data")
                assert "openOrderDTO" in j.get("data")
                assert "zrNo" in j.get("data").get("userAccountDTO")
                assert "phone" in j.get("data").get("userAccountDTO")
                assert "nickname" in j.get("data").get("userAccountDTO")
                assert "openOrderId" in j.get("data").get("openOrderDTO")
                assert "userId" in j.get("data").get("openOrderDTO")
                assert "latestSubmitTime" in j.get("data").get("openOrderDTO")
                assert "finishTime" in j.get("data").get("openOrderDTO")
                assert "createTime" in j.get("data").get("openOrderDTO")
                assert "updateTime" in j.get("data").get("openOrderDTO")
                assert "status" in j.get("data")

        except:
            raise AssertionError(j)
