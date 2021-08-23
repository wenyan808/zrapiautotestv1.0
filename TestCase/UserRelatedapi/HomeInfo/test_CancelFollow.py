# test_CancelFollow
import json
import logging

import allure
import pytest

from Common.login import login
from Common.show_sql import showsql
from Common.sign import get_sign

from Common.requests_library import Requests

from Common.tools.read_write_yaml import yamltoken

from glo import JSON, HTTP


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('主页信息-取消用户关注')
class TestCancelFollow():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        login()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_CancelFollow(self):
        # 拼装参数
        header = {}
        header.update(JSON)
        headers = {}
        headers.update(header)
        token = {"token": yamltoken()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        userId = showsql(
            '192.168.1.237', 'root', '123456', "user_account",
            "select user_id from t_user_account where `zr_no`= '98363547';"
        )

        url = HTTP + "/as_user/api/follow/v1/add"
        paylo = {
            "userId": list(list(userId)[0])[0]
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="关注用户"
        )
        j = r.json()
        # print(j)
        url1 = HTTP + "/as_user/api/follow/v1/cancel"
        paylo1 = {
            "userId": list(list(userId)[0])[0]
        }
        sign1 = {"sign": get_sign(paylo1)}  # 把参数签名后通过sign1传出来
        payload2 = {}
        payload2.update(paylo1)
        payload2.update(sign1)

        payload3 = json.dumps(dict(payload2))

        r1 = Requests(self.session).post(
            url=url1, headers=headers, data=payload3, title="取消用户关注"
        )
        j1 = r1.json()
        # print(j1)
        assert r1.status_code == 200
        if j1.get("code") == "000000":
            assert j1.get("msg") == "ok"
            if j1.get("data") == True:
                logging.info("取消用户关注")

            else:
                logging.info("未取消用户关注")


        else:
            raise ValueError(f"{j1}")