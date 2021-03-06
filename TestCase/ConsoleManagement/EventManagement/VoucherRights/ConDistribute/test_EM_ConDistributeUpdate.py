# test_EM_ConDistributeUpdate    修改定向派发（二期）    /api/con_distribute/v1/update
import json
import logging
import random

import allure
import pytest

from Common.ConsoleEventManagement.Add_Voucher_ParentCard import Add_ParentCard, Add_Voucher, add_distribute
from Common.ConsoleEventManagement.ConParentCardList import get_distributeIdlist, get_ConParentCardId, get_voucherId

from Common.getConsoleLogin import getConsoleLogin_token
from Common.get_time_stamp import timetostamp13, gettoday

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_JSON, console_HTTP, BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('活动管理console_修改定向派发（二期）')
class TestEMConDistributeUpdate():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(
                                 BASE_DIR +
                                 r"/TestData/test_EventManagementdata/test_EM_ConDistributeUpdate.json"))
    def test_EM_ConDistributeUpdate(self, info):
        url = console_HTTP + "/api/con_distribute/v1/update"
        header = console_JSON
        headers = {}
        headers.update(header)
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        Add_Voucher(headers)  # 新增权益
        voucherIds = [str(get_voucherId(headers, "高级行情-美股LV1权益", 0))]  # 获取权益ids
        # print(voucherIds)
        Add_ParentCard(headers, voucherIds)  # 新增母卡券
        parentCardId = get_ConParentCardId(headers, 0)  # 获取母卡券id
        add_distribute(headers, parentCardId)
        distributeId = get_distributeIdlist(headers, 0)  # 获取定向派发id

        applyType = info.get("applyType")
        applyNum = info.get("applyNum")
        reason = info.get("reason")
        distributeTime = int(timetostamp13(str(gettoday())))
        paylo = {
            "distributeId": distributeId,
            "reason": reason,
            "distributeTime": distributeTime,
            "distributeParentCard": [{
                "parentCardId": parentCardId,
                "applyType": applyType,
                "applyNum": applyNum
            }]
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="修改定向派发（二期）"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"

        except:
            assert j.get("code") == "530102"
            assert j.get("msg") == "母卡券信息不存在"

        else:
            raise AssertionError(
                f"\n请求地址：{url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}")
