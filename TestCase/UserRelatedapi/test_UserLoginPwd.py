# test_UserLoginPwd
import json

import allure
import pytest

from Business.Urlpath.UrlPath_userlogin import UrlPath_user_login_pwd
from Common.register_common import get_registerno
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.md5 import get_md5


from glo import JSON, HTTP, phoneArea, pwd1


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('用户相关接口-用户密码登陆')
class TestUserLoginPwd():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_UserLoginPwd(self):
        # 用户密码登录url
        url = HTTP + UrlPath_user_login_pwd
        # 注册并获取手机号
        sign_in = list(get_registerno())
        phone = sign_in[0]
        # 拼装headers参数
        headers = {}
        headers.update(sign_in[-1])

        # phone = "13321165200"
        password = pwd1

        paylo = {
            "loginPassword": get_md5(password),
            "phone": phone,
            "phoneArea": phoneArea
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
        assert r.status_code == 200
        try:
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
            if "data" in j:
                assert j.get("data").get("phone") == paylo.get("phone")
                assert j.get("data").get("phoneArea") == paylo.get("phoneArea")
                assert "token" in j.get("data")
                assert "userId" in j.get("data")
        except:
            raise AssertionError(
                f"\n请求地址：{url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}")
