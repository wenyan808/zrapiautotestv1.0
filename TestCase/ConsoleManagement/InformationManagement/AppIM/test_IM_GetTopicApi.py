# test_IM_GetTopicApi   查询主题接口    /as_stock_information/api/topic/v1/get
import json
import logging
import random

import allure
import pytest

from Common.getConsoleLogin import getConsoleLogin_token
from Common.get_time_stamp import stampToTime

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import BASE_DIR, HTTP, JSON


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('资讯app_查询主题接口')
class TestIMGetTopicApi():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/testIMData/test_IM_GetTopicApi.json"))
    def test_IM_GetTopicApi(self, info):
        url = HTTP + "/as_stock_information/api/topic/v1/get"
        header = {}
        header.update(JSON)


        paylo = info
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)
        headers = {}
        headers.update(header)
        # print(token)
        # print(type(token))
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        payload = json.dumps(dict(payload1))
        # time.sleep(60.01)

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="查询主题接口"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        if "data" in j:
            if len(j.get("data")) != 0:
                assert "id" in j.get("data")
                assert "categoryId" in j.get("data")
                assert "name" in j.get("data")
                assert "description" in j.get("data")
                if "backgroundImg" in j.get("data"):
                    assert "https://zhuorui-public-test.oss-cn-shenzhen.aliyuncs.com/information/" \
                           in j.get("data").get("backgroundImg")
                elif "headImg" in j.get("data"):
                    assert j.get("data").get("headImg") == \
                           "https://zhuorui-public-test.oss-cn-shenzhen.aliyuncs.com/" \
                           "information/20210621/13bd8850-d25a-11eb-94bb-5904ce8ea223.jpg"
                else:
                    raise AssertionError(j.get("data"))
            else:
                logging.info("data为空")
        else:
            logging.info("data不在j中")
