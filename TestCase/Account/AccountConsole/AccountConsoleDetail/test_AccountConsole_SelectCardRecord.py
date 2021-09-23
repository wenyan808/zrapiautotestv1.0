# test_AccountConsole_SelectCardRecord      证件照OCR记录     /api/con_open/v1/select_card_record
import json

import allure
import pytest

from Business.IdentityInformation import identityTypes, phone6
from Common.Accountcommon.getAccountConsoleList import getAccountConsoleList
from Common.assertapi import jsonschema_assert

from Common.getConsoleLogin import getConsoleLogin_token

from Common.sign import get_sign

from Common.requests_library import Requests
from TestAssertions.AccountConsoleSchemaData.SelectCardRecordSchema import SelectCardRecordSchema

from glo import console_JSON, console_HTTP


# @pytest.mark.skip(reason="开发中")
@allure.feature('开户console_证件照OCR记录')
class TestAccountConsoleSelectCardRecord():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_AccountConsole_SelectCardRecord(self):
        url = console_HTTP + "/api/con_open/v1/select_card_record"

        # 拼装参数
        headers = console_JSON
        headers = headers
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        phone = phone6
        status = None  # 状态，为空时查询所有数据 1、待客户修改 2、初审列表 3、终审列表 4、已通过 5、已拒绝
        # print(getAccountConsoleList(headers, identityTypes, status, phone))
        get_openOrderId = getAccountConsoleList(headers, identityTypes, status, phone)
        # print(get_openOrderId)
        if len(get_openOrderId.get("data").get("list")) != 0:
            openOrderId = get_openOrderId.get("data").get("list")[0].get("openOrderDTO").get("openOrderId")
            # print(openOrderId)
        else:
            openOrderId = getAccountConsoleList(headers, identityTypes).get("data").get("list")[0].get(
                "openOrderDTO").get("openOrderId")
        # print(getAccountConsoleDetail(headers, openOrderId))
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
            url=url, headers=headers, data=payload, title="证件照OCR记录"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        if j.get("code") == "000000":
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
            if "data" in j:
                for i in range(len(j.get("data"))):
                    assert "cardId" in j.get("data")[i]
                    assert "userId" in j.get("data")[i]
                    assert "openId" in j.get("data")[i]
                    assert "cardSide" in j.get("data")[i]
                    assert "url" in j.get("data")[i]
                    assert "cardName" in j.get("data")[i]
                    assert "cardAuthority" in j.get("data")[i]
                    assert "cardLastNamePinyin" in j.get("data")[i]
                    assert "cardNamePinyin" in j.get("data")[i]
                    assert "cardSex" in j.get("data")[i]
                    assert "cardNation" in j.get("data")[i]
                    assert "cardNo" in j.get("data")[i]
                    assert "cardAddress" in j.get("data")[i]
                    assert "cardBirth" in j.get("data")[i]
                    assert "result" in j.get("data")[i]
                    assert "lastTime" in j.get("data")[i]
                    assert "updateTime" in j.get("data")[i]
                    assert "createTime" in j.get("data")[i]
                jsonschema_assert(j.get("code"), j.get("msg"), j, SelectCardRecordSchema)

        else:
            raise AssertionError(
                f"\n请求地址：{url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}")
