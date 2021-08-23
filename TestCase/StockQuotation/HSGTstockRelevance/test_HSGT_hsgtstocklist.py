# test_HSGT_hsgtstocklist
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
class TestHSGThsgtstocklist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('沪股通/深股通/港股通(沪)/港股通(深)-成分股列表')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/test_HSGTData/test_HSGT_hsgtstocklist.json"))
    def test_HSGT_hsgtstocklist(self, info):

        response = zhuorui('Allstock', '沪股通/深股通/港股通(沪)/港股通(深)-成分股列表', info)
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
                assert "delay" in response.json().get("data")[i]
                assert "last" in response.json().get("data")[i]
                if "diffRate" in response.json().get("data")[i]:
                    assert "diffRate" in response.json().get("data")[i]
                if "turnover" in response.json().get("data")[i]:
                    assert "turnover" in response.json().get("data")[i]
                assert "preClose" in response.json().get("data")[i]
                if "diffPrice" in response.json().get("data")[i]:
                    assert "diffPrice" in response.json().get("data")[i]
                if "turnoverRate" in response.json().get("data")[i]:
                    assert "turnoverRate" in response.json().get("data")[i]
                if "totalMarkValue" in response.json().get("data")[i]:
                    assert "totalMarkValue" in response.json().get("data")[i]
                if "peRatioStatic" in response.json().get("data")[i]:
                    assert "peRatioStatic" in response.json().get("data")[i]
                if "comparison" in response.json().get("data")[i]:
                    assert "comparison" in response.json().get("data")[i]
                if "sharestraded" in response.json().get("data")[i]:
                    assert "sharestraded" in response.json().get("data")[i]
                if "amplitude" in response.json().get("data")[i]:
                    assert "amplitude" in response.json().get("data")[i]
                if "volumeRatio" in response.json().get("data")[i]:
                    assert "volumeRatio" in response.json().get("data")[i]
                if response.json().get("data")[i].get("delay") == False:
                    logging.info("实时数据")
                else:
                    logging.info("延时数据")
