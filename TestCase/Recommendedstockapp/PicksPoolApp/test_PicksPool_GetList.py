# test_PicksPool_GetList     精选股列表查询         /as_recommend/api/stock_pool/v1/list
"""
@File  ：test_PicksPool_Indicator.py
@Author: yishouquan
@Time  : 2020/8/05
@Desc  :  精选股池指标查询（分析指标、涨幅前三）
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
@allure.feature('精选股池指标查询（分析指标、涨幅前三）')
class TestPicksPoolGetList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        # login()  # 调用登录接口通过token传出来
        cls.url = HTTP + "/as_recommend/api/stock_pool/v1/indicator"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info', get_json(BASE_DIR +
                                              r"/TestData/PicksPoolAppData/test_PicksPoolGetList.json"))
    def test_PicksPool_GetList(self, info):
        # login()  # 调用登录接口通过token传出来
        headers = {}
        headers.update(JSON_dev)

        token = {"token": gettestLoginToken()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        currentPage = info.get("currentPage")  # 当前页，默认为1
        pageSize = info.get("pageSize")  # 页面大小，默认20条
        selectedType = info.get("selectedType")  # 类型：不传默认查港股。1-港股，2-美股，3-etf
        sort = info.get("sort")  # 排序条件(1:入选时间倒序<默认>、2:入选时间正序、3:入选后最高涨幅倒序、4:入选后最高涨幅正序）

        paylo = {
            "currentPage": currentPage,
            "pageSize": pageSize,
            "selectedType": selectedType,
            "sort": sort
        }
        # paylo = info
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=self.url, headers=headers, data=payload, title="精选股池指标查询（分析指标、涨幅前三）"
        )
        j = r.json()
        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("msg") == "ok"
            assert j.get("code") == "000000"
            if "data" in j:
                assert "yearAverageRate" in j.get("data")
                assert "yearSuccessRate" in j.get("data")
                if "tops" in j.get("data"):
                    for i in range(len(j.get("data").get("tops"))):
                        assert "ts" in j.get("data").get("tops")[i]
                        assert "code" in j.get("data").get("tops")[i]
                        assert "name" in j.get("data").get("tops")[i]
                        assert "inTime" in j.get("data").get("tops")[i]
                        assert "type" in j.get("data").get("tops")[i]
                        assert "realPrice" in j.get("data").get("tops")[i]
                        assert "histMaxRate" in j.get("data").get("tops")[i]

        except:
            raise AssertionError(
                f"\n请求地址：{self.url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}")
