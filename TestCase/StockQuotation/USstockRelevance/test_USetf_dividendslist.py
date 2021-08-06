# test_USetf_dividendslist

import logging
import allure
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login

# @pytest.mark.skip(reason="调试中")
@allure.feature('美股相关')
class TestUSetfdividendslist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('美股etf分红派息详情页')
    def test_USetf_dividendslist(self):
        response = zhuorui("Allstock", "美股etf分红派息详情页")
        assert_data(response, '000000', 'ok')

        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                assert "list" in response.json().get("data")
                for i in range(len(response.json().get("data").get("list"))):
                    assert response.json().get("data").get("list")[i].get("currency") == "美元"
                    assert "exemptionDate" in response.json().get("data").get("list")[i]
                    assert "divPerShare" in response.json().get("data").get("list")[i]
                # assert response.json().get("data").get("total") == 65
                assert response.json().get("data").get("pageSize") == 15
                assert response.json().get("data").get("currentPage") == 1
                # print(response.json().get("data"))

            else:
                logging.info("data是空的集合")

        else:
            logging.info("无data数据")

