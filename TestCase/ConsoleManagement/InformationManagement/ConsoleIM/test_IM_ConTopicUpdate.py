# test_IM_ConTopicUpdate      修改专题       /api/con_topic/v1/update
import json
import logging
import random

import allure
import pytest

from Common.ConTopic_common.get_ConTopicID import get_ConTopicID
from Common.OSS import oss_file


from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_HTTP, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('资讯console_修改专题')
class TestIMConTopicUpdate():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    # @pytest.mark.parametrize('info',
    #                          get_json(BASE_DIR + r"/TestData/testIMData/test_IM_conNewsList.json"))
    def test_IM_ConTopicUpdate(self):
        url = console_HTTP + "/api/con_topic/v1/update"
        url1 = console_HTTP + "/api/con_sts/v1/token"
        list1 =list(get_ConTopicID())
        headers = list1[1]
        id = list1[0]
        name = "自动化测试专题01"
        description = "本次接口已测试为主，不可胡乱添加到前端，请谨慎添加或者关联到前端,可以删除"
        category_id = 1
        catalog = "/Business/Img/"
        headImg = list(oss_file("information", "img03.jpg", catalog, url1, headers))[-1]
        backgroundImg = list(oss_file("information", "img04.jpg", catalog, url1, headers))[-1]
        isHot = 0

        paylo = {
            "name": name,
            "description": description,
            "headImg": headImg,
            "backgroundImg": backgroundImg,
            "category_id": category_id,
            "isHot": isHot,
            "id": id
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)
        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="修改专题"
        )

        j = r.json()

        # print(j)
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        assert j.get("data") == True
