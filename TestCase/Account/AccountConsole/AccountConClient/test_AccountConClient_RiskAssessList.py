# test_AccountConClient_RiskAssessList   投资者风险承受能力测评查询     /api/con_client/v1/risk_assess_list
"""
@File  ：test_AccountConClient_RiskAssessList.py
@Author: yishouquan
@Time  : 2021/9/14
@Desc  :  投资者风险承受能力测评查询
"""
import json
import time

import allure
import pytest

from Common.Accountcommon.getAccountConsoleList import getAccountConsoleList
from Common.getConsoleLogin import getConsoleLogin_token
from Common.get_time_stamp import TimeToStamp13

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_json import get_json

from glo import console_HTTP, console_JSON, BASE_DIR, loginAccount_phone


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('投资者风险承受能力测评查询')
class TestAccountConClientRiskAssessList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        # login()  # 调用登录接口通过token传出来
        cls.url = console_HTTP + "/api/con_client/v1/risk_assess_list"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info', get_json(BASE_DIR +
                                              r"/TestData/AccountConsoledata/test_AccountConClient_RiskAssessList.json"))
    def test_AccountConClient_RiskAssessList(self, info):

        headers = {}
        headers.update(console_JSON)

        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)

        zrNo = info.get("zrNo")  # 卓锐号
        accType = info.get("accType")  # 资金账户类型 C-现金账户 M-孖展账户
        clientId = info.get("clientId")  # 客户账号
        fundAccount = info.get("fundAccount")  # 资金账号
        sureStartTime = TimeToStamp13(info.get("sureStartTime"))  # 开始时间 零点时间戳
        sureEndTime = TimeToStamp13(info.get("sureEndTime"))  # 结束数据 零点时间戳
        clientType = info.get("clientType")  # 账户类型 1-证券账户
        currentPage = info.get("currentPage")  # 当前页，默认1
        pageSize = info.get("pageSize")  # 每页显示条数,默认20
        paylo = {
            "zrNo": zrNo,
            "accType": accType,
            "clientId": clientId,
            "fundAccount": fundAccount,
            "sureStartTime": sureStartTime,
            "sureEndTime": sureEndTime,
            "clientType": clientType,
            "currentPage": currentPage,
            "pageSize": pageSize
        }
        # paylo={}
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=self.url, headers=headers, data=payload, title="投资者风险承受能力测评查询"
        )
        j = r.json()
        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("msg") == "ok"
            assert j.get("code") == "000000"
            if "data" in j:
                for i in range(len(j.get("data").get("list"))):
                    assert "userId" in j.get("data").get("list")[i]
                    assert "zrNo" in j.get("data").get("list")[i]
                    assert "riskAssessId" in j.get("data").get("list")[i]
                    assert "clientId" in j.get("data").get("list")[i]
                    assert "fundAccount" in j.get("data").get("list")[i]
                    assert "accType" in j.get("data").get("list")[i]
                    assert "riskScore" in j.get("data").get("list")[i]
                    assert "fsInfo" in j.get("data").get("list")[i]
                    assert "fsFundSource" in j.get("data").get("list")[i].get("fsInfo")
                    assert "fsIncome" in j.get("data").get("list")[i].get("fsInfo")
                    assert "fsIncome" in j.get("data").get("list")[i].get("fsInfo")
                    assert "fsTotalAssets" in j.get("data").get("list")[i].get("fsInfo")
                    assert "fsWealthSource" in j.get("data").get("list")[i].get("fsInfo")
                    assert "fsWorkStatus" in j.get("data").get("list")[i].get("fsInfo")
                    assert "investInfo" in j.get("data").get("list")[i]
                    assert "investAmount" in j.get("data").get("list")[i].get("investInfo")
                    assert "investBond" in j.get("data").get("list")[i].get("investInfo")
                    assert "investFixed" in j.get("data").get("list")[i].get("investInfo")
                    assert "investFund" in j.get("data").get("list")[i].get("investInfo")
                    assert "investLossScope" in j.get("data").get("list")[i].get("investInfo")
                    assert "investOther" in j.get("data").get("list")[i].get("investInfo")
                    assert "investRate" in j.get("data").get("list")[i].get("investInfo")
                    assert "investReserveFund" in j.get("data").get("list")[i].get("investInfo")
                    assert "investTarget" in j.get("data").get("list")[i].get("investInfo")
                    assert "investTime" in j.get("data").get("list")[i].get("investInfo")
                    assert "investWarrants" in j.get("data").get("list")[i].get("investInfo")
                    assert "createTime" in j.get("data").get("list")[i]
                    assert "clientType" in j.get("data").get("list")[i]
                    assert "total" in j.get("data")
                    assert "pageSize" in j.get("data")
                    assert "currentPage" in j.get("data")
        except:
            raise AssertionError(
                f"\n请求地址：{self.url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}")

