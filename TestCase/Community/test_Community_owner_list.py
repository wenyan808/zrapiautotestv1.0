# test_Community_owner_list
import json

import allure
import pytest

from Common.get_time_stamp import get_time_stamp13
from Common.login import login
from Common.show_sql import showsql
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_yaml import yamltoken
from glo import HTTP, JSON


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('个人主页-用户主贴查询')
class TestCommunitycommentowner_list():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        login()  # 调用登录接口通过token传出来

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_Community_owner_list(self):
        # login()  # 调用登录接口通过token传出来
        url = HTTP + "/as_community/api/post/v1/owner_list"
        headers = JSON
        userId = showsql(
            '192.168.1.237', 'root', '123456', "user_account",
            "select user_id from t_user_account where `zr_no`= '68904140';"
        )
        # 拼装参数
        paylo = {

            "userId": str(userId[3:-5:]),
            "publishTime": get_time_stamp13(),
            "pageSize": 20

        }
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)
        headers = headers
        # print(token)
        # print(type(token))
        token1 = yamltoken()
        token = {"token": token1}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        payload = json.dumps(dict(payload1))
        # time.sleep(60.01)

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="用户主贴查询"
        )
        y = r.json()
        # print(y)
        # 断言
        assert r.status_code == 200
        assert y.get("code") == "000000"
        assert y.get("msg") == "ok"
