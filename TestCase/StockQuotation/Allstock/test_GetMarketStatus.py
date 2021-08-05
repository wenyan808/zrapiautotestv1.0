# test_GetMarketStatus
import logging
import allure
import pytest
from Common.guide import zhuorui
from Common.login import login
from Common.tools.read_write_json import get_json
from glo import BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('公共分类')
class TestGetMarketStatus:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('查询市场交易状态')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/AllStockData/test_GetMarketStatus.json"))
    def test_GetMarketStatus(self, info):
        response = zhuorui("Allstock", "查询市场交易状态", info)

        assert response.status_code == 200
        if response.json().get("code") == "000000":
            assert response.json().get("code") == "000000"
            assert response.json().get("msg") == "ok"
            if "data" in response.json():
                if type(response.json().get("data")) == list:
                    for i in range(len(response.json().get("data"))):
                        assert "market" in response.json().get("data")[i]
                        assert "nowDate" in response.json().get("data")[i]
                        assert "statusCode" in response.json().get("data")[i]
                        assert "delay" in response.json().get("data")[i]
                        if response.json().get("data")[i].get("delay") == False:
                            logging.info("实时数据")
                        else:
                            logging.info("延时数据")
                        if "desc" in response.json().get("data")[i]:
                            assert "desc" in response.json().get("data")[i]
                        if "starStatusCode" in response.json().get("data")[i]:
                            assert "starStatusCode" in response.json().get("data")[i]
                        if "starNowDate" in response.json().get("data")[i]:
                            assert "starNowDate" in response.json().get("data")[i]
                elif type(response.json().get("data")) == dict:
                    assert "market" in response.json().get("data")
                    assert "nowDate" in response.json().get("data")
                    assert "statusCode" in response.json().get("data")
                    assert "delay" in response.json().get("data")
                    if response.json().get("data").get("delay") == False:
                        logging.info("实时数据")
                    else:
                        logging.info("延时数据")
                else:
                    raise TypeError(print(type(response.json().get("data"))))
