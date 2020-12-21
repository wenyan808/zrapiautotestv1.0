import logging

import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


# test_HSGT_get60TradeDate
# @pytest.mark.skip(reason="调试中")
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
        # print(response.json())
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                # print(type(response.json().get("data")[0]))
                # print(response.json().get("data")[0])
                # print(response.json().get("data")[1])
                assert "date" in response.json().get("data")[0]
                assert "ts" in response.json().get("data")[0]
                if len(response.json().get("data")[0].get("date")) != 0:
                    assert response.json().get("data")[0].get("ts") == "HK"
                    # print(response.json().get("data")[0]["date"][0])
                    assert len(response.json().get("data")[0]["date"]) == 60

            else:
                logging.info("data是空的集合")

        else:

            logging.info("无data数据")
