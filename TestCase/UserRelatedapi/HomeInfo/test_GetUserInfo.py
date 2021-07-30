# test_GetUserInfo
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
@allure.feature('主页信息-获取用户信息(包含统计信息)')
class TestGetUserInfo():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        login()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_GetUserInfo(self):
        # 拼装参数
        header = JSON
        headers = {}
        headers.update(header)
        token = {"token": yamltoken()}
        headers.update(token)  # 将token更新到headers
        # print(headers)

        url1 = HTTP + "/as_user/api/user_info/v1/info"
        paylo = {}
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url1, headers=headers, data=payload, title="获取用户信息(包含统计信息)"
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
                assert j.get("data").get("zrNo") == zrNo
                assert j.get("data").get("phone") == phone
                assert j.get("data").get("phoneArea") == "86"
                assert j.get("data").get("headPhoto") == headPhoto
                assert j.get("data").get("nickname") == nickname
                assert "followCount" in j.get("data")
                assert "fansCount" in j.get("data")
                assert "discussCount" in j.get("data")
                assert "stockSelectedCount" in j.get("data")


        else:
            raise ValueError(
                f"\n请求地址：{url1}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}"
            )
