# test_USetf_constituentstock
import logging
import allure
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


# @pytest.mark.skip(reason="调试中")
@allure.feature('美股相关')
class TestUSetfConstituentstock:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('美股etf成分股组合（十大成分股+持仓构成）')
    def test_USetf_constituentstock(self):
        response = zhuorui("Allstock", "美股etf成分股组合（十大成分股+持仓构成）")
        assert_data(response, '000000', 'ok')

        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                assert "tenStocks" in response.json().get("data")
                for i in range(len(response.json().get("data").get("tenStocks"))):
                    assert "ts" in response.json().get("data").get("tenStocks")[i]
                    assert "code" in response.json().get("data").get("tenStocks")[i]
                    assert "type" in response.json().get("data").get("tenStocks")[i]
                    assert "name" in response.json().get("data").get("tenStocks")[i]
                    assert "rate" in response.json().get("data").get("tenStocks")[i]
                assert "position" in response.json().get("data")
                assert "num" in response.json().get("data").get("position")
                assert "industry" in response.json().get("data").get("position")
                for i in range(len(response.json().get("data").get("position").get("industry"))):
                    assert "code" in response.json().get("data").get("position").get("industry")[i]
                    assert "name" in response.json().get("data").get("position").get("industry")[i]
                    assert "rate" in response.json().get("data").get("position").get("industry")[i]

            else:
                logging.info("data为空，无数据")

        else:
            logging.info("无data字段")
