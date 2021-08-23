# test_ConErrorCodeList     查询错误码列表             /api/response_code/v1/list
"""
@File  ：test_ConErrorCodeList.py
@Author: yishouquan
@Time  : 2020/8/05
@Desc  :  查询错误码列表
"""
import json
import time

import allure
import pytest

from Common.getConsoleLogin import getConsoleLogin_token

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_HTTP, console_JSON, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('查询错误码列表')
class TestConErrorCodeList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        # login()  # 调用登录接口通过token传出来
        cls.url = console_HTTP + "/api/response_code/v1/list"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info', get_json(BASE_DIR +
                                              r"/TestData/Consoledate/test_ConErrorCodeList.json"))
    def test_ConErrorCode_List(self, info):
        # login()  # 调用登录接口通过token传出来
        headers = {}
        headers.update(console_JSON)

        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        currentPage = info.get("currentPage")  # 当前页，默认为1
        pageSize =info.get("pageSize")  # 页面大小，默认20条
        code = info.get("code")  # 错误码

        zh_CN = info.get("zh_CN")  # 中文简体
        operator = info.get("operator")  # 操作人
        variation = info.get("variation")  # 是否发生改变  0未改变 1改变
        deleted = info.get("deleted")  # 删除标识    0未删除 1程序值已删除

        paylo = {
            "currentPage": currentPage,
            "pageSize": pageSize,
            "code": code,
            "zh_CN": zh_CN,
            "operator": operator,
            "variation": variation,
            "deleted": deleted
        }
        # paylo = info
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=self.url, headers=headers, data=payload, title="查询错误码列表"
        )
        j = r.json()
        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("msg") == "ok"
            assert j.get("code") == "000000"
            if "data" in j:
                if "list" in j.get("data"):
                    for i in range(len(j.get("data").get("list"))):
                        assert "msgOriginal" in j.get("data").get("list")[i]
                        assert "code" in j.get("data").get("list")[i]
                        assert "zh_CN" in j.get("data").get("list")[i]
                        assert "zh_TW" in j.get("data").get("list")[i]
                        assert "en_US" in j.get("data").get("list")[i]
                        assert "operator" in j.get("data").get("list")[i]
                        assert "updateTime" in j.get("data").get("list")[i]
                        assert "variation" in j.get("data").get("list")[i]
                        assert "deleted" in j.get("data").get("list")[i]

        except:
            raise AssertionError(
                f"\n请求地址：{self.url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}")
