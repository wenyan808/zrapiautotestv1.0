# test_US_newsstockcount
import logging
import allure
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login

# @pytest.mark.skip(reason="调试中")
@allure.feature('美股相关')
class TestUSNewsstockcount:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('新股日历获取待上市、今日上市数量')
    def test_US_newsstockcount(self):
        response = zhuorui("Allstock", "新股日历获取待上市、今日上市数量")
        assert_data(response, '000000', 'ok')

        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                assert "toBeListed" in response.json().get("data")
                assert "listed" in response.json().get("data")
            else:
                logging.info("data为空，无数据")

        else:
            logging.info("无data字段")