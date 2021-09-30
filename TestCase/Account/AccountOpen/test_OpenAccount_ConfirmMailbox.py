# test_OpenAccount_ConfirmMailbox    用户确定收到邮件         /as_user/api/open/v1/confirm_mailbox
import json
import logging
import random

import allure
import pytest

from Business.IdentityInformation import mailbox
from Common.Accountcommon.getLoginAccountToken import GetLoginAccountToken
from Common.sign import get_sign

from Common.requests_library import Requests

from glo import HTTP, JSON


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('开户app_用户确定收到邮件')
class TestOpenAccountConfirmMailbox():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    # @pytest.mark.parametrize('info',
    #                          get_json(BASE_DIR + r"/TestData/testIMData/test_IM_conNewsList.json"))
    def test_OpenAccount_ConfirmMailbox(self):
        url = HTTP + "/as_user/api/open/v1/confirm_mailbox"

        headers = {}
        headers.update(JSON)
        token = {"token": GetLoginAccountToken()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        paylo = {}
        # paylo = info
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="用户确定收到邮件"
        )

        j = r.json()
        # print(j)

        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"

