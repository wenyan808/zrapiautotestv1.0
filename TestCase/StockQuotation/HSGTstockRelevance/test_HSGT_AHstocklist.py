# test_HSGT_AHstocklist
import logging
import allure
import pytest
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
from Common.tools.read_write_json import get_json
from glo import BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('沪深港通')
class TestHSGTAHstocklist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('沪深港通-AH股成分股列表')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/test_HSGT_AHstocklist.json"))
    def test_HSGT_AHstocklist(self, info):

        response = zhuorui('Allstock', '沪深港通-AH股成分股列表', info)
        assert_data(response, '000000', 'ok')

        assert response.status_code == 200
        assert response.json().get("code") == "000000"
        assert response.json().get("msg") == "ok"
        if "data" in response.json():
            for i in range(len(response.json().get("data"))):
                assert "ts" in response.json().get("data")[i]
                assert "code" in response.json().get("data")[i]
                assert "type" in response.json().get("data")[i]
                assert "name" in response.json().get("data")[i]
                assert "alast" in response.json().get("data")[i]
                assert "apreClose" in response.json().get("data")[i]
                assert "hlast" in response.json().get("data")[i]
                assert "hpreClose" in response.json().get("data")[i]
                assert "premium" in response.json().get("data")[i]
                assert "totalMarkValue" in response.json().get("data")[i]
                assert "peRatioStatic" in response.json().get("data")[i]
                assert "delay" in response.json().get("data")[i]
                if response.json().get("data")[i].get("delay") == False:
                    logging.info("实时数据")
                else:
                    logging.info("延时数据")











