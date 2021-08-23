# test_GetConnectBalance
import json


import allure
import pytest
import requests

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


from Common.sign import get_sign


from Common.tools.read_write_yaml import yamltoken
from glo import HTTP, JSON


# @pytest.mark.skip(reason="调试中")
@allure.feature('资金流向')
class TestGetConnectBalance:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('查询当天的北向最新资金')
    def test_GetConnectBalance(self):
        response = zhuorui("Allstock", "查询当天的北向最新资金")
        assert_data(response, '000000', 'ok')

        if "data" in response.json():
            assert "direction" in response.json().get("data")
            assert "curTime" in response.json().get("data")
            assert "curBalanceSH" in response.json().get("data")
            assert "curBalanceSZ" in response.json().get("data")


    @allure.story('查询当天的南向最新资金')
    def test_GetConnectBalance_SB(self):

        response = zhuorui("Allstock", "查询当天的北向最新资金")
        # assert_data(response, '000000', 'ok')

        assert response.status_code == 200
        if response.json().get("code") == "000000":
            assert response.json().get("code") == "000000"
            assert response.json().get("msg") == "ok"
            if "data" in response.json():
                assert "direction" in response.json().get("data")
                assert "curTime" in response.json().get("data")
                assert "curBalanceSH" in response.json().get("data")
                assert "curBalanceSZ" in response.json().get("data")
        elif response.json().get("code") == "270403":
            assert response.json().get("code") == "270403"
            assert response.json().get("msg") == "只允许北向资金查询"
        else:
            raise AssertionError(print(response.json()))
