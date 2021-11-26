# test_SignOut
import json

import allure
import pytest

from Business.Urlpath.UrlPath_userlogin import UrlPath_sign_out
from Common.getTestLoginToken import getlogintoken
from Common.register_common import get_registerno
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import JSON2, HTTP, phoneArea, pwd1, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('用户相关接口-退出登陆')
class TestSignOut():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/UserRelatedapiData/SignOut.json"))
    def test_SignOut(self, info):
        # 登出的url
        url_SignOut = HTTP + UrlPath_sign_out
        # 注册并获取手机号
        sign_in = list(get_registerno())
        phone = sign_in[0]
        # 获取登录密码
        # password = "zr123456"
        password = pwd1
        # 调取登录接口并获取token
        headers_token = getlogintoken(phone, password, phoneArea)
        # 拼装headers参数，从注册接口获取headers
        headers = {}
        headers.update(sign_in[-1])
        headers1 = {}
        headers1.update(headers)
        token = {"token": headers_token}
        # print(type(token))
        headers1.update(token)  # 将token更新到headers

        paylo_SignOut = info
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
        try:
            assert j_SignOut.get("code") == "000000"
            assert j_SignOut.get("msg") == "ok"
        except:
            raise AssertionError(
                f"\n请求地址：{url_SignOut}"
                f"\nbody参数：{payload_SignOut}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j_SignOut}")
