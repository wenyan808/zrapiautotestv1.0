# test_AccountConsole_SelectSignatureRecord      查询用户签名记录       /api/con_open/v1/select_signature_record
import json

import allure
import pytest

from Business.IdentityInformation import identityTypes
from Common.Accountcommon.getAccountConsoleList import getAccountConsoleList
from Common.assertapi import jsonschema_assert

from Common.getConsoleLogin import getConsoleLogin_token

from Common.sign import get_sign

from Common.requests_library import Requests
from TestAssertions.AccountConsoleSchemaData.SelectSignatureRecordSchema import SelectSignatureRecordSchema

from glo import console_JSON, console_HTTP, loginAccount_phone


# @pytest.mark.skip(reason="开发中")
@allure.feature('开户console_查询用户签名记录')
class TestAccountConsoleSelectSignatureRecord():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_AccountConsole_SelectSignatureRecord(self):
        url = console_HTTP + "/api/con_open/v1/select_signature_record"

        # 拼装参数
        headers = console_JSON
        headers = headers
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        phone = loginAccount_phone
        # status = None  # 状态，为空时查询所有数据 1、待客户修改 2、初审列表 3、终审列表 4、已通过 5、已拒绝
        # print(getAccountConsoleList(headers, identityTypes,status,phone).get("data").get("list"))
        openOrderId = getAccountConsoleList(headers, identityTypes).get("data").get("list")[0].get("openOrderDTO").get(
            "openOrderId")
        # print(userId)
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
            url=url, headers=headers, data=payload, title="查询用户签名记录"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
            if "data" in j:
                for i in range(len(j.get("data"))):
                    assert "signatureUrl" in j.get("data")[i]
                    assert "submitTime" in j.get("data")[i]

                jsonschema_assert(j.get("code"), j.get("msg"), j, SelectSignatureRecordSchema)

        except:
            raise AssertionError(j)

