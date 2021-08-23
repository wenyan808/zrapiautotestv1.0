# test_US_F10dividendlist
import logging
import allure
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login



# @pytest.mark.skip(reason="调试中")
@allure.feature('美股相关')
class TestUSF10dividendlist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('分红派息-查看详情_all')
    def test_US_F10dividendlist_all(self):
        response = zhuorui("Allstock", "分红派息-查看详情_all")
        assert_data(response, '000000', 'ok')

        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                assert "pageSize" in response.json().get("data")
                assert "pageSize" in response.json().get("data")
                assert "currentPage" in response.json().get("data")
                # assert "list" in response.json().get("data")
                assert response.json().get("data").get("total") == 0
                assert response.json().get("data").get("pageSize") == 15
                assert response.json().get("data").get("currentPage") == 1


            else:
                logging.info("data为空，无数据")

        else:
            logging.info("无data字段")

    @allure.story('分红派息-查看详情_必传值')
    def test_US_F10dividendlist_tscode(self):
        response = zhuorui("Allstock", "分红派息-查看详情_必传值")
        assert_data(response, '000000', 'ok')

        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                assert "pageSize" in response.json().get("data")
                assert "pageSize" in response.json().get("data")
                assert "currentPage" in response.json().get("data")
                # assert "list" in response.json().get("data")
                assert response.json().get("data").get("total") == 0
                assert response.json().get("data").get("pageSize") == 15
                assert response.json().get("data").get("currentPage") == 1


            else:
                logging.info("data为空，无数据")

        else:
            logging.info("无data字段")