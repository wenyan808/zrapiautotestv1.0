# test_US_F10assetsliabilitylist

import logging
import allure
import pytest
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
from Common.tools.read_write_json import get_json
from glo import BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('美股相关')
class TestUSF10profitlist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('美股F10获取资产负债表详情页信息')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/USStockData/test_US_F10assetsliabilitylist.json"))
    def test_US_F10assetsliabilitylist(self, info):

        response = zhuorui('Allstock', '美股F10获取资产负债表详情页信息',info)
        assert_data(response, '000000', 'ok')

        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                assert "list" in response.json().get("data")
                for i in range(len(response.json().get("data").get("list"))):
                    assert response.json().get("data").get("list")[i].get("currency") == "USD"
                    assert response.json().get("data").get("list")[i].get("reportType") == str(info.get("type"))
                    assert "date" in response.json().get("data").get("list")[i]
                    assert "currency" in response.json().get("data").get("list")[i]
                    assert "reportType" in response.json().get("data").get("list")[i]
                    assert "totalAssets" in response.json().get("data").get("list")[i]
                    assert "cashAndCashEquivalents" in response.json().get("data").get("list")[i]
                    assert "accountsReceivable" in response.json().get("data").get("list")[i]
                    assert "stock" in response.json().get("data").get("list")[i]
                    assert "intangibleAssets" in response.json().get("data").get("list")[i]
                    assert "otherAssets" in response.json().get("data").get("list")[i]
                    assert "totalCurrentAssets" in response.json().get("data").get("list")[i]
                    assert "totalLiabilities" in response.json().get("data").get("list")[i]
                    if "shortTermLoan" in response.json().get("data").get("list")[i]:
                        assert "shortTermLoan" in response.json().get("data").get("list")[i]
                    assert "accountsPayable" in response.json().get("data").get("list")[i]
                    assert "totalCurrentLiabilities" in response.json().get("data").get("list")[i]
                    assert "longTermLiabilities" in response.json().get("data").get("list")[i]
                    assert "deferredTax" in response.json().get("data").get("list")[i]
                    assert "totalOwnerEquity" in response.json().get("data").get("list")[i]
                    if "preferredStock" in response.json().get("data").get("list")[i]:
                        assert "preferredStock" in response.json().get("data").get("list")[i]
                    if "minorityInterest" in response.json().get("data").get("list")[i]:
                        assert "minorityInterest" in response.json().get("data").get("list")[i]
                assert "total" in response.json().get("data")
                assert response.json().get("data").get("pageSize") == 15
                assert response.json().get("data").get("currentPage") == 1
                # print(response.json().get("data"))

            else:
                logging.info("data是空的集合")

        else:
            logging.info("无data数据")
