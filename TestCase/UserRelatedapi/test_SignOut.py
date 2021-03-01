# test_SignOut
import json

import allure
import pytest

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.md5 import get_md5
from Common.tools.read_yaml import yamltoken

from glo import JSON, HTTP


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('用户相关接口-退出登陆')
class TestSignOut():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_SignOut(self):
        # 拼装参数
        headers = JSON

        phone = "13321165200"
        password = "zr123456"
        url = HTTP + "/as_user/api/user_account/v1/user_login_pwd"
        paylo = {
            "password": get_md5(password),
            "phone": phone,
            "phoneArea": "86"
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="用户密码登陆"
        )

        j = r.json()
        # print(j)
        headers_token = j.get("data").get("token")
        headers1 = {}
        headers1.update(header)
        token = {"token": headers_token}
        # print(type(token))
        headers1.update(token)  # 将token更新到headers
        url_SignOut = HTTP + "/as_user/api/user_account/v1/sign_out"
        paylo_SignOut = {
            "osType": "all"
        }
        sign2 = {"sign": get_sign(paylo_SignOut)}  # 把参数签名后通过sign1传出来
        payload2 = {}
        payload2.update(paylo_SignOut)
        payload2.update(sign2)

        payload_SignOut = json.dumps(dict(payload2))

        r_SignOut = Requests(self.session).post(
            url=url_SignOut, headers=headers1, data=payload_SignOut, title="退出登陆"
        )

        j_SignOut = r_SignOut.json()
        # print(j_SignOut)
        assert r_SignOut.status_code == 200
        assert j_SignOut.get("code") == "000000"
        assert j_SignOut.get("msg") == "ok"
