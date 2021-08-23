# test_US_newsstocktobelistedlist
import logging
import allure
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login

# @pytest.mark.skip(reason="调试中")
@allure.feature('美股相关')
class TestUSNewsstocktobelistedlist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('新股日历获取待上市列表')
    def test_US_newsstocktobelistedlist(self):
        response = zhuorui("Allstock", "新股日历获取待上市列表")
        assert_data(response, '000000', 'ok')

        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                for i in range(len(response.json().get("data"))):
                    assert "ts" in response.json().get("data")[i]
                    assert "code" in response.json().get("data")[i]
                    assert "type" in response.json().get("data")[i]
                    assert "name" in response.json().get("data")[i]
                    assert "ipoDate" in response.json().get("data")[i]
                    assert "ipoPriceLow" in response.json().get("data")[i]
                    assert "ipoPriceHigh" in response.json().get("data")[i]
                    assert "shares" in response.json().get("data")[i]
            else:
                logging.info("data为空，无数据")

        else:
            logging.info("无data字段")