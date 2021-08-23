# test_ETF_planklist

import logging

import allure
import pytest
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
from Common.tools.read_write_json import get_json
from glo import BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('ETF相关')
class TestETFplanklist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('etf板块成分股')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/AllStockData/test_ETF_planklist.json"))
    def test_ETF_planklist(self, info):
        response = zhuorui("Allstock", "etf板块成分股", info)
        assert_data(response, '000000', 'ok')

        assert response.status_code == 200
        if response.json().get("code") == "000000":
            assert response.json().get("code") == "000000"
            assert response.json().get("msg") == "ok"
            if "data" in response.json():
                if len(response.json().get("data")) != 0:
                    for i in range(len(response.json().get("data"))):
                        assert "ts" in response.json().get("data")[i]
                        assert "code" in response.json().get("data")[i]
                        assert "type" in response.json().get("data")[i]
                        assert "delay" in response.json().get("data")[i]
                        assert "name" in response.json().get("data")[i]
                        # assert "last" in response.json().get("data")[i]
                        if "preClose" in response.json().get("data")[i]:
                            assert "preClose" in response.json().get("data")[i]
                        elif "turnover" in response.json().get("data")[i]:
                            assert "turnover" in response.json().get("data")[i]
                        elif "sharestraded" in response.json().get("data")[i]:
                            assert "sharestraded" in response.json().get("data")[i]
                        elif "volumeRatio" in response.json().get("data")[i]:
                            assert "volumeRatio" in response.json().get("data")[i]
                        elif "amplitude" in response.json().get("data")[i]:
                            assert "amplitude" in response.json().get("data")[i]
                        elif "diffRate" in response.json().get("data")[i]:
                            assert "diffRate" in response.json().get("data")[i]
                        elif "diffPrice" in response.json().get("data")[i]:
                            assert "diffPrice" in response.json().get("data")[i]
                        elif "comparison" in response.json().get("data")[i]:
                            assert "comparison" in response.json().get("data")[i]
                        # assert "totalMarkValue" in response.json().get("data")[i]
                        if "direction" in response.json().get("data")[i]:
                            assert "direction" in response.json().get("data")[i]
                            assert "lever" in response.json().get("data")[i]
                        elif "totalCapitalStock" in response.json().get("data")[i]:
                            assert "totalCapitalStock" in response.json().get("data")[i]

                        elif str(response.json().get("data")[i].get("delay")) == "true":
                            logging.info("实时数据")
                        else:
                            logging.info("延时数据")

                else:
                    logging.info("data为空，无数据")

            else:
                logging.info("无data字段")

        elif response.json().get("code") == "000103":
            assert response.json().get("code") == "000103"
            assert response.json().get("msg") == "sortItem out of range"

        else:
            raise AssertionError(response.json())

