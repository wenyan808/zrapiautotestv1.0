# test_RefreshToken
import json

import allure
import pytest

from Common.getTestLoginToken import getlogintoken
from Common.sign import get_sign

from Common.requests_library import Requests


from glo import JSON2, HTTP, phoneArea, pwd1


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('用户相关接口-token刷新')
class TestRefreshToken():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_RefreshToken(self):
        # 拼装参数
        headers = JSON2

        phone = "13321165200"
        # password = "zr123456"
        password = pwd1

        headers_token = getlogintoken(phone, password, phoneArea)
        headers1 = {}
        headers1.update(headers)
        token = {"token": headers_token}
        # print(type(token))
        headers1.update(token)  # 将token更新到headers
        url_token = HTTP + "/as_user/api/user_account/v1/refresh_token"
        paylo_token = {}
        sign2 = {"sign": get_sign(paylo_token)}  # 把参数签名后通过sign1传出来
        payload2 = {}
        payload2.update(paylo_token)
        payload2.update(sign2)

        payload_token = json.dumps(dict(payload2))

        r_token = Requests(self.session).post(
            url=url_token, headers=headers1, data=payload_token, title="token刷新"
        )

        j_token = r_token.json()
        # print(j_token)
        assert r_token.status_code == 200
        try:
            assert j_token.get("code") == "000000"
            assert j_token.get("msg") == "ok"
            assert len(j_token.get("data")) != 0

        except:
            raise ValueError(
                f"\n请求地址：{url_token}"
                f"\nbody参数：{payload_token}"
                f"\n请求头部参数：{headers1}"
                f"\n返回数据结果：{j_token}"
            )
