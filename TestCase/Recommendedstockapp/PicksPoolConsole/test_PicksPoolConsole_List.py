# test_PicksPoolConsole_List    列表查询   /api/con_stock_pool/v1/list
"""
@File  ：test_PicksPool_ChangeList.py
@Author: yishouquan
@Time  : 2020/8/06
@Desc  :  最新变动列表查询
"""
import json
import time

import allure
import pytest

from Common.getTestLoginToken import gettestLoginToken
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import HTTP, JSON_dev, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('最新变动列表查询')
class TestPicksPoolChangeList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        # login()  # 调用登录接口通过token传出来
        cls.url = HTTP + "/as_recommend/api/stock_pool/v1/change_list"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info', get_json(BASE_DIR +
                                              r"/TestData/PicksPoolAppData/test_PicksPoolChangeList.json"))
    def test_PicksPool_ChangeList(self, info):
        # login()  # 调用登录接口通过token传出来
        headers = {}
        headers.update(JSON_dev)

        token = {"token": gettestLoginToken()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        currentPage = info.get("currentPage")  # 当前页，默认为1
        pageSize = info.get("pageSize")  # 页面大小，默认20条
        market = info.get("market")  # 市场：1-港 2-美
        date = info.get("date")  # 时间  1-近一月 2-近三月 3-近半年 4-近一年
        operStatus = info.get("operStatus")  # 操作类型 1-调入 0-调出

        paylo = {
            "currentPage": currentPage,
            "pageSize": pageSize,
            "market": market,
            "date": date,
            "operStatus": operStatus
        }
        # paylo = info
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=self.url, headers=headers, data=payload, title="最新变动列表查询"
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
                assert j.get("data").get("pageSize") == pageSize
                assert j.get("data").get("currentPage") == currentPage
                if "list" in j.get("data"):
                    for i in range(len(j.get("data").get("list"))):
                        assert "id" in j.get("data").get("list")[i]
                        assert "ts" in j.get("data").get("list")[i]
                        assert "code" in j.get("data").get("list")[i]
                        assert "name" in j.get("data").get("list")[i]
                        assert "market" in j.get("data").get("list")[i]
                        assert "type" in j.get("data").get("list")[i]
                        assert "operStatus" in j.get("data").get("list")[i]
                        assert "operReason" in j.get("data").get("list")[i]
                        assert "operTime" in j.get("data").get("list")[i]

        except:
            raise AssertionError(
                f"\n请求地址：{self.url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}")

