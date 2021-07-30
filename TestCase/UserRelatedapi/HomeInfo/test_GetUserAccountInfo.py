# test_GetUserAccountInfo
import json

import allure
import pytest

from Common.login import login
from Common.show_sql import showsql
from Common.sign import get_sign

from Common.requests_library import Requests

from Common.tools.read_write_yaml import yamltoken

from glo import JSON, HTTP


@pytest.mark.skip(reason="调试中 ")
@allure.feature('主页信息-获取用户信息')
class TestGetUserAccountInfo():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        login()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_GetUserAccountInfo(self):
        # 拼装参数
        header = JSON
        headers = {}
        headers.update(header)
        token = {"token": yamltoken()}
        headers.update(token)  # 将token更新到headers
        # print(headers)

        url1 = HTTP + "/as_user/api/user_account/v1/by_user_id"
        paylo = {}
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url1, headers=headers, data=payload, title="获取用户信息"
        )
        j = r.json()
        # print(j)
        assert r.status_code == 200
        if j.get("code") == "000000":
            assert j.get("msg") == "ok"





        else:
            raise ValueError(f"{j}")
