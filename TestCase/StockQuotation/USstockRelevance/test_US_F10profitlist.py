# test_US_F10profitlist

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

    @allure.story('美股F10获取利润表详情页信息')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/USStockData/test_US_F10profitlist.json"))
    def test_US_F10profitlist(self, info):
        response = zhuorui("Allstock", "美股F10获取利润表详情页信息",info)
        assert_data(response, '000000', 'ok')

        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                assert "list" in response.json().get("data")
                for i in range(len(response.json().get("data").get("list"))):
                    assert response.json().get("data").get("list")[i].get("currency") == "USD"
                    assert response.json().get("data").get("list")[i].get("reportType") == str(info.get("type"))
                    assert "reportType" in response.json().get("data").get("list")[i]
                    assert "date" in response.json().get("data").get("list")[i]
                    assert "currency" in response.json().get("data").get("list")[i]
                    assert "businessIncome" in response.json().get("data").get("list")[i]
                    assert "businessIncomeAndExpenses" in response.json().get("data").get("list")[i]
                    assert "pretaxProfit" in response.json().get("data").get("list")[i]
                    assert "incomeTax" in response.json().get("data").get("list")[i]
                    assert "netProfit" in response.json().get("data").get("list")[i]
                    assert "netProfitBelongToShareholdersOfListedCompany" in response.json().get("data").get("list")[i]
                    assert "operatingProfit" in response.json().get("data").get("list")[i]
                assert "total" in response.json().get("data")
                assert response.json().get("data").get("pageSize") == 15
                assert response.json().get("data").get("currentPage") == 1
                # print(response.json().get("data"))

            else:
                logging.info("data是空的集合")

        else:
            logging.info("无data数据")
