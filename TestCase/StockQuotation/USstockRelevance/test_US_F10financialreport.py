# test_US_F10financialreport
import json
import logging

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
@allure.feature('美股相关')
class TestUSF10dividendlist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('美股F10财报')
    def test_US_financialreport(self):
        response = zhuorui("Allstock", "美股F10财报")
        assert_data(response, '000000', 'ok')

        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                assert "mainBusinessReport" in response.json().get("data")
                assert "profitDetailUrl" in response.json().get("data")
                assert "liabilDetailUrl" in response.json().get("data")
                assert "cashFlowDetailUrl" in response.json().get("data")
                assert "profitReport" in response.json().get("data")
                assert "liabilistyReport" in response.json().get("data")
                assert "cashFlowReport" in response.json().get("data")

            else:
                logging.info("data为空，无数据")

        else:
            logging.info("无data字段")