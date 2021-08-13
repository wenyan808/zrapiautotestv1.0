# test_PicksPoolConsole_GetList            精选股池变更记录列表查询          /api/con_stock_pool/v1/get_list
"""
@File  ：test_PicksPoolConsoleGetList.py
@Author: yishouquan
@Time  : 2020/8/06
@Desc  :  精选股池变更记录列表查询
"""
import json
import time

import allure
import pytest

from Common.getConsoleLogin import getConsoleLogin_token

from Common.get_time_stamp import TimeToStamp13, gettoday, getTimeTostamp
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_HTTP, console_JSON, BASE_DIR


# @pytest.mark.skip(reason="请求地址不存在")
@allure.feature('精选股详情查询')
class TestPicksPoolConsoleGetList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

        cls.url = console_HTTP + "/api/con_stock_pool/v1/get_list"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info', get_json(BASE_DIR +
                                              r"/TestData/PicksPoolConsoleData/test_PicksPoolConsole_GetList.json"))
    def test_PicksPoolConsole_GetList(self, info):
        # login()  # 调用登录接口通过token传出来
        headers = {}
        headers.update(console_JSON)

        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        currentPage = info.get("currentPage")  # 当前页，默认为1
        pageSize = info.get("pageSize")  # 页面大小，默认20条
        keyword = info.get("keyword")  # 股票名称或股票code相关的关键字
        sort = info.get("sort")  # 排序条件(1:操作时间倒序<默认>、2:操作时间正序）
        market = info.get("selectedTimeType")  # 市场：1-港股 2-美股
        startTime = TimeToStamp13(info.get("startTime"))  # getTimeTostamp(30)  # 开始时间，传零点时间戳
        endTime = TimeToStamp13(info.get("endTime"))  # TimeToStamp13(str(gettoday()) + " " + "23:59:59")  # 终止时间，传零点时间戳
        operStatus = info.get("operStatus")  # operStatus 操作类型 1-调入 0-调出

        paylo = {
            "currentPage": currentPage,
            "pageSize": pageSize,
            "keyword": keyword,
            "sort": sort,
            "market": market,
            "operStatus": operStatus,
            "startTime": startTime,
            "endTime": endTime
        }
        # paylo.update(info)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=self.url, headers=headers, data=payload, title="精选股池变更记录列表查询"
        )
        j = r.json()
        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("msg") == "ok"
            assert j.get("code") == "000000"
            if "data" in j:
                if j.get("data").get("list") != None:
                    for i in range(len(j.get("data").get("list"))):
                        assert "id" in j.get("data").get("list")[i]
                        assert "type" in j.get("data").get("list")[i]
                        assert "ts" in j.get("data").get("list")[i]
                        assert "code" in j.get("data").get("list")[i]
                        assert "name" in j.get("data").get("list")[i]
                        assert "market" in j.get("data").get("list")[i]
                        assert "operStatus" in j.get("data").get("list")[i]
                        assert "operator" in j.get("data").get("list")[i]
                        assert "operatorId" in j.get("data").get("list")[i]
                        assert "operReason" in j.get("data").get("list")[i]
                        assert "operTime" in j.get("data").get("list")[i]
                        assert "total" in j.get("data")
                        assert "pageSize" in j.get("data")
                        assert "currentPage" in j.get("data")
                else:
                    print(f"列表数据：{j.get('data').get('list')}")



        except:
            raise AssertionError(
                f"\n请求地址：{self.url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}")
