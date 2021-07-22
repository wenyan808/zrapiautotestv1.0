# test_EM_ConDistributeAdd    新增定向派发（二期修改）     /api/con_distribute/v1/add
import json
import logging
import random

import allure
import pytest

from Common.ConsoleEventManagement.Add_Voucher_ParentCard import Add_ParentCard, Add_Voucher, add_activity
from Common.ConsoleEventManagement.ConParentCardList import get_ConParentCardId, get_voucherId
from Common.ConsoleEventManagement.ImportConUserGroup import ImportConUserGroup
from Common.getConsoleLogin import getConsoleLogin_token
from Common.get_time_stamp import TimeToStamp13, gettoday

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_JSON, console_HTTP, BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('活动管理console_新增定向派发（二期修改）')
class TestEMConDistributeAdd():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/test_EventManagementdata/test_EM_ConDistributeAdd.json"))
    def test_EM_ConDistributeAdd(self, info):
        url = console_HTTP + "/api/con_distribute/v1/add"
        header = console_JSON
        headers = {}
        headers.update(header)
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # 新增权益
        Add_Voucher(headers)
        # 获取权益id
        voucherId = get_voucherId(headers, "高级行情-美股LV1权益", 0)
        voucherIds = [voucherId]  # 复数权益id，可以多个（权益ids string[]）
        Add_ParentCard(headers, voucherIds)  # 新增母卡券

        groupId = list(ImportConUserGroup("user_group", "groupid_phone.xlsx", headers))[0]  # 用户组id
        distributeTime = int(TimeToStamp13(str(gettoday()) + ' ' + "11:00:00"))  # 派发开始时间
        parentCardId = get_ConParentCardId(headers, 0)  # 母卡券id
        totalNum = "20"
        paylo = info
        paylo1 = {
            "groupId": groupId,
            "distributeTime": distributeTime,
            "distributeParentCard": [
                {"parentCardId": parentCardId,
                 "totalNum": totalNum}
            ]
        }
        paylo1.update(paylo)
        sign1 = {"sign": get_sign(paylo1)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo1)
        # payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="新增定向派发（二期修改）"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"

        except:
            assert j.get("code") == "530114"
            assert j.get("msg") == "母卡券应为自动激活"

        else:
            raise AssertionError(
                f"\n请求地址：{url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}")
