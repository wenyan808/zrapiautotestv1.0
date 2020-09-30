
import logging

import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


# test_HSGT_get60TradeDate
@pytest.mark.skip(reason="调试中")
@allure.feature('沪深港股通资金流向排行榜')
class TestHSGTget60TradeDate:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('查询最近60个交易日期_HKandSH')
    def test_HSGT_get60TradeDate_HKandSH(self):
        response = zhuorui('沪深港通', '查询最近60个交易日期_HKandSH')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        print(response.json())
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                # assert "date" in response.json().get("data")
                assert "ts" in response.json().get("data")
                if len(response.json().get("data").get("date")) != 0:
                    for i in range(len(response.json().get("data").get("list"))):
                        pass

            else:
                logging.info("data是空的集合")

        else:

            logging.info("无data数据")
