# test_IM_GetConTopic     查询单个专题信息     /api/con_topic/v1/get
import json
import logging
import random

import allure
import pytest

from Common.ConTopic_common.get_ConTopicID import get_ConTopicID
from Common.getConsoleLogin import getConsoleLogin_token

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_HTTP, BASE_DIR, console_JSON


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('资讯console_查询单个专题信息')
class TestIMGetConTopic():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    # @pytest.mark.parametrize('info',
    #                          get_json(BASE_DIR + r"/TestData/testIMData/test_IM_conNewsList.json"))
    def test_IM_GetConTopic(self):
        url = console_HTTP + "/api/con_topic/v1/get"

        header = console_JSON
        headers = {}
        headers.update(header)
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        Id = get_ConTopicID(headers, 1)
        paylo = {
            "id": Id
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)
        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="查询单个专题信息"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        if "data" in j:
            assert j.get("data").get("id") == Id
            assert "categoryId" in j.get("data")
            assert "name" in j.get("data")
            assert "description" in j.get("data")
            assert "categoryName" in j.get("data")
            assert "isHot" in j.get("data")
            assert "sort" in j.get("data")
            assert "type" in j.get("data")
            assert "headImg" in j.get("data")
            assert "backgroundImg" in j.get("data")
            if j.get("data").get("id") == Id:
                # assert j.get("data").get("categoryId") == list1[-1].get("data").get("list")[0].get("categoryId")
                # assert j.get("data").get("name") == list1[-1].get("data").get("list")[0].get("name")
                # assert j.get("data").get("description") == list1[-1].get("data").get("list")[0].get("description")
                assert j.get("data").get("categoryName") == None
                assert j.get("data").get("isHot") == None
                assert j.get("data").get("sort") == None
                assert j.get("data").get("type") == None
                assert "https://zhuorui-public-test.oss-cn-shenzhen.aliyuncs.com/information/" \
                       in j.get("data").get("headImg")
                assert "https://zhuorui-public-test.oss-cn-shenzhen.aliyuncs.com/information/" \
                       in j.get("data").get("backgroundImg")
            else:
                raise AssertionError(
                    f"\n请求地址：{url}"
                    f"\nbody参数：{payload}"
                    f"\n请求头部参数：{headers}"
                    f"\n返回数据结果：{j}"
                )