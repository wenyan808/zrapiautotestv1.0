# test_EM_conVoucherUpdate      修改停用权益(二期修改)              /api/con_voucher/v1/update
import json
import logging
import random

import allure
import pytest

from Common.conVoucher_common.get_Voucherid import getvoucherId, delvoucherId
from Common.getConsoleLogin import getConsoleLogin_token
from Common.get_time_stamp import gettoday

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_JSON, console_HTTP, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('活动管理console_修改停用权益(二期修改)')
class TestEMconVoucherUpdate():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/test_EventManagementdata/test_EM_conVoucherUpdate.json"))
    def test_EM_conVoucherUpdate(self, info):
        url = console_HTTP + "/api/con_voucher/v1/update"
        header = console_JSON

        voucherId = getvoucherId(info.get("type"))
        paylo1 = {
            "description": info.get("description") + str(gettoday()),
            "applyType": info.get("applyType"),
            "applyNum": info.get("applyNum"),
            "stop": info.get("stop")
        }
        paylo = {
            "voucherId": voucherId
        }

        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(paylo1)
        payload1.update(sign1)
        headers = {}
        headers.update(header)
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="修改停用权益(二期修改)"
        )

        j = r.json()
        # print(j)
        delvoucherId(voucherId)
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
