# test_EM_VoucherDetail
import json
import logging
import random

import allure
import pytest

from Common.getConsoleLogin import getConsoleLogin_token

from Common.sign import get_sign

from Common.requests_library import Requests

from glo import console_JSON, console_HTTP


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('活动管理console_权益详情')
class TestEMVoucherDetail():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_EM_VoucherDetail(self):
        url = console_HTTP + "/api/con_voucher/v1/list"
        header = console_JSON

        # 拼装参数
        paylo = {}
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)
        headers = {}
        headers.update(header)
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="权益列表"
        )

        j = r.json()
        # print(j)
        # print(j.get('data').get('list')[0].get('voucherId'))

        url_detail = console_HTTP + "/api/con_voucher/v1/detail"
        paylo_detail = {"voucherId": f"{j.get('data').get('list')[0].get('voucherId')}"}
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo_detail)
        payload1.update(sign1)
        payload = json.dumps(dict(payload1))
        r = Requests(self.session).post(
            url=url_detail, headers=headers, data=payload, title="权益详情"
        )
        j = r.json()
        # print(j)
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        if "data" in j:
            if len(j.get("data")) != 0:
                assert "voucherId" in j.get("data")
                assert "voucherName" in j.get("data")
                assert "description" in j.get("data")
                assert "usedType" in j.get("data")
                assert "type" in j.get("data")
                assert "createTime" in j.get("data")
                assert "voucherTotalNum" in j.get("data")
                assert "voucherAvailableNum" in j.get("data")
                assert "stop" in j.get("data")

            else:
                logging.info("data为空")

        else:
            logging.info("data不在j中")
