# test_Community_DeleteSensitiveWord
import json
import logging
import random

import allure
import pytest

from Common.getConsoleLogin import getConsoleLogin_token
from Common.get_time_stamp import TimeTostamp, get_time_stamp13


from Common.sign import get_sign

from Common.requests_library import Requests

from glo import console_JSON, console_HTTP


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('社区console_删除敏感词')
class TestCommunityDeleteSensitiveWord():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()


    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_Community_DeleteSensitiveWord(self):
        url = console_HTTP + "/api/con_sensitive_word/v1/add"
        headers = console_JSON

        # 拼装参数
        paylo = {
            "name": "中国共产党",
            "type": 1,
            "sensitiveType": 2
        }
        # paylo = info
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)
        headers = headers
        # print(token)
        # print(type(token))
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        payload = json.dumps(dict(payload1))
        # time.sleep(60.01)

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="添加敏感词"
        )

        j = r.json()
        # logging.info(j)
        url_list = console_HTTP + "/api/con_sensitive_word/v1/list"
        paylo_list = {
            "name": paylo.get("name"),
            "type": paylo.get("type"),
            "startTime": TimeTostamp(),
            "endTime": get_time_stamp13()
        }
        sign1 = {"sign": get_sign(paylo_list)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo_list)
        payload1.update(sign1)
        payload = json.dumps(dict(payload1))
        r_list = Requests(self.session).post(
            url=url_list, headers=headers, data=payload, title="敏感词列表"
        )
        j_list = r_list.json()
        # print(j_list)
        url_delete = console_HTTP + "/api/con_sensitive_word/v1/delete"
        if len(j_list.get("data").get("list"))!=0:
            paylo_delete = {
                "id": j_list.get("data").get("list")[0].get("id")
            }
            # print(j_list.get("data").get("list")[0].get("id"))
            sign1 = {"sign": get_sign(paylo_delete)}  # 把参数签名后通过sign1传出来
            payload1 = {}
            payload1.update(paylo_delete)
            payload1.update(sign1)
            payload = json.dumps(dict(payload1))
            r_delete = Requests(self.session).post(
                url=url_delete, headers=headers, data=payload, title="删除敏感词"
            )
            j_delete = r_delete.json()
            # print(j_delete)
            assert j_delete.get("code") == "000000"
            assert j_delete.get("msg") == "ok"
        else:
            raise ValueError(j_list.get("data").get("list"))