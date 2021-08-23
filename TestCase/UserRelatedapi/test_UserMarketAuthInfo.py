# test_UserMarketAuthInfo
import json

import allure
import pytest

from Common.login import login
from Common.sign import get_sign

from Common.requests_library import Requests

from Common.tools.read_write_yaml import yamltoken

from glo import JSON, HTTP


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('用户相关接口-获取用户市场行情权限')
class TestUserMarketAuthInfo():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        login()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_UserMarketAuthInfo(self):
        # 拼装参数
        header = {}
        header.update(JSON)
        headers = {}
        headers.update(header)
        token = {"token": yamltoken()}
        headers.update(token)  # 将token更新到headers
        # print(headers)

        url1 = HTTP + "/as_user/api/user_market_auth/v1/info"
        paylo = {}
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url1, headers=headers, data=payload, title="获取用户市场行情权限"
        )
        j = r.json()
        # print(j1)
        assert r.status_code == 200
        if j.get("code") == "000000":
            assert j.get("msg") == "ok"
            assert "hkAuth" in j.get("data")
            assert "usAuth" in j.get("data")
            assert j.get("data").get("aAuth") == 'LV1'


        else:
            raise ValueError(f"{j}")

