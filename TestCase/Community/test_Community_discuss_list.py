# test_Community_discuss_list
import json

import allure
import pytest

from Common.login import login
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_yaml import yamltoken
from glo import HTTP, JSON


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('社区列表-讨论区列表')
class TestCommunitycommentdiscuss_list():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_Community_discuss_list(self):
        login()  # 调用登录接口通过token传出来
        url = HTTP + "/as_community/api/community/v1/discuss_list"
        headers = JSON
        stocks = [
            {
                "ts": "HK",
                "code": "00700",
                "name": "腾讯控股",
                "type": 2
            }
        ]
        # 拼装参数
        paylo = {
            "stocks": stocks
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
            url=url, headers=headers, data=payload, title="讨论区列表"
        )
        y = r.json()
        # print(y)
        # print(r.json())
        # 断言
        assert r.status_code == 200
        assert y.get("code") == "000000"
        assert y.get("msg") == "ok"
