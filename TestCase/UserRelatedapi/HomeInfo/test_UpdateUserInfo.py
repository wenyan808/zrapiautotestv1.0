# test_UpdateUserInfo
import json

import allure
import pytest

from Common.login import login
from Common.show_sql import showsql
from Common.sign import get_sign

from Common.requests_library import Requests

from Common.tools.read_write_yaml import yamltoken

from glo import JSON, HTTP, zrNo, phone, nickname, headPhoto


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('主页信息-修改用户信息')
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
        sex = 3
        url1 = HTTP + "/as_user/api/user_info/v1/update"
        paylo = {
            "sex": sex
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url1, headers=headers, data=payload, title="修改用户信息"
        )
        j = r.json()
        # print(j)
        assert r.status_code == 200
        if j.get("code") == "000000":
            assert j.get("msg") == "ok"
            if "data" in j:
                userId = showsql(
                    '192.168.1.237', 'root', '123456', "user_account",
                    "select user_id from t_user_account where `zr_no`= '68904140';"
                )
                assert j.get("data").get("userId") == list(list(userId)[0])[0]
                assert j.get("data").get("sex") == sex


        else:
            raise ValueError(f"{j}")
