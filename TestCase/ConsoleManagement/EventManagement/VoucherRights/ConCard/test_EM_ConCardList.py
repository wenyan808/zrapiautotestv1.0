# test_EM_ConCardList   子卡券列表(二期修改)   /api/con_card/v1/list

import json
import logging
import random

import allure
import pytest

from Common.ConsoleEventManagement.ConParentCardList import get_distributeIdlist

from Common.getConsoleLogin import getConsoleLogin_token

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_JSON, console_HTTP, BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('活动管理console_子卡券列表(二期修改)')
class TestEMConCardList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(
                                 BASE_DIR +
                                 r"/TestData/test_EventManagementdata/test_EM_ConCardList.json"))
    def test_EM_ConCardList(self, info):
        url = console_HTTP + "/api/con_card/v1/list"
        header = console_JSON
        headers = {}
        headers.update(header)
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        pageSize = info.get("pageSize")  # 每页条数
        currentPage = info.get("currentPage")  # 页数，默认当前页
        cardId = info.get("cardId")  # 子卡券id
        parentCardName = info.get("parentCardName")  # 母卡券名称
        receiveStartTime = info.get("receiveStartTime")  # 领取开始时间
        receiveEndTime = info.get("receiveEndTime")  # 领取结束时间
        updateStartTime = info.get("updateStartTime")  # 最近操作开始时间
        updateEndTime = info.get("updateEndTime")  # 最近操作结束时间
        consumeStartTime = info.get("consumeStartTime")  # 激活开始时间
        consumeEndTime = info.get("consumeEndTime")  # 激活结束时间
        voucherStartTime = info.get("voucherStartTime")  # 权益开始时间
        voucherEndTime = info.get("voucherEndTime")  # 权益结束时间
        receiveZrNo = info.get("receiveZrNo")  # 领取卓锐号
        consumeZrNo = info.get("consumeZrNo")  # 使用卓锐号
        sort = info.get("sort")
        # 1、派发方式倒序 2、派发方式正序 3、领取状态倒序 4、领取状态正序 5、使用状态倒序 6、使用状态正序
        # 7、领取时间倒序 8、领取时间正序 9、使用时间倒序 10、使用时间正序 1、权益生效时间段倒序 12、权益生效时间段正序
        distributeId = get_distributeIdlist(headers, 0)
        sourceId = distributeId  # 来源id,活动id(activity_id)或者定向派发id(distribute_id)

        paylo = {
            "pageSize": pageSize,
            "currentPage": currentPage,
            "cardId": cardId,
            "parentCardName": parentCardName,
            "receiveStartTime": receiveStartTime,
            "receiveEndTime": receiveEndTime,
            "updateStartTime": updateStartTime,
            "updateEndTime": updateEndTime,
            "consumeStartTime": consumeStartTime,
            "consumeEndTime": consumeEndTime,
            "voucherStartTime": voucherStartTime,
            "voucherEndTime": voucherEndTime,
            "receiveZrNo": receiveZrNo,
            "consumeZrNo": consumeZrNo,
            "sort": sort,
            "sourceId": sourceId
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="子卡券列表(二期修改)"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
