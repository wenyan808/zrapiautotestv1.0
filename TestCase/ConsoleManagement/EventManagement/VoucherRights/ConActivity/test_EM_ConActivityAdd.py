# test_EM_ConActivityAdd    创建活动   /api/con_activity/v1/add

import json
import logging
import random

import allure
import pytest

from Common.ConsoleEventManagement.Add_Voucher_ParentCard import Add_Voucher, Add_ParentCard
from Common.ConsoleEventManagement.ConParentCardList import get_voucherId, get_ConParentCardId
from Common.ConsoleEventManagement.ImportConUserGroup import ImportConUserGroup
from Common.getConsoleLogin import getConsoleLogin_token
from Common.get_time_stamp import gettoday, TimeToStamp13, getTimeTostamp

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_JSON, console_HTTP, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('活动管理console_创建活动')
class TestEMConActivityAdd():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/test_EventManagementdata/test_EM_ConActivityAdd.json"))
    def test_EM_ConActivityAdd(self, info):
        url = console_HTTP + "/api/con_activity/v1/add"
        header = console_JSON

        headers = {}
        headers.update(header)
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        Add_Voucher(headers)  # 新增权益
        voucherIds = [str(get_voucherId(headers,"高级行情-美股LV1权益", 0))]  # 获取权益id
        # print(voucherIds)
        Add_ParentCard(headers, voucherIds)  # 新增母卡券

        paylo = info
        publishStartTime = int(getTimeTostamp(1))  # 活动发布开始时间
        publishEndTime = int(getTimeTostamp(30))  # 活动发布结束时间

        parentCardId = get_ConParentCardId(headers, 0)  # 获取母卡券id
        totalNum = "20"  # 总数
        # position = 2  # 广告位置 ff1、活动-热门活动 2、活动-普通活动
        # startTime = int(TimeToStamp13(str(gettoday()) + ' ' + "23:59:59"))  # 广告开始时间
        # imageUrl = ""  # 图片地址(海报地址)
        # accessUrl = "http://zr66.com"  # 广告连接地址
        paylo1 = {"publishStartTime": publishStartTime,
                  "publishEndTime": publishEndTime,
                  "activityParentCard": [{
                      "parentCardId": parentCardId,
                      "totalNum": totalNum
                  }]}
        # print(paylo)
        # paylo2 = {"activityName": "asdhklnasd", "virtual": 1, "activityType": 2, "publishStartTime": 1623495154000,
        #           "publishEndTime": 1625019277000, "ad": 0,
        #           "activityParentCard": [{"parentCardId": "92757e54563d42f58d568f8d6b669e4a", "totalNum": 1000}]}
        paylo1.update(paylo)
        sign1 = {"sign": get_sign(paylo1)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo1)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="创建活动"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
