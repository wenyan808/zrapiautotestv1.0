# test_CodeTableList   增量获取码表数据   /as_market/api/code_table/v1/list
"""
@File  ：test_CodeTableList.py
@Author: yishouquan
@Time  : 2020/8/02
@Desc  :  股票行情_增量获取码表数据
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
@allure.feature('增量获取码表数据')
class TestCodeTableList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        # login()  # 调用登录接口通过token传出来
        cls.url = HTTP + "/as_market/api/code_table/v1/list"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/AllStockData/test_CodeTableList.json"))
    def test_CodeTableList(self, info):
        # login()  # 调用登录接口通过token传出来
        headers = {}
        headers.update(JSON_dev)

        token = {"token": gettestLoginToken()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        version = info.get("version")  # 版本号（后台以该参数查询大于该版本的数据）

        paylo = {
            "version": version
        }
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=self.url, headers=headers, data=payload, title="增量获取码表数据"
        )
        j = r.json()
        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("msg") == "ok"
            assert j.get("code") == "000000"
            if "data" in j:
                assert j.get("data").get("more") == True or False
                assert "version" in j.get("data")
                assert "timestamp" in j.get("data")
                if "table" in j.get("data"):
                    for i in range(len(j.get("data").get("table"))):
                        assert "ts" in j.get("data").get("table")[i]
                        assert "code" in j.get("data").get("table")[i]
                        assert "type" in j.get("data").get("table")[i]
                        assert "status" in j.get("data").get("table")[i]
                        if "name" in j.get("data").get("table"):
                            assert "zh_CN" in j.get("data").get("table").get("name")
                            assert "zh_TW" in j.get("data").get("table").get("name")
                            assert "en_US" in j.get("data").get("table").get("name")
        except:
            raise AssertionError(
                f"\n请求地址：{self.url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}")
