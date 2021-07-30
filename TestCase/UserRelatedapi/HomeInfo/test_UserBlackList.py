# test_UserBlackList
import json
import logging

import allure
import pytest

from Common.get_time_stamp import get_time_stamp13
from Common.login import login
from Common.show_sql import showsql

from Common.sign import get_sign

from Common.requests_library import Requests

from Common.tools.read_write_yaml import yamltoken

from glo import JSON, HTTP


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('黑名单-黑名单列表')
class TestUserBlackList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        login()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_UserBlackList(self):
        # 拼装参数
        header = {}
        header.update(JSON)
        headers = {}
        headers.update(header)
        token = {"token": yamltoken()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        createTime = get_time_stamp13()

        url = HTTP + "/as_user/api/user_black/v1/list"
        paylo = {
            "createTime": createTime,
            "pageSize": 20
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="黑名单列表"
        )
        j = r.json()
        # print(j)
        assert r.status_code == 200
        if j.get("code") == "000000":
            assert j.get("msg") == "ok"
            if "data" in j:
                userId = showsql(
                    '192.168.1.237', 'root', '123456', "user_account",
                    "select user_id from t_user_account where `zr_no`= '10000049';"
                )

                assert j.get("data")[-1].get("userId") == list(list(userId)[0])[0]

                assert j.get("data")[-1].get("createTime") == 1614237549000



        else:
            raise ValueError(f"{j}")
