# test_EM_VoucherList
import json
import logging
import random

import allure
import pytest

from Common.getConsoleLogin import getConsoleLogin_token

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import console_JSON, console_HTTP, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('活动管理console_权益列表')
class TestEMVoucherList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/test_EventManagementdata/test_EM_VoucherList.json"))
    def test_EM_VoucherList(self, info):
        url = console_HTTP + "/api/con_voucher/v1/list"
        header = console_JSON

        # 拼装参数
        paylo = info
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
        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        if "data" in j:
            if len(j.get("data")) != 0:
                assert "total" in j.get("data")
                assert "pageSize" in j.get("data")
                assert "currentPage" in j.get("data")
                if "list" in j.get("data"):
                    if j.get("data").get("list") != None:
                        for i in range(len(j.get("data").get("list"))):
                            assert "voucherId" in j.get("data").get("list")[i]
                            assert "voucherId" in j.get("data").get("list")[i]
                            assert "usedType" in j.get("data").get("list")[i]
                            assert "type" in j.get("data").get("list")[i]
                            assert "voucherTotalNum" in j.get("data").get("list")[i]
                            assert "voucherAvailableNum" in j.get("data").get("list")[i]
                            assert "stop" in j.get("data").get("list")[i]
                            assert "operator" in j.get("data").get("list")[i]
                            assert "updateTime" in j.get("data").get("list")[i]

                    else:
                        logging.info("list为空")
                else:
                    logging.info("list不在data中")
            else:
                logging.info("data为空")
        else:
            logging.info("data不在j中")
