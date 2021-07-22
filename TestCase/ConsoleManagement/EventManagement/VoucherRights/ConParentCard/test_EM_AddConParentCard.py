# test_EM_AddConParentCard     创建母卡券    /api/con_parent_card/v1/add
import json
import logging
import random

import allure
import pytest

from Common.ConsoleEventManagement.ConParentCardList import get_ConParentCardId
from Common.ConsoleEventManagement.ConParentCardUpdateStatus import UpdateStatus_conparentcard
from Common.ConsoleEventManagement.ImportConUserGroup import ImportConUserGroup
from Common.getConsoleLogin import getConsoleLogin_token
from Common.get_time_stamp import TimeToStamp13, gettoday, TimeTostamp, getTimeTostamp

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_JSON, console_HTTP, BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('活动管理console_创建母卡券')
class TestEMAddConParentCard():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/test_EventManagementdata/test_EM_AddConParentCard.json"))
    def test_EM_AddConParentCard(self, info):
        url = console_HTTP + "/api/con_parent_card/v1/add"
        header = console_JSON
        headers = {}
        headers.update(header)
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        parentCardName = info.get("parentCardName") + str(gettoday())  # 母卡券名称
        type1 = info.get("type")  # 母卡券类型:1、行情卡
        groupId = list(ImportConUserGroup("user_group", "groupid_phone.xlsx", headers))[0]  # 用户组id
        voucherIds = info.get("voucherIds")  # 权益ids
        parentCardTotalNum = info.get("parentCardTotalNum")  # 母卡券总数数量
        activationType = info.get("activationType")  # 激活方式:1、自动激活 2、手动激活
        # activationStartTime = int(TimeToStamp13(info.get("activationStartTime")))  # 激活开始时间
        activationStartTime = getTimeTostamp(0)
        # activationEndTime = int(TimeToStamp13(info.get("activationEndTime")))  # 激活结束时间
        activationEndTime = getTimeTostamp(30)
        validType = info.get("validType")  # 权益时间类型1、天数2、时间范围
        validDays = info.get("validDays")  # 权益有效期天数

        # 权益时间段开始时间
        # validStartTime = int(TimeToStamp13(info.get("validStartTime")))
        validStartTime = getTimeTostamp(1)
        # 权益时间段结束时间
        # alidEndTime = int(TimeToStamp13(info.get("alidEndTime")))
        alidEndTime = getTimeTostamp(30)
        receiveType = info.get("receiveType")  # 领取方式:1、自动领取 2、手动领取
        receiveMode = info.get("receiveMode")  # 领取模式 1、一人一次 2、一人多次
        receiveNum = info.get("receiveNum")  # 可领取次数
        receiveInterval = info.get("receiveInterval")  # 可领取间隔
        # paylo = info
        paylo = {
            "parentCardName": parentCardName,
            "type": type1,
            "groupId": groupId,
            "voucherIds": voucherIds,
            "parentCardTotalNum": parentCardTotalNum,
            "activationType": activationType,
            "activationStartTime": activationStartTime,
            "activationEndTime": activationEndTime,
            "validType": validType,
            "validDays": validDays,
            "validStartTime": validStartTime,
            "validEndTime": alidEndTime,
            "receiveType": receiveType,
            "receiveMode": receiveMode,
            "receiveNum": receiveNum,
            "receiveInterval": receiveInterval
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="创建母卡券"
        )

        j = r.json()
        # print(j)
        # 获取卡券id
        parentCardId = get_ConParentCardId(headers, 0)
        # 终止领取
        UpdateStatus_conparentcard(headers, parentCardId, 1)
        # 终止核销
        UpdateStatus_conparentcard(headers, parentCardId, 3)
        # 母卡券停用
        UpdateStatus_conparentcard(headers, parentCardId, 5)
        assert r.status_code == 200
        try:
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"

        except:
            assert j.get("code") == "530106"
            assert j.get("msg") == "激活结束时间必须在激活开始时间之后"

        # else:
        #     raise AssertionError(
        #         f"\n请求地址：{url}"
        #         f"\nbody参数：{payload}"
        #         f"\n请求头部参数：{headers}"
        #         f"\n返回数据结果：{j}")
