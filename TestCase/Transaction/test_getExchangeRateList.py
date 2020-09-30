import logging

import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


# test_getExchangeRateList

# @pytest.mark.skip(reason="调试中")
class TestgetExchangeRateList:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('行情汇率列表')
    def test_getExchangeRateList(self):
        response = zhuorui('交易', '行情汇率列表')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                for i in range(len(response.json().get("data"))):
                    assert "currency" in response.json().get("data")[i]
                    assert "rate" in response.json().get("data")[i]



            else:
                logging.info("data是空的集合")

        else:

            logging.info("无data数据")
