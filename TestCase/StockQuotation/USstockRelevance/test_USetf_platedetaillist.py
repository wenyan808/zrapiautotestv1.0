# test_USetf_platedetaillist
import json
import logging

import allure
import pytest
import requests

from Common.login import login

from Common.sign import get_sign

from Common.tools.read_yaml import yamltoken
from glo import HTTP, JSON


# @pytest.mark.skip(reason="调试中")
@allure.feature('美股相关')
class TestUSetfplatelist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('美股etf板块etf详情页')
    def test_USetf_platelist(self):
        # pass
        url = HTTP + "/as_market/api/us/etf/plate/v1/detail/list"
        headers = JSON

        # 拼装参数
        paylo = {}
        # paylo = info
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        # 调用登录接口通过token传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)
        headers = headers
        # print(token)
        # print(type(token))

        token1 = yamltoken()
        token = {"token": token1}
        headers.update(token)
        # print(headers)
        payload = json.dumps(dict(payload1))
        # time.sleep(1)
        r = requests.post(url=url, headers=headers, data=payload)
        # 断言
        j = r.json()
        # print(j)

        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        if "data" in j:
            if len(j.get("data")) != 0:
                assert "sectionTitle" in j.get("data")
                assert "data" in j.get("data")
                for i in range(len(j.get("data").get("data"))):
                    assert "plateName" in j.get("data").get("data")[i]
                    assert "plateDiffRate" in j.get("data").get("data")[i]
                    assert "name" in j.get("data").get("data")[i]
                    assert "diffRate" in j.get("data").get("data")[i]
                    assert "delay" in j.get("data").get("data")[i]
                    if str(j.get("data").get("data")[i].get("delay")) == "true":
                        logging.info("实时数据")
                    else:
                        logging.info("延时数据")
                # assert j.get("data").get("total") == 65
                # assert j.get("data").get("pageSize") == 15
                # assert j.get("data").get("currentPage") == 1
                # print(j.get("data"))

            else:
                logging.info("data为空，无数据")

        else:
            logging.info("无data字段")
