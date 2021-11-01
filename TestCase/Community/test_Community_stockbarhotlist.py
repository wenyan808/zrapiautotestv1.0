# test_Community_stockbarhotlist
import json

import allure
import pytest

from Common.get_time_stamp import TimeTostamp
from Common.login import login
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_yaml import yamltoken
from glo import HTTP, JSON


@pytest.mark.skip(reason="调试中 ")
@allure.feature('股吧列表-热门列表')
class TestCommunitycommentstockbarhot_list():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        login()  # 调用登录接口通过token传出来

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_Community_stockbarhot_list(self):
        # login()  # 调用登录接口通过token传出来
        url = HTTP + "/as_community/api/stock_bar/v1/hot_list"
        headers = {}
        headers.update(JSON)

        # 拼装参数
        paylo = {

            "ts": "HK",
            "code": "00700",
            "publishTime": TimeTostamp(),
            "pageSize": 20



        }
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        # print(token)
        # print(type(token))
        token1 = yamltoken()
        token = {"token": token1}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        payload = json.dumps(dict(payload1))
        # time.sleep(60.01)

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="股吧热门列表"
        )
        y = r.json()
        # print(y)
        # 断言
        assert r.status_code == 200
        assert y.get("code") == "000000"
        assert y.get("msg") == "ok"