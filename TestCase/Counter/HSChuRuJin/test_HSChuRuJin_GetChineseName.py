# test_HSChuRuJin_GetChineseName    用户中文姓名查询     /as_user/api/client/v1/get_name
import json

import allure
import pytest

from Common.Accountcommon.accountAuth import AccountAuth

from Common.sign import get_sign

from Common.requests_library import Requests


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_用户中文姓名查询')
class TestHSChuRuJinGetChineseName():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_HSChuRuJin_GetChineseName(self):
        login_list = list(AccountAuth())
        http = login_list[-1]
        headers = login_list[1]

        url = http + "/as_user/api/client/v1/get_name"

        paylo = {}

        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload2 = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload2, title="用户中文姓名查询"
        )

        j = r.json()

        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("msg") == 'ok'
            assert j.get("code") == "000000"
        except:
            raise AssertionError(j)