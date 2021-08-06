# test_USetf_stockpage
import json
import logging
import allure
import requests

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
from Common.sign import get_sign
from Common.tools.read_write_yaml import yamltoken
from glo import HTTP, JSON


# @pytest.mark.skip(reason="调试中")
@allure.feature('美股相关')
class TestUSUSetfStockpage:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('etf获取成分股-查看更多')
    def test_USetf_stockpage(self):
        response = zhuorui("Allstock", "etf获取成分股-查看更多")
        assert_data(response, '000000', 'ok')

        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                assert "list" in response.json().get("data")
                for i in range(len(response.json().get("data").get("list"))):
                    assert "ts" in response.json().get("data").get("list")[i]
                    assert "code" in response.json().get("data").get("list")[i]
                    assert "type" in response.json().get("data").get("list")[i]
                    assert "name" in response.json().get("data").get("list")[i]
                    assert "rate" in response.json().get("data").get("list")[i]
                assert "total" in response.json().get("data")
                assert "pageSize" in response.json().get("data")
                assert "currentPage" in response.json().get("data")
                # assert type(response.json().get("data").get("total")) ==
                # assert response.json().get("data").get("pageSize") == paylo.get("pageSize")
                # assert response.json().get("data").get("currentPage") == paylo.get("currentPage")

            else:
                logging.info("data为空，无数据")

        else:
            logging.info("无data字段")
