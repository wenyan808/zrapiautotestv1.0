# test_PicksPoolConsole_List    列表查询   /api/con_stock_pool/v1/list
"""
@File  ：test_PicksPoolConsoleList.py
@Author: yishouquan
@Time  : 2020/8/06
@Desc  :  列表查询
"""
import json
import time

import allure
import pytest

from Common.getConsoleLogin import getConsoleLogin_token

from Common.get_time_stamp import TimeToStamp13
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_HTTP, console_JSON, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('列表查询')
class TestPicksPoolConsoleList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

        cls.url = console_HTTP + "/api/con_stock_pool/v1/list"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info', get_json(BASE_DIR +
                                              r"/TestData/PicksPoolConsoleData/test_PicksPoolConsole_List.json"))
    def test_PicksPoolConsole_List(self, info):
        # login()  # 调用登录接口通过token传出来
        headers = {}
        headers.update(console_JSON)

        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        currentPage = info.get("currentPage")  # 当前页，默认为1
        pageSize = info.get("pageSize")  # 页面大小，默认20条
        operatorNm = info.get("operatorNm")  # 操作人昵称
        keyword = info.get("keyword")  # 股票名称或股票code相关的关键字
        market = info.get("market")  # 市场：1-港 2-美 3-A
        selectedTimeType = info.get("selectedTimeType")  # 时间查询类型：1-调入时间，2-调出时间，3-操作时间
        startTime = TimeToStamp13(info.get("startTime"))  # 开始时间，传零点时间戳
        endTime = TimeToStamp13(info.get("endTime"))  # 终止时间，传零点时间戳
        selectedRateType = info.get("selectedRateType")  # 筛选涨幅类型：1-入选后最高涨幅，2-最近一年最高涨幅
        startRate = info.get("startRate")  # 涨幅开始，要查询涨幅在20%~30%之间的记录，startRate请传0.2，endRate请传0.3
        endRate = info.get("endRate")  # 涨幅结束，要查询涨幅在20%~30%之间的记录，startRate请传0.2，endRate请传0.3
        status = info.get("status")  # 股票状态，1-正常，2-停牌，3-复牌，4-待上市，5-美股暂停交易，6-退市
        chosenStatus = info.get("chosenStatus")  # 精选状态（1-已调入  0-已调出）
        sortColType = info.get(
            "sortColType")  # （sortColType和sortRule要一起传）目标排序字段枚举：1-调入时间、2-调出时间、3-入选后最高涨幅、4-近一年最高涨幅、5-操作时间
        sortRule = info.get("sortRule")  # （sortColType和sortRule要一起传）排序规则枚举：1-顺序，0-逆序
        paylo = {
            "currentPage": currentPage,
            "pageSize": pageSize,
            "operatorNm": operatorNm,
            "keyword": keyword,
            "market": market,
            "selectedTimeType": selectedTimeType,
            "startTime": startTime,
            "endTime": endTime,
            "selectedRateType": selectedRateType,
            "startRate": startRate,
            "endRate": endRate,
            "status": status,
            "chosenStatus": chosenStatus,
            "sortColType": sortColType,
            "sortRule": sortRule
        }

        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=self.url, headers=headers, data=payload, title="列表查询"
        )
        j = r.json()
        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("msg") == "ok"
            assert j.get("code") == "000000"
            if "data" in j:
                assert "list" in j.get("data")
                assert "total" in j.get("data")
                assert "pageSize" in j.get("data")
                assert "currentPage" in j.get("data")
                # assert j.get("data").get("pageSize") == pageSize
                # assert j.get("data").get("currentPage") == currentPage
                if "list" in j.get("data"):
                    for i in range(len(j.get("data").get("list"))):
                        assert "id" in j.get("data").get("list")[i]
                        assert "last" in j.get("data").get("list")[i]
                        assert "ts" in j.get("data").get("list")[i]
                        assert "code" in j.get("data").get("list")[i]
                        assert "name" in j.get("data").get("list")[i]
                        assert "market" in j.get("data").get("list")[i]
                        assert "type" in j.get("data").get("list")[i]
                        assert "inTime" in j.get("data").get("list")[i]
                        assert "outTime" in j.get("data").get("list")[i]
                        assert "histMaxRate" in j.get("data").get("list")[i]
                        assert "yearMaxRate" in j.get("data").get("list")[i]
                        assert "chosenStatus" in j.get("data").get("list")[i]
                        assert "status" in j.get("data").get("list")[i]
                        assert "updateTime" in j.get("data").get("list")[i]
                        assert "operatorId" in j.get("data").get("list")[i]
                        assert "operatorNm" in j.get("data").get("list")[i]

        except:
            raise AssertionError(
                f"\n请求地址：{self.url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}")
