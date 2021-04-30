# test_IM_ConTopicAdd      新增专题    /api/con_topic/v1/add
import json
import logging
import random

import allure
import pytest

from Common.OSS import oss_file
from Common.getConsoleLogin import getConsoleLogin_token
from Common.get_time_stamp import get_time_stamp16

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_JSON, console_HTTP, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('资讯console_查询资讯列表')
class TestIMConTopicAdd():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    # @pytest.mark.parametrize('info',
    #                          get_json(BASE_DIR + r"/TestData/testIMData/test_IM_conNewsList.json"))
    def test_IM_ConTopicAdd(self):
        url = console_HTTP + "/api/con_topic/v1/add"
        url1 = console_HTTP + "/api/con_sts/v1/token"
        header = console_JSON
        header = header

        headers = {}
        headers.update(header)

        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        name = "自动化测试专题"+str(get_time_stamp16())
        description = "本次接口已测试为主，不可胡乱添加到前端，请谨慎添加或者关联到前端"
        categoryId = 0
        catalog = "/Business/Img/"
        headImg = list(oss_file("information", "img01.jpg", catalog, url1, headers))[-1]
        backgroundImg = list(oss_file("information", "img02.jpg", catalog, url1, headers))[-1]
        paylo = {
            "name": name,
            "description": description,
            "categoryId": categoryId,
            "headImg": headImg,
            "backgroundImg": backgroundImg
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)
        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="新增专题"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        assert j.get("data") == True
